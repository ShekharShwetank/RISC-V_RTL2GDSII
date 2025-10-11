#!/usr/bin/env python3
"""
parse_pvt_and_plot.py
Reads per-corner reports in reports/pvt/ and aggregates:
 - worst setup slack (from _5_worst_slack_max.rpt or _3_setup_full.rpt)
 - worst hold slack (from _5_worst_slack_min.rpt or _4_hold_full.rpt)
 - WNS (report_wns outputs)
 - TNS (report_tns outputs)

Outputs:
 - reports/pvt_summary.csv
 - reports/pvt_worst_setup.png
 - reports/pvt_worst_hold.png
 - reports/pvt_wns.png
 - reports/pvt_tns.png
"""
from pathlib import Path
import re, csv
import matplotlib.pyplot as plt

PVT_DIR = Path("reports/pvt")
OUT = Path("reports")
OUT.mkdir(exist_ok=True)

# helper: find files for each corner label (by prefix)
def corners_from_dir(p):
    labels = set()
    for f in p.glob("*"):
        name = f.name
        # extract prefix before first dot or underscore
        m = re.match(r"^([^. _]+)[._].*$", name)
        if m:
            labels.add(m.group(1))
    return sorted(labels)

def read_single_value_from_file(p, patterns):
    # open file and search for a numeric value in lines that contain any pattern
    if not p.exists():
        return None
    txt = p.read_text(errors="ignore")
    for line in txt.splitlines():
        for pat in patterns:
            if pat.lower() in line.lower():
                # pick last number on the line
                nums = re.findall(r"[-+]?\d*\.?\d+|\d+", line)
                if nums:
                    return float(nums[-1])
    # fallback: find first numeric anywhere
    nums = re.findall(r"[-+]?\d*\.?\d+|\d+", txt)
    if nums:
        return float(nums[0])
    return None

# main gather
rows = []
labels = corners_from_dir(PVT_DIR)
print("Detected corner labels:", labels)
for lbl in labels:
    # try standard files (constructed by run_sta_per_corner.sh)
    wns_file = PVT_DIR / f"{lbl}._wns.rpt"
    tns_file = PVT_DIR / f"{lbl}._tns.rpt"
    worst_max = PVT_DIR / f"{lbl}._5_worst_slack_max.rpt"
    worst_min = PVT_DIR / f"{lbl}._5_worst_slack_min.rpt"
    # fallback to setup/hold full
    setup_full = PVT_DIR / f"{lbl}._3_setup_full.rpt"
    hold_full  = PVT_DIR / f"{lbl}._4_hold_full.rpt"

    wns = read_single_value_from_file(wns_file, ["wns", "worst negative slack", "worst setup slack", "worst slack"])
    tns = read_single_value_from_file(tns_file, ["tns", "total negative slack", "total slack"])
    worst_setup = read_single_value_from_file(worst_max, ["slack", "worst setup"])
    worst_hold = read_single_value_from_file(worst_min, ["slack", "worst hold"])

    # fallback: if worst_setup/worst_hold None, try parse setup_full & hold_full by extracting top numeric slack
    if worst_setup is None and setup_full.exists():
        # Seek lines with 'slack' keyword and take min
        txt = setup_full.read_text()
        nums = [float(n) for n in re.findall(r"[-+]?\d*\.?\d+|\d+", txt)]
        if nums:
            worst_setup = min(nums)

    if worst_hold is None and hold_full.exists():
        txt = hold_full.read_text()
        nums = [float(n) for n in re.findall(r"[-+]?\d*\.?\d+|\d+", txt)]
        if nums:
            worst_hold = min(nums)

    rows.append({
        "corner": lbl,
        "worst_setup": worst_setup,
        "worst_hold": worst_hold,
        "wns": wns,
        "tns": tns
    })

# write CSV
csvp = OUT / "pvt_summary.csv"
with csvp.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["corner","worst_setup","worst_hold","wns","tns"])
    w.writeheader()
    for r in rows:
        w.writerow(r)

print("Wrote", csvp)

# --- plotting helper ---
def plot_metric(metric_key, out_png, title, yfmt="{:.2f}"):
    xs = [r["corner"] for r in rows]
    ys = [r.get(metric_key) if r.get(metric_key) is not None else float('nan') for r in rows]
    plt.figure(figsize=(10,4))
    plt.plot(xs, ys, marker='o', linewidth=2)
    for i,y in enumerate(ys):
        if y is not None and (y==y): # not nan
            plt.text(i, y, yfmt.format(y), ha='center', va='bottom', color='red', fontsize=9)
    plt.xticks(rotation=30, ha='right')
    plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
    print("Wrote", out_png)

# generate 4 charts
plot_metric("worst_setup", OUT / "pvt_worst_setup.png", "Worst Setup Slack")
plot_metric("worst_hold", OUT / "pvt_worst_hold.png", "Worst Hold Slack")
plot_metric("wns", OUT / "pvt_wns.png", "WNS")
plot_metric("tns", OUT / "pvt_tns.png", "TNS")

