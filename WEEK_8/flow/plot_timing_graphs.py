#!/usr/bin/env python3

"""
<<<<<<< HEAD
Timing Graph Visualization Script for Multi-Corner PVT Analysis
Generates comprehensive timing graphs comparing metrics across design stages
Week 8 Task - VSDBabySoC Post-Layout STA Visualization
=======
Timing Graph Generator
Generates line graphs and heatmaps for Setup, Hold, TNS, and THS.
>>>>>>> 2e9d213 (added assets)
"""

import json
import matplotlib.pyplot as plt
<<<<<<< HEAD
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import sys

class TimingGraphGenerator:
    """Generate visualization graphs for timing analysis results"""
    
=======
import numpy as np
from pathlib import Path
import sys
import matplotlib.colors as mcolors

class TimingGraphGenerator:
>>>>>>> 2e9d213 (added assets)
    def __init__(self, metrics_file):
        self.metrics_file = Path(metrics_file)
        self.metrics = self.load_metrics()
        
<<<<<<< HEAD
        # Define corner ordering for consistent plotting
=======
>>>>>>> 2e9d213 (added assets)
        self.corner_order = [
            "tt_025C_1v80", "tt_100C_1v80",
            "ff_100C_1v65", "ff_100C_1v95", "ff_n40C_1v56", 
            "ff_n40C_1v65", "ff_n40C_1v76", "ff_n40C_1v95",
            "ss_100C_1v40", "ss_100C_1v60", "ss_n40C_1v28",
            "ss_n40C_1v35", "ss_n40C_1v40", "ss_n40C_1v44",
            "ss_n40C_1v60", "ss_n40C_1v76"
        ]
        
<<<<<<< HEAD
        # Define stages
        self.stages = ["postsynth", "postplace", "postcts", "postroute"]
        self.stage_labels = ["Post-Synthesis", "Post-CTS", "Post-Placement", "Post-Routing"]
        
        # Color scheme for different stages
        self.colors = {
            'postsynth': '#1f77b4',   # Blue
            'postplace': '#ff7f0e',   # Orange
            'postcts': '#2ca02c',     # Green
            'postroute': '#d62728'    # Red
        }
        
        self.markers = {
            'postsynth': 'o',
            'postplace': 's',
            'postcts': '^',
            'postroute': 'x'
        }
    
    def load_metrics(self):
        """Load timing metrics from JSON file"""
=======
        self.stages = ["postsynth", "postplace", "postcts", "postroute"]
        self.stage_labels = ["Post-synth", "Post-place", "Post-cts", "Post-route"]
        
        self.styles = {
            'postsynth': {'color': '#003f5c', 'marker': 'D', 'label': 'Post-Synthesis'},
            'postplace': {'color': '#ffa600', 'marker': 's', 'label': 'Post-Placement'},
            'postcts':   {'color': '#58508d', 'marker': '^', 'label': 'Post-CTS'},
            'postroute': {'color': '#bc5090', 'marker': 'x', 'label': 'Post-Routing'}
        }
    
    def load_metrics(self):
