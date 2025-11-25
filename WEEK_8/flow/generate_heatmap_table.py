#!/usr/bin/env python3

"""
Heatmap Table Generator for Timing Analysis
Generates styled PNG tables with Red-Yellow-Green heatmaps for WNS, TNS, Setup, and Hold.
Matches the Excel-style conditional formatting provided in the reference.
Week 8 Task - VSDBabySoC
"""

import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from pathlib import Path
import sys

class TimingTableGenerator:
    def __init__(self, metrics_file):
        self.metrics_file = Path(metrics_file)
        self.metrics = self.load_metrics()
        
        # Order of corners as per standard reports
        self.corner_order = [
            "tt_025C_1v80", "tt_100C_1v80",
            "ff_100C_1v65", "ff_100C_1v95", "ff_n40C_1v56", 
            "ff_n40C_1v65", "ff_n40C_1v76", "ff_n40C_1v95",
            "ss_100C_1v40", "ss_100C_1v60", "ss_n40C_1v28",
            "ss_n40C_1v35", "ss_n40C_1v40", "ss_n40C_1v44",
            "ss_n40C_1v60", "ss_n40C_1v76"
        ]
        
        self.stages = ["postsynth", "postplace", "postcts", "postroute"]
        self.stage_titles = {
            "postsynth": "Post-Synthesis Timing Summary",
            "postplace": "Post-Placement Timing Summary",
            "postcts": "Post-CTS Timing Summary",
            "postroute": "Post-Routing Timing Summary"
        }

    def load_metrics(self):
        try:
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading metrics: {e}")
            sys.exit(1)

    def get_color(self, value, vmin, vmax):
        """
        Generate a color from Red (min) to Yellow to Green (max).
        """
        if vmin == vmax:
            return "#6aa84f" # Default green if all values identical
            
        # Normalize value between 0 and 1
        norm = (value - vmin) / (vmax - vmin)
        
        # Custom colormap: Red -> Yellow -> Green
        cmap = mcolors.LinearSegmentedColormap.from_list("RdYlGn", ["#e06666", "#ffd966", "#6aa84f"])
        
        return mcolors.to_hex(cmap(norm))

    def generate_table(self, stage, output_path):
        # 1. Prepare Data
        data = []
        corners = []
        
        # columns: wns, tns, setup, hold
        col_keys = ['wns', 'tns', 'setup_slack', 'hold_slack']
        col_labels = ['WNS', 'TNS', 'Worst\nSetup Slack', 'Worst\nHold Slack']
        
        # Collect numerical data for color scaling
        numerics = {k: [] for k in col_keys}
        
        for corner in self.corner_order:
            corners.append(corner)
            row_data = []
            m = self.metrics.get(stage, {}).get(corner, {})
            
            for k in col_keys:
                val = m.get(k)
                if val is None: val = 0.0
                numerics[k].append(val)
                row_data.append(val)
            data.append(row_data)

        # 2. Create Plot
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.axis('off')
        
        # 3. Create Table
        # Add headers
        table_data = []
        cell_colors = []
        
        # Calculate min/max for heatmaps per column
        col_ranges = {}
        for k in col_keys:
            vals = numerics[k]
            col_ranges[k] = (min(vals), max(vals))

        # Build rows
        for i, corner in enumerate(corners):
            row_vals = data[i]
            formatted_row = [corner] + [f"{x:.4f}" for x in row_vals]
            table_data.append(formatted_row)
            
            # Color logic
            row_colors = ["#ffffff"] # Corner name background (White)
            
            # Apply heatmap to data cells
            for j, val in enumerate(row_vals):
                k = col_keys[j]
                vmin, vmax = col_ranges[k]
                
                # Special case for WNS/TNS: 0 is usually best (Green)
                # If column represents violations (negative good, 0 best)
                # But strictly speaking, for heatmap: Higher is Better (Green)
                # So -10 is Red, 0 is Green. This fits standard logic.
                
                color = self.get_color(val, vmin, vmax)
                row_colors.append(color)
            
            cell_colors.append(row_colors)

        # Draw the table
        table = ax.table(
            cellText=table_data,
            colLabels=["PVT Corner"] + col_labels,
            cellColours=cell_colors,
            loc='center',
            cellLoc='center'
        )

        # 4. Styling
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.5) # Adjust scaling for row height

        # Header Styling
        for (row, col), cell in table.get_celld().items():
            if row == 0:
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor('#002060') # Dark Blue header
                cell.set_edgecolor('white')
            else:
                cell.set_edgecolor('black')
                cell.set_linewidth(0.5)
                # Bold the corner names
                if col == 0:
                    cell.set_text_props(weight='bold')

        # Title
        plt.title(self.stage_titles.get(stage, stage), fontsize=14, fontweight='bold', y=0.98)
        
        # Save
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Table generated: {output_path}")

    def generate_all_tables(self, output_dir):
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        
        print("\nGenerating Heatmap Tables...")
        print("=" * 60)
        
        for stage in self.stages:
            self.generate_table(stage, out / f"heatmap_table_{stage}.png")
            
        print("=" * 60)

def main():
    if len(sys.argv) > 1:
        metrics_file = sys.argv[1]
    else:
        metrics_file = "reports/sta_across_pvt/timing_metrics_all.json"
        
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = "reports/sta_across_pvt/graphs"
        
    if not Path(metrics_file).exists():
        print(f"Metrics file missing: {metrics_file}")
        sys.exit(1)
        
    generator = TimingTableGenerator(metrics_file)
    generator.generate_all_tables(output_dir)

if __name__ == "__main__":
    main()
