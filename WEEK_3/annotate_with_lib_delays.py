"""
annotate_with_lib_delays.py

- Reads reports/parsed_critical_path_full.txt for the path nodes (must exist).
- Parses VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib to extract timing numbers
  for cells encountered on the path.
- Produces:
   - reports/critical_path_with_lib_delays.dot
   - reports/critical_path_with_lib_delays.png  (requires graphviz)
   - reports/critical_path_with_lib_delays.txt  (tabular summary)

Notes:
- Liberty parsing is best-effort: we look for timing blocks inside each cell and
  extract numeric values from cell_rise/cell_fall or any numeric tokens in timing
  blocks. Liberty timing tables are often multi-dimensional and require interpolation;
  this script uses a simple scalar extraction (first numeric value seen) for quick annotation.
- Units: script attempts to detect a 'time_unit' in the liberty file; if not found we assume ns.
"""
from pathlib import Path
import re, subprocess, sys, statistics

R = Path("reports")
lib_path = Path("VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib")
parsed_path = R / "parsed_critical_path_full.txt"
out_dot = R / "critical_path_with_lib_delays.dot"
out_png = R / "critical_path_with_lib_delays.png"
out_txt = R / "critical_path_with_lib_delays.txt"

if not parsed_path.exists():
    print("ERROR: parsed critical path not found:", parsed_path)
    print("Run parse_full_critical_path.py first.")
    sys.exit(1)
if not lib_path.exists():
    print("ERROR: liberty file not found:", lib_path)
    sys.exit(1)

lib_text = lib_path.read_text(errors="ignore")

# Try to find time unit
time_unit = "ns"
m_unit = re.search(r"time_unit\s*:\s*\"([a-zA-Z]+)\"", lib_text)
if m_unit:
    time_unit = m_unit.group(1)
else:
    # some liberty files use units(...) style
    m_unit2 = re.search(r"units\s*\(\s*time_unit\s*:\s*\"([a-zA-Z]+)\"\s*\)", lib_text)
    if m_unit2:
        time_unit = m_unit2.group(1)

# read nodes
nodes = []
with parsed_path.open() as f:
    for ln in f:
        ln = ln.strip()
        if not ln or ln.lower().startswith("parsed"):
            continue
        # lines are like: Index\tPin\tCell\tDelay(ns)\tTime(ns)\tDir
        parts = ln.split("\t")
        if len(parts) >= 3 and parts[0].isdigit():
            idx = int(parts[0])
            pin = parts[1]
            cell = parts[2]
            # attempt to read delay/time if present
            delay = None
            time = None
            if len(parts) >= 4:
                try:
                    delay = float(parts[3])
                except:
                    delay = None
            if len(parts) >= 5:
                try:
                    time = float(parts[4])
                except:
                    time = None
            nodes.append({"idx": idx, "pin": pin, "cell": cell, "delay": delay, "time": time})
# dedupe cells preserving order
cells_in_path = []
seen = set()
for n in nodes:
    c = n["cell"]
    if c not in seen:
        seen.add(c)
        cells_in_path.append(c)