>>>>>>> 2e9d213 (added assets)
        try:
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        except Exception as e:
<<<<<<< HEAD
            print(f"Error loading metrics file: {e}")
            sys.exit(1)
    
    def extract_metric_data(self, metric_name):
        """Extract specific metric across all corners and stages"""
        data = {}
        for stage in self.stages:
            data[stage] = []
            for corner in self.corner_order:
                value = self.metrics.get(stage, {}).get(corner, {}).get(metric_name)
                data[stage].append(value if value is not None else 0)
        return data
    
    def plot_metric_comparison(self, metric_name, ylabel, title, output_file):
        """Generate comparison plot for a specific metric across all corners"""
        
        fig, ax = plt.subplots(figsize=(16, 8))
        
        # Extract data
        data = self.extract_metric_data(metric_name)
        
        # X-axis positions
        x = np.arange(len(self.corner_order))
        
        # Plot lines for each stage
        for stage in self.stages:
            ax.plot(x, data[stage], 
                   marker=self.markers[stage],
                   color=self.colors[stage],
                   linewidth=2,
                   markersize=8,
                   label=stage.replace('post', 'Post-').replace('synth', 'Synthesis').replace('cts', 'CTS').replace('place', 'Placement').replace('route', 'Routing'))
        
        # Add horizontal line at y=0 for reference
        ax.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)
        
        # Formatting
        ax.set_xlabel('PVT Corner', fontsize=12, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(self.corner_order, rotation=45, ha='right')
        ax.legend(loc='best', fontsize=10, frameon=True, shadow=True)
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # Color-code background regions for corner types
        # TT corners
        ax.axvspan(-0.5, 1.5, alpha=0.05, color='gray', label='_nolegend_')
        # FF corners
        ax.axvspan(1.5, 7.5, alpha=0.05, color='green', label='_nolegend_')
        # SS corners
        ax.axvspan(7.5, 15.5, alpha=0.05, color='red', label='_nolegend_')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Generated: {output_file}")
    
    def plot_all_metrics(self, output_dir):
        """Generate all timing metric plots"""
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        print("\nGenerating timing visualization graphs...")
        print("=" * 60)
        
        # WNS Plot
        self.plot_metric_comparison(
            'wns',
            'Worst Negative Slack (ns)',
            'WNS Across PVT Corners and Design Stages',
            output_dir / 'wns_comparison.png'
        )
        
        # TNS Plot
        self.plot_metric_comparison(
            'tns',
            'Total Negative Slack (ns)',
            'TNS Across PVT Corners and Design Stages',
            output_dir / 'tns_comparison.png'
        )
        
        # WHS Plot
        self.plot_metric_comparison(
            'whs',
            'Worst Hold Slack (ns)',
            'Worst Hold Slack Across PVT Corners and Design Stages',
            output_dir / 'whs_comparison.png'
        )
        
        # THS Plot
        self.plot_metric_comparison(
            'ths',
            'Total Hold Slack (ns)',
            'Total Hold Slack Across PVT Corners and Design Stages',
            output_dir / 'ths_comparison.png'
        )
    
    def plot_setup_slack_heatmap(self, output_file):
        """Generate heatmap showing setup slack violations"""
        
        # Extract WNS data
        wns_data = self.extract_metric_data('wns')
        
        # Convert to numpy array for heatmap
        data_array = np.array([wns_data[stage] for stage in self.stages])
        
        fig, ax = plt.subplots(figsize=(16, 6))
        
        im = ax.imshow(data_array, cmap='RdYlGn', aspect='auto', interpolation='nearest')
        
        # Set ticks and labels
        ax.set_xticks(np.arange(len(self.corner_order)))
        ax.set_yticks(np.arange(len(self.stages)))
        ax.set_xticklabels(self.corner_order, rotation=45, ha='right')
        ax.set_yticklabels([s.replace('post', 'Post-') for s in self.stages])
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Worst Negative Slack (ns)', rotation=270, labelpad=20)
        
        # Add text annotations
        for i in range(len(self.stages)):
            for j in range(len(self.corner_order)):
                text = ax.text(j, i, f'{data_array[i, j]:.2f}',
                             ha="center", va="center", color="black", fontsize=7)
        
        ax.set_title('Setup Slack Heatmap Across Design Stages and PVT Corners', 
                    fontsize=14, fontweight='bold', pad=20)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Generated: {output_file}")
    
    def plot_corner_type_summary(self, output_file):
        """Generate bar chart summarizing violations by corner type"""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        corner_types = {
            'TT': ['tt_025C_1v80', 'tt_100C_1v80'],
            'FF': [c for c in self.corner_order if c.startswith('ff_')],
            'SS': [c for c in self.corner_order if c.startswith('ss_')]
        }
        
        def count_violations(metric_name, stage):
            counts = {}
            for ctype, corners in corner_types.items():
                count = 0
                for corner in corners:
                    value = self.metrics.get(stage, {}).get(corner, {}).get(metric_name)
                    if value is not None and value < 0:
                        count += 1
                counts[ctype] = count
            return counts
        
        # Setup violations for each stage
        for ax, stage in zip([ax1, ax2, ax3, ax4], self.stages):
            violations = count_violations('wns', stage)
            
            x = np.arange(len(corner_types))
            bars = ax.bar(x, list(violations.values()), color=['gray', 'green', 'red'], alpha=0.7)
            
            ax.set_ylabel('Number of Violations', fontsize=10)
            ax.set_title(f'{stage.replace("post", "Post-").capitalize()} - Setup Violations by Corner Type',
                        fontsize=11, fontweight='bold')
            ax.set_xticks(x)
            ax.set_xticklabels(corner_types.keys())
            ax.grid(axis='y', alpha=0.3)
            
            # Add value labels on bars
            for i, bar in enumerate(bars):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{int(height)}',
                       ha='center', va='bottom', fontsize=9)
        
        plt.suptitle('Setup Timing Violations Summary by Corner Type',
                    fontsize=14, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Generated: {output_file}")
    
    def generate_all_graphs(self, output_dir):
        """Generate all visualization graphs"""
        self.plot_all_metrics(output_dir)
        self.plot_setup_slack_heatmap(Path(output_dir) / 'setup_slack_heatmap.png')
        self.plot_corner_type_summary(Path(output_dir) / 'violations_by_corner_type.png')
        
        print("=" * 60)
        print(f"All graphs generated successfully in: {output_dir}")


def main():
    """Main execution function"""
    
    # Get metrics file from command line or use default
=======
            print(f"Error: {e}")
            sys.exit(1)
    
    def get_data_series(self, metric_key):
        series = {}
        for stage in self.stages:
            values = []
            for corner in self.corner_order:
                val = self.metrics.get(stage, {}).get(corner, {}).get(metric_key)
                if val is None: val = 0.0
                values.append(val)
            series[stage] = values
        return series
    
    def plot_metric(self, metric_key, title, ylabel, filename, output_dir):
        data = self.get_data_series(metric_key)
        x = np.arange(len(self.corner_order))
        
        fig, ax = plt.subplots(figsize=(18, 9))
        
        for stage in self.stages:
            style = self.styles[stage]
            ax.plot(x, data[stage], 
                    marker=style['marker'], 
                    color=style['color'], 
                    linewidth=2.5, 
                    markersize=8,
                    label=style['label'])
            
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
        ax.set_xlabel('PVT Corner', fontsize=12, fontweight='bold')
        
        ax.set_xticks(x)
        ax.set_xticklabels(self.corner_order, rotation=90, fontsize=10, fontweight='bold')
        
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.8)
        ax.grid(True, which='both', linestyle='--', alpha=0.6)
        ax.legend(fontsize=12, frameon=True, shadow=True)
        
        plt.tight_layout()
        filepath = Path(output_dir) / filename
        plt.savefig(filepath, dpi=300)
        plt.close()
        print(f"Graph generated: {filepath}")

    def plot_heatmap(self, metric_key, title, cbar_label, filename, output_dir, cmap_name='RdYlGn'):
        data = []
        for stage in self.stages:
            row = []
            for corner in self.corner_order:
                val = self.metrics.get(stage, {}).get(corner, {}).get(metric_key)
                if val is None: val = 0.0
                row.append(val)
            data.append(row)
        
        data = np.array(data)
        
        fig, ax = plt.subplots(figsize=(20, 8))
        
        im = ax.imshow(data, cmap=cmap_name, aspect='auto')
        
        # Show all ticks
        ax.set_xticks(np.arange(len(self.corner_order)))
        ax.set_yticks(np.arange(len(self.stages)))
        
        # Label ticks
        ax.set_xticklabels(self.corner_order, rotation=45, ha="right", fontsize=10)
        ax.set_yticklabels(self.stage_labels, fontsize=12)
        
        # Loop over data dimensions and create text annotations.
        for i in range(len(self.stages)):
            for j in range(len(self.corner_order)):
                text = ax.text(j, i, f"{data[i, j]:.2f}",
                               ha="center", va="center", color="black", fontsize=9, weight='bold')
        
        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax)
        cbar.ax.set_ylabel(cbar_label, rotation=-90, va="bottom", fontsize=12)
        
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        filepath = Path(output_dir) / filename
        plt.savefig(filepath, dpi=300)
        plt.close()
        print(f"Heatmap generated: {filepath}")

    def generate_graphs(self, output_dir):
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        
        print("\nGenerating Graphs...")
        print("-" * 60)
        
        # Line Graphs
        self.plot_metric('wns', 'WNS (Violation Only)', 'Slack (ns)', 'wns_comparison.png', out)
        self.plot_metric('tns', 'TNS (Total Negative Slack)', 'Total Slack (ns)', 'tns_comparison.png', out)
        self.plot_metric('setup_slack', 'Worst Setup Slack (Raw)', 'Slack (ns)', 'setup_slack_comparison.png', out)
        self.plot_metric('hold_slack', 'Worst Hold Slack', 'Slack (ns)', 'whs_comparison.png', out)
        
        # Heatmaps
        self.plot_heatmap('setup_slack', 'Setup Slack Heatmap Across Design Stages and PVT Corners', 'Worst Setup Slack (ns)', 'setup_slack_heatmap.png', out, cmap_name='RdYlGn')
        self.plot_heatmap('hold_slack', 'Hold Slack Heatmap Across Design Stages and PVT Corners', 'Worst Hold Slack (ns)', 'hold_slack_heatmap.png', out, cmap_name='RdYlGn')
        self.plot_heatmap('tns', 'Total Negative Slack Heatmap', 'Total Negative Slack (ns)', 'tns_heatmap.png', out, cmap_name='RdYlGn') # Reversed colormap for TNS (0 is best/green)
        
        print("-" * 60)

def main():
>>>>>>> 2e9d213 (added assets)
    if len(sys.argv) > 1:
        metrics_file = sys.argv[1]
    else:
        metrics_file = "reports/sta_across_pvt/timing_metrics_all.json"
<<<<<<< HEAD
    
    # Check if file exists
    if not Path(metrics_file).exists():
        print(f"Error: Metrics file not found: {metrics_file}")
        print("Please run the extraction script first.")
        sys.exit(1)
    
    # Get output directory
    output_dir = "reports/sta_across_pvt/graphs"
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    
    # Create graph generator and generate all plots
    generator = TimingGraphGenerator(metrics_file)
    generator.generate_all_graphs(output_dir)
    
    print("\nVisualization complete!")

=======
        
    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = "reports/sta_across_pvt/graphs"
        
    if not Path(metrics_file).exists():
        print(f"Metrics file missing: {metrics_file}")
        sys.exit(1)
        
    generator = TimingGraphGenerator(metrics_file)
    generator.generate_graphs(output_dir)
>>>>>>> 2e9d213 (added assets)

if __name__ == "__main__":
    main()
