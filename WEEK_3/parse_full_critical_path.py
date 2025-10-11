"""
parse_full_critical_path.py
Parses OpenSTA 'full_clock_expanded' critical path report and generates:
 - reports/critical_path.dot
 - reports/critical_path.png (requires graphviz)
 - reports/parsed_critical_path_full.txt (human-readable)
"""
import re
from pathlib import Path
import subprocess, sys

R = Path("reports")
R.mkdir(exist_ok=True)

infile = R / "6_critical_path_full.rpt"
if not infile.exists():
    print("Error: expected", infile, "to exist. Run OpenSTA with -format full_clock_expanded first.")
    sys.exit(1)

txt = infile.read_text()

# Find the timing table block: locate header "Delay    Time   Description" and the next dashed line
m_header = re.search(r"Delay\s+Time\s+Description\s*\n[-]+\n", txt, re.IGNORECASE)
if not m_header:
    # fallback: try to find "Delay    Time" line index
    lines = txt.splitlines()
    for i,ln in enumerate(lines):
        if "Delay" in ln and "Description" in ln:
            start_idx = i+1
            break
    else:
        print("Could not find timing table header in", infile)
        start_idx = None
else:
    start_idx = len(txt[:m_header.end()].splitlines())

lines = txt.splitlines()
# parse rows until a blank line followed by "data arrival time" or until we encounter "data required time"
rows = []
i = start_idx
while i < len(lines):
    ln = lines[i].rstrip()
    # stop conditions
    if re.match(r"^\s*$", ln):
        # check if next non-empty line contains "data arrival" or "data required"
        look = None
        for j in range(i+1, min(i+6, len(lines))):
            if lines[j].strip():
                look = lines[j].strip()
                break
        if look and ("data arrival" in look.lower() or "data required" in look.lower()):
            break
    # typical line: "   8.43    8.43 ^ core/_9085_/Q (sky130_fd_sc_hd__dfxtp_1)"
    m = re.match(r"^\s*(?P<delay>[-+]?\d*\.\d+|\d+)\s+(?P<time>[-+]?\d*\.\d+|\d+)\s+(?P<dir>[\^v])\s+(?P<pin>[A-Za-z0-9_\/\$\.-]+)\s*\((?P<cell>[^\)]+)\)", ln)
    if m:
        rows.append({
            "delay": float(m.group("delay")),
            "time": float(m.group("time")),
            "dir": m.group("dir"),
            "pin": m.group("pin"),
            "cell": m.group("cell"),
            "raw": ln
        })
    else:
        # sometimes clock lines use different format: "   0.00    0.00   clock core_clk (rise edge)"
        mc = re.match(r"^\s*(?P<delay>[-+]?\d*\.\d+|\d+)\s+(?P<time>[-+]?\d*\.\d+|\d+)\s+(?P<descr>.+)$", ln)
        if mc and "clock" in mc.group("descr").lower():
            # ignore clock-only lines (but keep if you want)
            pass
        else:
            # ignore other lines
            pass
    i += 1

# find data arrival/required/slack blocks below the table (scan next 20 lines)
arrival = None
required = None
slack = None
for j in range(i, min(i+40, len(lines))):
    l = lines[j].strip()
    m_arr = re.search(r"data arrival time[:\s]*([0-9]*\.?[0-9]+)", l, re.I)
    m_req = re.search(r"data required time[:\s]*([0-9]*\.?[0-9]+)", l, re.I)
    m_slk = re.search(r"slack\s*\(?([A-Za-z]+)?\)?[:\s]*([+-]?[0-9]*\.?[0-9]+)", l, re.I)
    if m_arr:
        arrival = float(m_arr.group(1))
    if m_req:
        required = float(m_req.group(1))
    if m_slk:
        slack = float(m_slk.group(2))

# Build node list from rows: use only rows with ^ or v pins (skip clock/header rows)
nodes = []
for r in rows:
    nodes.append((r["pin"], r["cell"], r["delay"], r["time"], r["dir"]))

# write parsed text
out_txt = R / "parsed_critical_path_full.txt"
with out_txt.open("w") as f:
    f.write(f"Parsed from {infile}\n\n")
    f.write("Index\tPin\tCell\tDelay(ns)\tTime(ns)\tDir\n")
    for idx,(pin,cell,delay,time,dirc) in enumerate(nodes):
        f.write(f"{idx}\t{pin}\t{cell}\t{delay}\t{time}\t{dirc}\n")
    f.write("\nArrival: %s\nRequired: %s\nSlack: %s\n" % (arrival, required, slack))

# Build DOT
dot_lines = []
dot_lines.append('digraph critical_path {')
dot_lines.append('  rankdir=LR;')
dot_lines.append('  node [shape=record, fontname="Helvetica"];')
for idx,(pin,cell,delay,time,dirc) in enumerate(nodes):
    label = f"{pin}\\n{cell}\\nTime: {time} ns"
    dot_lines.append(f'  n{idx} [label="{label}"];')
# edges: label with delay (use the delay value from row)
for idx in range(len(nodes)-1):
    d = nodes[idx+1][2]  # delay at the next node (following the OpenSTA per-step semantics)
    dot_lines.append(f'  n{idx} -> n{idx+1} [label="{d} ns"];')
# annotate arrival/required/slack in graph label
dot_lines.append(f'  label="Critical path (arrival={arrival} ns, required={required} ns, slack={slack} ns)";')
dot_lines.append('}')
dot_path = R / "critical_path.dot"
dot_path.write_text("\n".join(dot_lines))

# Render PNG: try python graphviz, fallback to dot command
png_path = R / "critical_path.png"
rendered = False
try:
    import graphviz
    g = graphviz.Source(dot_path.read_text(), format="png")
    g.render(filename=str(png_path.with_suffix('')), cleanup=True)
    rendered = png_path.exists()
except Exception as e:
    try:
        subprocess.run(["dot", "-Tpng", str(dot_path), "-o", str(png_path)], check=True)
        rendered = png_path.exists()
    except Exception as e2:
        print("Render failed:", e, e2)

print("Wrote:", out_txt)
print("Wrote DOT:", dot_path)
if rendered:
    print("Wrote PNG:", png_path)
else:
    print("PNG not created. If graphviz is installed, run: dot -Tpng", dot_path, "-o", png_path)