# utility: extract a cell block using brace matching
def extract_cell_block(libtext, cellname):
    # find "cell ( cellname ) {" occurrences (allow whitespace)
    pat = re.compile(r"cell\s*\(\s*%s\s*\)\s*\{" % re.escape(cellname))
    m = pat.search(libtext)
    if not m:
        # try without parenthesis style: cell ( cellname ) or cell cellname { (some liberty variants)
        pat2 = re.compile(r"cell\s*\(\s*\"?%s\"?\s*\)\s*\{" % re.escape(cellname))
        m2 = pat2.search(libtext)
        if m2:
            m = m2
    if not m:
        # try a loose match: cell <cellname> { 
        pat3 = re.compile(r"cell\s+%s\s*\{" % re.escape(cellname))
        m3 = pat3.search(libtext)
        if m3:
            m = m3
    if not m:
        return None
    start = m.end()-1  # position at '{'
    # brace matching to extract block
    depth = 0
    i = start
    end = None
    while i < len(libtext):
        ch = libtext[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i
                break
        i += 1
    if end is None:
        return libtext[m.start():]  # fallback: return from start to end
    return libtext[m.start():end+1]

# best-effort numeric extraction inside a timing/cell block
num_re = re.compile(r"([-+]?\d*\.\d+|\d+)")
def extract_numeric_from_timing_block(blocktext):
    # look for cell_rise or cell_fall scalar numbers first
    m = re.search(r"cell_rise\s*\(\s*.*?values\s*\(\s*([^\)]+)\)", blocktext, re.S)
    if m:
        nums = num_re.findall(m.group(1))
        if nums:
            return float(nums[0])
    m2 = re.search(r"cell_rise\s*\(\s*([^\)]+)\)", blocktext, re.S)
    if m2:
        nums = num_re.findall(m2.group(1))
        if nums:
            return float(nums[0])
    # search for "intrinsic" or "cell_fall" or timing metric numbers
    for token in ("intrinsic", "cell_fall", "cell_rise", "output_net_delay"):
        mm = re.search(r"%s[^\d\w\-]*([^\n;]+)" % token, blocktext, re.I)
        if mm:
            nums = num_re.findall(mm.group(1))
            if nums:
                return float(nums[0])
    # otherwise, harvest first numeric in any timing() subblock
    # find "timing" blocks and pick first number inside
    tpat = re.compile(r"timing\s*\([^)]*\)\s*\{", re.I)
    tm = tpat.search(blocktext)
    if tm:
        # find the matching block text for this timing block
        start = tm.end()-1
        depth = 0; i = start; blocklen = len(blocktext); endb=None
        while i < blocklen:
            ch = blocktext[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    endb = i
                    break
            i += 1
        if endb:
            tb = blocktext[tm.start():endb+1]
            nums = num_re.findall(tb)
            if nums:
                return float(nums[0])
    # last resort: any number in the cell block
    nums = num_re.findall(blocktext)
    if nums:
        return float(nums[0])
    return None

# Build mapping
cell_delay_map = {}
for c in cells_in_path:
    blk = extract_cell_block(lib_text, c)
    if not blk:
        # attempt to try name variants: many- libraries use quoted names or no prefix
        # try with and without quotes
        blk = extract_cell_block(lib_text, '"' + c + '"')
    if not blk:
        # try simplified name without any prefix if contains special chars (fallback)
        simplified = re.sub(r"[^A-Za-z0-9_]", "_", c)
        blk = extract_cell_block(lib_text, simplified)
    if not blk:
        cell_delay_map[c] = {"lib_delay": None, "note": "cell block not found"}
        continue
    libval = extract_numeric_from_timing_block(blk)
    cell_delay_map[c] = {"lib_delay": libval, "note": "ok" if libval is not None else "no numeric found"}

# Write summary table
with out_txt.open("w") as f:
    f.write("Detected time unit in liberty: %s\n\n" % time_unit)
    f.write("Index\tPin\tCell\tObserved_delay(ns)\tTime(ns)\tLib_intrinsic(%s)\tNote\n" % time_unit)
    for n in nodes:
        c = n["cell"]
        libinfo = cell_delay_map.get(c, {})
        f.write("%d\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
            n["idx"],
            n["pin"],
            c,
            str(n.get("delay")),
            str(n.get("time")),
            str(libinfo.get("lib_delay")),
            libinfo.get("note")
        ))

# Build DOT using lib delays in node labels
dot = []
dot.append('digraph critical_path {')
dot.append(' rankdir=LR;')
dot.append(' node [shape=box, fontname="Helvetica", style="filled"];')
for n in nodes:
    c = n["cell"]
    libinfo = cell_delay_map.get(c, {})
    color = "lightgreen" if ("dfxtp" in (c or "").lower() or "dff" in (c or "").lower()) else "lightblue"
    libd = libinfo.get("lib_delay")
    libstr = f"Lib: {libd} {time_unit}" if libd is not None else "Lib: N/A"
    label = f"{n['pin']}\\n{c}\\nTime: {n.get('time')} ns\\n{libstr}"
    label = label.replace('"','\\"')
    dot.append(f' n{n["idx"]} [label="{label}", fillcolor="{color}"];')

# edges: use observed step delay (next node delay) if present
for i in range(len(nodes)-1):
    d = nodes[i+1].get("delay")
    lab = f"{d} ns" if d is not None else ""
    dot.append(f' n{i} -> n{i+1} [label="{lab}"];')

dot.append(' label="Critical path annotated with library intrinsic delays";')
dot.append('}')

out_dot.write_text("\n".join(dot))
print("Wrote:", out_txt)
print("Wrote DOT:", out_dot)

# try render
rendered = False
try:
    import graphviz
    g = graphviz.Source(out_dot.read_text(), format="png")
    g.render(filename=str(out_png.with_suffix('')), cleanup=True)
    rendered = out_png.exists()
except Exception:
    try:
        subprocess.run(["dot", "-Tpng", str(out_dot), "-o", str(out_png)], check=True)
        rendered = out_png.exists()
    except Exception as e:
        print("Render failed:", e)

if rendered:
    print("Wrote PNG:", out_png)
else:
    print("PNG not created. To render: dot -Tpng", out_dot, "-o", out_png)

