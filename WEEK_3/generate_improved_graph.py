# generate_improved_graph.py
# Reads reports/6_critical_path_full.rpt (OpenSTA full_clock_expanded)
# Produces reports/critical_path_improved.dot and .png and writes parsed summary.

from pathlib import Path
import re, subprocess, sys

R = Path("reports")
infile = R / "6_critical_path_full.rpt"
if not infile.exists():
    print("ERROR: missing", infile); sys.exit(1)

txt = infile.read_text()

# --- extract the timing-table rows ---
# match rows like:
#    8.43    8.43 ^ core/_9085_/Q (sky130_fd_sc_hd__dfxtp_1)
row_re = re.compile(r"^\s*(?P<delay>[-+]?\d*\.?\d+|\d+)\s+(?P<time>[-+]?\d*\.?\d+|\d+)\s+(?P<dir>[\^v])\s+(?P<pin>[A-Za-z0-9_\/\$\.-]+)\s*\((?P<cell>[^\)]+)\)", re.M)
rows = [m.groupdict() for m in row_re.finditer(txt)]

# if rows empty, fallback to previously parsed file
if not rows:
    fallback = R / "parsed_critical_path_full.txt"
    if fallback.exists():
        lines = fallback.read_text().splitlines()
        rows = []
        for ln in lines:
            if ln.strip() and ln.split("\t")[0].isdigit():
                _, pin, cell, delay, time, dirc = ln.split("\t")
                rows.append({"delay": delay, "time": time, "dir": dirc, "pin": pin, "cell": cell})
    else:
        print("No rows found in report and no fallback parsed file. Exiting.")
        sys.exit(1)

# Normalize numeric fields
for r in rows:
    try:
        r["delay"] = float(r["delay"])
    except:
        r["delay"] = None
    try:
        r["time"] = float(r["time"])
    except:
        r["time"] = None

# --- extract arrival, required, slack ---
# lines like: "           8.19   data arrival time"
m_arr = re.search(r"^\s*([0-9]*\.?[0-9]+)\s+data arrival time", txt, re.I | re.M)
m_req = re.search(r"^\s*([0-9]*\.?[0-9]+)\s+data required time", txt, re.I | re.M)
m_slk = re.search(r"^\s*([+-]?[0-9]*\.?[0-9]+)\s+slack", txt, re.I | re.M)
arrival = float(m_arr.group(1)) if m_arr else None
required = float(m_req.group(1)) if m_req else None
slack = float(m_slk.group(1)) if m_slk else None

# --- build dot (color flops vs comb) ---
dot_lines = []
dot_lines.append('digraph critical_path {')
dot_lines.append('  rankdir=LR;')
dot_lines.append('  node [shape=box, fontname="Helvetica", style="filled", fontsize=10];')

def node_color(cellname):
    cn = cellname.lower()
    # treat dff-like cells as flipflops (dfxtp in your report)
    if "dff" in cn or "dfxtp" in cn or "dff_" in cn:
        return "lightgreen"
    # combinational gates
    return "lightblue"

for i, r in enumerate(rows):
    pin = r["pin"]
    cell = r.get("cell","")
    time = r.get("time")
    delay = r.get("delay")
    color = node_color(cell)
    label = f"{pin}\\n{cell}\\nTime: {time if time is not None else 'N/A'} ns"
    label = label.replace('"','\\"').replace('\\','\\\\')
    dot_lines.append(f'  n{i} [label="{label}", fillcolor="{color}"];')

# edges: label with per-step delay. We use the next row's 'delay' as the local step contribution
for i in range(len(rows)-1):
    # compute step delay: this report lists delay on the source step; use rows[i+1].delay for the transition shown earlier
    d = rows[i+1].get("delay")
    lab = f"{d:.2f} ns" if d is not None else ""
    dot_lines.append(f'  n{i} -> n{i+1} [label="{lab}", fontsize=10];')

dot_lines.append(f'  labelloc="t";')
dot_lines.append(f'  label="Critical path — arrival={arrival} ns, required={required} ns, slack={slack} ns";')
dot_lines.append('}')

dot_path = R / "critical_path_improved.dot"
dot_path.write_text("\n".join(dot_lines))
print("Wrote DOT:", dot_path)

# Render PNG (try graphviz python then dot)
png_path = R / "critical_path_improved.png"
rendered = False
try:
    import graphviz
    g = graphviz.Source(dot_path.read_text(), format="png")
    g.render(filename=str(png_path.with_suffix('')), cleanup=True)
    rendered = png_path.exists()
except Exception:
    try:
        subprocess.run(["dot", "-Tpng", str(dot_path), "-o", str(png_path)], check=True)
        rendered = png_path.exists()
    except Exception as e:
        print("Render failed:", e)

if rendered:
    print("Wrote PNG:", png_path)
else:
    print("PNG not created. Run: dot -Tpng", dot_path, "-o", png_path)

