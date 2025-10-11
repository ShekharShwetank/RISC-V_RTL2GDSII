import re
from pathlib import Path
import getpass
from datetime import datetime
import subprocess
import sys

ROOT = Path(".")
R = ROOT / "reports"
R.mkdir(exist_ok=True)

# Input files (adjust names if your script produced different filenames)
FILES = {
    "clocks": R / "1_clocks.rpt",
    "setup": R / "3_setup_report.rpt",
    "hold":  R / "4_hold_report.rpt",
    "worst": R / "5_worst_slack.rpt",
    "crit":  R / "6_critical_path.rpt",
}

def read_or_warn(p: Path):
    if not p.exists():
        print(f"Warning: {p} not found.")
        return ""
    return p.read_text(errors="ignore")

# 1) Parse clocks
def parse_clocks(txt):
    clocks = []
    # Typical lines: "clock_name : period = X ns, waveform = (0 5)"
    for ln in txt.splitlines():
        ln = ln.strip()
        if not ln: continue
        if "clock" in ln.lower() or re.search(r"period\s*=", ln, re.I) or re.search(r"create_clock", ln, re.I):
            clocks.append(ln)
        # also capture simple clock names lines
        m = re.match(r"^\s*([A-Za-z0-9_\-\/\$\.]+)\s*$", ln)
        if m and len(ln) < 60 and " " not in ln:
            # short token might be a clock name, add conservatively
            if ln.lower().startswith("clk") or "clk" in ln.lower():
                clocks.append(ln)
    # deduplicate preserving order
    seen = set(); out=[]
    for c in clocks:
        if c not in seen:
            seen.add(c); out.append(c)
    return out

# 2) Parse worst slack report: get a short table of worst slack endpoints
def parse_worst_slack(txt, top_k=10):
    lines = []
    for ln in txt.splitlines():
        # look for common patterns: "1) <pin> slack = -0.123 ns"
        m = re.search(r"(?P<pin>[\w\/\.\_\$\-]+)[^\d\n\-]*?(?P<slack>[-+]?[0-9]*\.?[0-9]+)\s*ns", ln)
        if m:
            lines.append((m.group("pin"), float(m.group("slack")), ln.strip()))
            continue
        # fallback: lines with "slack" word
        if "slack" in ln.lower():
            # extract last number
            mm = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", ln)
            if mm:
                lines.append((ln.strip(), float(mm[-1]), ln.strip()))
    # sort by slack ascending (worst slack = smallest)
    lines_sorted = sorted(lines, key=lambda x: x[1])
    return lines_sorted[:top_k]

# 3) Parse critical path report - heuristics
def parse_critical_path(txt):
    steps = []
    # Many report formats enumerate path steps: "1) core/_9085_/Q (pin) (delay = 0.123 ns)"
    for ln in txt.splitlines():
        ln_s = ln.strip()
        if not ln_s: continue
        # numbered line start
        if re.match(r"^\s*\d+[\.\)]\s+", ln_s):
            # try to find token that looks like instance/pin (contains / or _)
            mname = re.search(r"([A-Za-z0-9_\/\$\.-]+\/[A-Za-z0-9_]+)", ln_s)
            md = re.search(r"([0-9]+\.[0-9]+|[0-9]+)\s*ns", ln_s)
            name = mname.group(1) if mname else ln_s.split()[1]
            delay = float(md.group(1)) if md else None
            steps.append({"raw": ln_s, "name": name, "delay": delay})
            continue
        # 'From pin:' or 'To pin:'
        m2 = re.search(r"(From pin|To pin)\s*[:=]?\s*([A-Za-z0-9_\/\$\.-]+)", ln_s, re.I)
        if m2:
            steps.append({"raw": ln_s, "name": m2.group(2), "delay": None})
            continue
        # explicit pin with delay: "pin_name ... delay = 0.123 ns"
        m3 = re.search(r"([A-Za-z0-9_\/\$\.-]+)[^\d\n]*delay\s*[=:\s]\s*([0-9]+\.[0-9]+|[0-9]+)\s*ns", ln_s, re.I)
        if m3:
            steps.append({"raw": ln_s, "name": m3.group(1), "delay": float(m3.group(2))})
            continue
    # If still empty, look for any lines with '->' and split
    if not steps:
        for ln in txt.splitlines():
            if '->' in ln:
                parts = [p.strip() for p in ln.split('->') if p.strip()]
                for p in parts:
                    steps.append({"raw": ln.strip(), "name": p, "delay": None})
    return steps

