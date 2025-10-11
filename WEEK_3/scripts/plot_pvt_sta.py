# Enhanced plot_pvt_sta.py — parses OpenSTA PVT reports for both violations and clean corners

import os, re
import pandas as pd
import matplotlib.pyplot as plt

BASE = "reports/pvt"

def extract_last_slack(path):
    """Extract the last numeric slack value from a hold/setup summary report."""
    if not os.path.exists(path):
        return None
    slack = None
    with open(path) as f:
        for line in f:
            # Match floating-point numbers at the end of each line
            m = re.search(r"(-?\d+\.\d+|-?\d+)\s*$", line.strip())
            if m:
                slack = float(m.group(1))
    return slack

def read_scalar(path):
    """Extract first float from WNS/TNS single-value reports."""
    if not os.path.exists(path):
        return None
    with open(path) as f:
        m = re.search(r"(-?\d+\.\d+|-?\d+)", f.read())
        return float(m.group(1)) if m else None

rows = []
corners = sorted([d for d in os.listdir(BASE) if os.path.isdir(os.path.join(BASE, d))])

for corner in corners:
    path = os.path.join(BASE, corner)

    # Extract WNS/TNS
    wns_setup = read_scalar(os.path.join(path, "wns_setup.rpt")) or 0.0
    tns_setup = read_scalar(os.path.join(path, "tns_setup.rpt")) or 0.0
    wns_hold  = read_scalar(os.path.join(path, "wns_hold.rpt")) or 0.0
    tns_hold  = read_scalar(os.path.join(path, "tns_hold.rpt")) or 0.0

    # Extract worst slacks from summary reports (including positive values)
    setup_slack = extract_last_slack(os.path.join(path, "3_setup_summary.rpt"))
    hold_slack  = extract_last_slack(os.path.join(path, "4_hold_summary.rpt"))

    if setup_slack is None:
        setup_slack = wns_setup
    if hold_slack is None:
        hold_slack = wns_hold

    # Select which WNS/TNS to report
    WNS = wns_setup if wns_setup != 0 else wns_hold
    TNS = tns_setup if tns_setup != 0 else tns_hold

    rows.append({
        "PVT_CORNER": corner,
        "Worst Setup Slack": round(float(setup_slack), 3),
        "Worst Hold Slack": round(float(hold_slack), 3),
        "WNS": round(float(WNS), 3),
        "TNS": round(float(TNS), 3),
    })

df = pd.DataFrame(rows)
df.to_csv("pvt_summary.csv", index=False)
print("\n=== PVT SUMMARY ===")
print(df.to_string(index=False))

# ----------- Plotting -------------
def plot_series(x, y, title, ylabel, outpng):
    plt.figure(figsize=(9,4))
    plt.plot(x, y, marker='o', linewidth=2)
    plt.xticks(rotation=45, ha='right')
    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(outpng)
    plt.close()

plot_series(df["PVT_CORNER"], df["Worst Setup Slack"], "Worst Setup Slack vs PVT", "Slack (ns)", "pvt_worst_setup.png")
plot_series(df["PVT_CORNER"], df["Worst Hold Slack"],  "Worst Hold Slack vs PVT",  "Slack (ns)", "pvt_worst_hold.png")
plot_series(df["PVT_CORNER"], df["WNS"],               "WNS vs PVT",               "WNS (ns)",  "pvt_wns.png")
plot_series(df["PVT_CORNER"], df["TNS"],               "TNS vs PVT",               "TNS (ns)",  "pvt_tns.png")

print("\nWrote pvt_summary.csv and plots: pvt_worst_setup.png, pvt_worst_hold.png, pvt_wns.png, pvt_tns.png\n")

