#!/usr/bin/env python3

"""
Timing Graph Visualization Script for Multi-Corner PVT Analysis
Generates comprehensive timing graphs comparing metrics across design stages
Week 8 Task - VSDBabySoC Post-Layout STA Visualization
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import sys

class TimingGraphGenerator:
    """Generate visualization graphs for timing analysis results"""
    
    def __init__(self, metrics_file):
        self.metrics_file = Path(metrics_file)
        self.metrics = self.load_metrics()
        
        # Define corner ordering for consistent plotting
        self.corner_order = [
            "tt_025C_1v80", "tt_100C_1v80",
            "ff_100C_1v65", "ff_100C_1v95", "ff_n40C_1v56", 
            "ff_n40C_1v65", "ff_n40C_1v76", "ff_n40C_1v95",
            "ss_100C_1v40", "ss_100C_1v60", "ss_n40C_1v28",
            "ss_n40C_1v35", "ss_n40C_1v40", "ss_n40C_1v44",
            "ss_n40C_1v60", "ss_n40C_1v76"
        ]
        
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
        try:
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        except Exception as e:
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
    if len(sys.argv) > 1:
        metrics_file = sys.argv[1]
    else:
        metrics_file = "reports/sta_across_pvt/timing_metrics_all.json"
    
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


if __name__ == "__main__":
    main()