# 4) Write DOT + render PNG
def build_dot(steps, dot_path):
    lines = []
    lines.append('digraph critical_path {')
    lines.append('  rankdir=LR;')
    lines.append('  node [shape=box, fontname="Helvetica"];')
    for i,s in enumerate(steps):
        lab = s["name"]
        if s["delay"] is not None:
            lab = f"{lab}\\n{float(s['delay']):.6g} ns"
        lab = lab.replace('"','\\"').replace('\\','\\\\')
        lines.append(f'  n{i} [label="{lab}"];')
    for i in range(len(steps)-1):
        lines.append(f'  n{i} -> n{i+1} ;')
    lines.append('  label="Critical path (generated)";')
    lines.append('}')
    dot_path.write_text("\n".join(lines))
    return dot_path

def try_render(dot_path, png_path):
    # Try graphviz python library first, then system 'dot'
    try:
        import graphviz
        g = graphviz.Source(dot_path.read_text(), format="png")
        g.render(filename=str(png_path.with_suffix('')), cleanup=True)
        return True
    except Exception:
        try:
            subprocess.run(["dot", "-Tpng", str(dot_path), "-o", str(png_path)], check=True)
            return True
        except Exception as e:
            print("Warning: graphviz render failed:", e)
            return False

def main():
    out_summary = R / "sta_summary.txt"
    with out_summary.open("w") as s:
        s.write(f"STA extraction run at {datetime.now().isoformat()} by {getpass.getuser()}\n\n")

    # read files
    txts = {k: read_or_warn(p) for k,p in FILES.items()}

    clocks = parse_clocks(txts["clocks"])
    worst = parse_worst_slack(txts["worst"])
    crit = parse_critical_path(txts["crit"])

    # write parsed outputs
    (R / "parsed_clocks.txt").write_text("\n".join(clocks) or "No clocks parsed\n")
    (R / "parsed_worst_slack.txt").write_text("\n".join([f"{p[0]}\t{p[1]}\t{p[2]}" for p in worst]) or "No worst slack entries\n")
    (R / "parsed_critical_path.txt").write_text("\n".join([f"{i}\t{s['name']}\t{s['delay']}\t{s['raw']}" for i,s in enumerate(crit)]) or "No critical path parsed\n")

    with out_summary.open("a") as s:
        s.write("Clocks (parsed):\n")
        for c in clocks: s.write(" - " + c + "\n")
        s.write("\nTop worst slack endpoints (parsed):\n")
        for p in worst:
            s.write(f" - {p[0]} slack={p[1]:.6g} ns  | raw: {p[2]}\n")
        s.write("\nCritical path steps (parsed):\n")
        for i,s in enumerate(crit):
            s.write(f" {i}. {s['name']}  delay={s['delay']}\n")

    # Create DOT and render
    dot_path = R / "critical_path.dot"
    png_path = R / "critical_path.png"
    if crit:
        build_dot(crit, dot_path)
        rendered = try_render(dot_path, png_path)
        print("DOT written to", dot_path)
        if rendered:
            print("PNG written to", png_path)
        else:
            print("PNG not created; run: dot -Tpng", dot_path, "-o", png_path)
    else:
        print("No critical-path steps parsed; created parsed_critical_path.txt for inspection.")

    print("Summary written to", out_summary)
    print("Done.")

if __name__ == "__main__":
    main()
