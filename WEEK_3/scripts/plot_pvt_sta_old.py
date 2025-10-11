import os
import re
import pandas as pd
import matplotlib.pyplot as plt

base_dir = "reports/pvt"
corners = sorted(os.listdir(base_dir))

def read_value_from_file(filepath):
    if not os.path.exists(filepath):
        return 0.0
    with open(filepath) as f:
        text = f.read()
    match = re.search(r"(-?\d+\.?\d*)", text)
    return float(match.group(1)) if match else 0.0

data = []
for corner in corners:
    corner_path = os.path.join(base_dir, corner)

    wns_setup = read_value_from_file(os.path.join(corner_path, "wns_setup.rpt"))
    tns_setup = read_value_from_file(os.path.join(corner_path, "tns_setup.rpt"))
    wns_hold  = read_value_from_file(os.path.join(corner_path, "wns_hold.rpt"))
    tns_hold  = read_value_from_file(os.path.join(corner_path, "tns_hold.rpt"))

    # Extract worst slacks from summaries if available
    def extract_slack(filename, label):
        path = os.path.join(corner_path, filename)
        if not os.path.exists(path):
            return 0.0
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            if "slack" in line.lower() or "Slack" in line:
                num = re.findall(r"-?\d+\.\d+", line)
                if num:
                    return float(num[-1])
        return 0.0

    worst_setup_slack = extract_slack("3_setup_summary.rpt", "setup")
    worst_hold_slack  = extract_slack("4_hold_summary.rpt", "hold")

    data.append({
        "PVT_CORNER": corner,
        "Worst Setup Slack": worst_setup_slack,
        "Worst Hold Slack": worst_hold_slack,
        "WNS": wns_setup if wns_setup != 0 else wns_hold,
        "TNS": tns_setup if tns_setup != 0 else tns_hold
    })

df = pd.DataFrame(data)
df.to_csv("pvt_summary.csv", index=False)
print("\n=== PVT SUMMARY ===")
print(df.to_string(index=False))

# === Plotting ===
plt.figure(figsize=(8, 4))
plt.plot(df["PVT_CORNER"], df["Worst Setup Slack"], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("Worst Setup Slack")
plt.ylabel("Slack (ns)")
plt.tight_layout()
plt.savefig("worst_setup_slack.png")

plt.figure(figsize=(8, 4))
plt.plot(df["PVT_CORNER"], df["Worst Hold Slack"], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("Worst Hold Slack")
plt.ylabel("Slack (ns)")
plt.tight_layout()
plt.savefig("worst_hold_slack.png")

plt.figure(figsize=(8, 4))
plt.plot(df["PVT_CORNER"], df["WNS"], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("WNS (Worst Negative Slack)")
plt.ylabel("WNS (ns)")
plt.tight_layout()
plt.savefig("wns_plot.png")

plt.figure(figsize=(8, 4))
plt.plot(df["PVT_CORNER"], df["TNS"], marker='o')
plt.xticks(rotation=45, ha='right')
plt.title("TNS (Total Negative Slack)")
plt.ylabel("TNS (ns)")
plt.tight_layout()
plt.savefig("tns_plot.png")

print("\nPlots saved as:")
print(" - worst_setup_slack.png")
print(" - worst_hold_slack.png")
print(" - wns_plot.png")
print(" - tns_plot.png")

