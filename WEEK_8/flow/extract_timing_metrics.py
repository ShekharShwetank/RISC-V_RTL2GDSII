#!/usr/bin/env python3

"""
<<<<<<< HEAD
Automated Timing Metrics Extraction and Analysis Script
Extracts WNS, TNS, WHS, THS from OpenSTA timing reports across all PVT corners
Week 8 Task - VSDBabySoC Post-Layout STA Analysis
=======
Automated Timing Metrics Extraction Script
- Converts OpenSTA time units (Seconds) to Nanoseconds (ns).
- Generates stage-specific CSV tables.
- Prints a consolidated PVT SUMMARY table to the console.
Week 8 Task - VSDBabySoC
>>>>>>> 2e9d213 (added assets)
"""

import os
import re
import csv
import json
from pathlib import Path
from collections import defaultdict
import sys

class TimingMetricsExtractor:
<<<<<<< HEAD
    """Extract and organize timing metrics from OpenSTA reports"""
    
=======
>>>>>>> 2e9d213 (added assets)
    def __init__(self, reports_dir):
        self.reports_dir = Path(reports_dir)
        self.metrics = defaultdict(lambda: defaultdict(dict))
        
<<<<<<< HEAD
        # Define all PVT corners
        self.corners = [
            "tt_025C_1v80", "tt_100C_1v80",
=======
        # Define PVT corners in specific order
        self.corners = [
>>>>>>> 2e9d213 (added assets)
            "ff_100C_1v65", "ff_100C_1v95", "ff_n40C_1v56", 
            "ff_n40C_1v65", "ff_n40C_1v76", "ff_n40C_1v95",
            "ss_100C_1v40", "ss_100C_1v60", "ss_n40C_1v28",
            "ss_n40C_1v35", "ss_n40C_1v40", "ss_n40C_1v44",
<<<<<<< HEAD
            "ss_n40C_1v60", "ss_n40C_1v76"
        ]
        
        # Define design stages
        self.stages = ["postsynth", "postplace", "postcts", "postroute"]
        
    def extract_from_summary_file(self, summary_file):
        """Extract timing metrics from summary text file"""
        metrics = {
            'wns': None,
            'tns': None,
            'whs': None,
            'ths': None
=======
            "ss_n40C_1v60", "ss_n40C_1v76",
            "tt_025C_1v80", "tt_100C_1v80"
        ]
        
        self.stages = ["postsynth", "postplace", "postcts", "postroute"]
        
    def extract_from_summary_file(self, summary_file):
        metrics = {
            'setup_slack': None, # Raw Setup Slack (ns)
            'wns': None,         # Violation (min(0, setup_slack))
            'tns': None,         # Total Negative Slack (ns)
            'hold_slack': None   # Raw Hold Slack (ns)
>>>>>>> 2e9d213 (added assets)
        }
        
        try:
            with open(summary_file, 'r') as f:
                content = f.read()
                
<<<<<<< HEAD
            # Extract WNS (Worst Negative Slack)
            wns_match = re.search(r'Worst Negative Slack \(WNS\):\s*([-\d.]+)', content)
            if wns_match:
                metrics['wns'] = float(wns_match.group(1))
            
            # Extract TNS (Total Negative Slack)
            tns_match = re.search(r'Total Negative Slack \(TNS\):\s*([-\d.]+)', content)
            if tns_match:
                metrics['tns'] = float(tns_match.group(1))
            
            # Extract WHS (Worst Hold Slack)
            whs_match = re.search(r'Worst Hold Slack \(WHS\):\s*([-\d.]+)', content)
            if whs_match:
                metrics['whs'] = float(whs_match.group(1))
            
            # Extract THS (Total Hold Slack)
            ths_match = re.search(r'Total Hold Slack \(THS\):\s*([-\d.]+)', content)
            if ths_match:
                metrics['ths'] = float(ths_match.group(1))
=======
            # Helper to parse float and convert Seconds -> Nanoseconds
            def parse_value(pattern, text, scale=1e9):
                match = re.search(pattern, text)
                if match:
                    try:
                        val = float(match.group(1))
                        return val * scale
                    except ValueError:
                        return None
                return None

            # Extract Raw Setup Slack (labeled as WNS in OpenSTA summary)
            raw_setup = parse_value(r'Worst Negative Slack \(WNS\):\s*([-\d.eE]+)', content)
            if raw_setup is not None:
                metrics['setup_slack'] = raw_setup
                # WNS is violation only (capped at 0)
                metrics['wns'] = min(0.0, raw_setup)
            
            # Extract TNS (Total Negative Slack)
            # TNS is usually already negative or zero. Convert to ns.
            tns_val = parse_value(r'Total Negative Slack \(TNS\):\s*([-\d.eE]+)', content)
            if tns_val is not None:
                metrics['tns'] = tns_val
            
            # Extract Raw Hold Slack (labeled as WHS in OpenSTA summary)
            hold_val = parse_value(r'Worst Hold Slack \(WHS\):\s*([-\d.eE]+)', content)
            if hold_val is not None:
                metrics['hold_slack'] = hold_val
>>>>>>> 2e9d213 (added assets)
                
        except Exception as e:
            print(f"Error reading {summary_file}: {e}")
            
        return metrics
    
    def extract_all_metrics(self):
<<<<<<< HEAD
        """Extract metrics from all summary files"""
        print("Extracting timing metrics from all corners and stages...")
        print("=" * 60)
=======
        print("Extracting timing metrics (converting Seconds -> Nanoseconds)...")
>>>>>>> 2e9d213 (added assets)
        
        for stage in self.stages:
            for corner in self.corners:
                summary_file = self.reports_dir / f"{stage}_{corner}_summary.txt"
                
                if summary_file.exists():
                    metrics = self.extract_from_summary_file(summary_file)
                    self.metrics[stage][corner] = metrics
<<<<<<< HEAD
                    
                    # Format metrics with defensive handling for None values
                    wns_str = f"{metrics['wns']:8.4f}" if metrics['wns'] is not None else "   FAILED"
                    tns_str = f"{metrics['tns']:10.4f}" if metrics['tns'] is not None else "    FAILED"
                    
                    print(f"Extracted: {stage:12s} | {corner:16s} | "
                          f"WNS={wns_str} TNS={tns_str}")
                else:
                    print(f"Missing:   {stage:12s} | {corner:16s}")
        
        print("=" * 60)
        return self.metrics
    
    def generate_csv_report(self, output_file):
        """Generate CSV report with all timing metrics"""
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            header = ['Stage', 'PVT Corner', 'WNS', 'TNS', 'WHS', 'THS']
            writer.writerow(header)
            
            # Write data
            for stage in self.stages:
                for corner in self.corners:
                    if corner in self.metrics[stage]:
                        m = self.metrics[stage][corner]
                        row = [
                            stage,
                            corner,
                            m['wns'] if m['wns'] is not None else 'N/A',
                            m['tns'] if m['tns'] is not None else 'N/A',
                            m['whs'] if m['whs'] is not None else 'N/A',
                            m['ths'] if m['ths'] is not None else 'N/A'
                        ]
                        writer.writerow(row)
        
        print(f"\nCSV report generated: {output_file}")
    
    def generate_json_report(self, output_file):
        """Generate JSON report with all timing metrics"""
        # Convert defaultdict to regular dict for JSON serialization
=======
    
    def generate_stage_tables(self, output_dir):
        """Generate separate CSV tables for each stage"""
        output_dir = Path(output_dir)
        
        for stage in self.stages:
            filename = output_dir / f"timing_table_{stage}.csv"
            
            # Print Console Table Header
            print(f"\n=== {stage.upper()} SUMMARY ===")
            print(f"{'PVT_CORNER':<15} {'Worst Setup Slack':<18} {'Worst Hold Slack':<18} {'WNS':<10} {'TNS':<10}")
            
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                header = ['PVT Corner', 'wns', 'tns', 'worst setup_slack', 'worst hold_slack']
                writer.writerow(header)
                
                for corner in self.corners:
                    m = self.metrics[stage].get(corner, {})
                    
                    wns = m.get('wns')
                    tns = m.get('tns')
                    setup = m.get('setup_slack')
                    hold = m.get('hold_slack')
                    
                    # Format for CSV
                    csv_row = [
                        corner,
                        f"{wns:.4f}" if wns is not None else 'N/A',
                        f"{tns:.4f}" if tns is not None else 'N/A',
                        f"{setup:.4f}" if setup is not None else 'N/A',
                        f"{hold:.4f}" if hold is not None else 'N/A'
                    ]
                    writer.writerow(csv_row)
                    
                    # Print to Console (formatted exactly as requested)
                    if setup is not None:
                        print(f"{corner:<15} {setup:>17.2f} {hold:>17.2f} {wns:>10.2f} {tns:>10.2f}")
                    else:
                        print(f"{corner:<15} {'N/A':>17} {'N/A':>17} {'N/A':>10} {'N/A':>10}")
            
            print(f"Saved: {filename}")

    def generate_json_report(self, output_file):
        # Convert defaultdict to dict
>>>>>>> 2e9d213 (added assets)
        json_data = {
            stage: {
                corner: metrics 
                for corner, metrics in corners.items()
            }
            for stage, corners in self.metrics.items()
        }
<<<<<<< HEAD
        
        with open(output_file, 'w') as f:
            json.dump(json_data, f, indent=2)
        
        print(f"JSON report generated: {output_file}")
    
    def generate_comparison_table(self, week3_data_file, output_file):
        """Generate Week 3 vs Week 8 comparison table"""
        
        # Load Week 3 data (assuming it's in JSON format)
        week3_metrics = {}
        if Path(week3_data_file).exists():
            with open(week3_data_file, 'r') as f:
                week3_metrics = json.load(f)
        
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            header = [
                'PVT Corner',
                'WNS (Week 3)', 'WNS (Week 8)', 'WNS Δ',
                'TNS (Week 3)', 'TNS (Week 8)', 'TNS Δ',
                'WHS (Week 3)', 'WHS (Week 8)', 'WHS Δ',
                'THS (Week 3)', 'THS (Week 8)', 'THS Δ'
            ]
            writer.writerow(header)
            
            # Compare post-synthesis (Week 3) with post-route (Week 8)
            for corner in self.corners:
                week3 = week3_metrics.get('postsynth', {}).get(corner, {})
                week8 = self.metrics.get('postroute', {}).get(corner, {})
                
                if week8:
                    row = [corner]
                    
                    # WNS comparison
                    w3_wns = week3.get('wns', 0)
                    w8_wns = week8.get('wns', 0)
                    row.extend([w3_wns, w8_wns, w8_wns - w3_wns if w3_wns else 'N/A'])
                    
                    # TNS comparison
                    w3_tns = week3.get('tns', 0)
                    w8_tns = week8.get('tns', 0)
                    row.extend([w3_tns, w8_tns, w8_tns - w3_tns if w3_tns else 'N/A'])
                    
                    # WHS comparison
                    w3_whs = week3.get('whs', 0)
                    w8_whs = week8.get('whs', 0)
                    row.extend([w3_whs, w8_whs, w8_whs - w3_whs if w3_whs else 'N/A'])
                    
                    # THS comparison
                    w3_ths = week3.get('ths', 0)
                    w8_ths = week8.get('ths', 0)
                    row.extend([w3_ths, w8_ths, w8_ths - w3_ths if w3_ths else 'N/A'])
                    
                    writer.writerow(row)
        
        print(f"Comparison table generated: {output_file}")
    
    def print_summary(self):
        """Print summary statistics"""
        print("\n" + "=" * 60)
        print("TIMING ANALYSIS SUMMARY")
        print("=" * 60)
        
        for stage in self.stages:
            print(f"\n{stage.upper()}:")
            
            wns_values = [m['wns'] for m in self.metrics[stage].values() 
                         if m.get('wns') is not None]
            whs_values = [m['whs'] for m in self.metrics[stage].values() 
                         if m.get('whs') is not None]
            
            if wns_values:
                worst_wns = min(wns_values)
                best_wns = max(wns_values)
                print(f"  Setup Slack Range: {worst_wns:.4f} to {best_wns:.4f} ns")
            else:
                print(f"  Setup Slack Range: NO VALID DATA")
            
            if whs_values:
                worst_whs = min(whs_values)
                best_whs = max(whs_values)
                print(f"  Hold Slack Range:  {worst_whs:.4f} to {best_whs:.4f} ns")
            else:
                print(f"  Hold Slack Range:  NO VALID DATA")
            
            # Count corners with violations
            if wns_values:
                setup_violations = sum(1 for v in wns_values if v < 0)
                print(f"  Setup Violations: {setup_violations}/{len(wns_values)} corners")
            
            if whs_values:
                hold_violations = sum(1 for v in whs_values if v < 0)
                print(f"  Hold Violations:  {hold_violations}/{len(whs_values)} corners")


def main():
    """Main execution function"""
    
    # Get reports directory from command line or use default
=======
        with open(output_file, 'w') as f:
            json.dump(json_data, f, indent=2)
        print(f"\nJSON Data generated: {output_file}")

def main():
>>>>>>> 2e9d213 (added assets)
    if len(sys.argv) > 1:
        reports_dir = sys.argv[1]
    else:
        reports_dir = "reports/sta_across_pvt"
    
<<<<<<< HEAD
    # Check if directory exists
    if not Path(reports_dir).exists():
        print(f"Error: Reports directory not found: {reports_dir}")
        print("Please run the STA analysis script first.")
        sys.exit(1)
    
    # Create extractor instance
    extractor = TimingMetricsExtractor(reports_dir)
    
    # Extract all metrics
    extractor.extract_all_metrics()
    
    # Generate output reports
    output_dir = Path(reports_dir)
    extractor.generate_csv_report(output_dir / "timing_metrics_all.csv")
    extractor.generate_json_report(output_dir / "timing_metrics_all.json")
    
    # Generate comparison table if Week 3 data is available
    week3_file = output_dir / "week3_baseline.json"
    if week3_file.exists():
        extractor.generate_comparison_table(
            week3_file, 
            output_dir / "week3_vs_week8_comparison.csv"
        )
    else:
        print(f"\nNote: Week 3 baseline data not found at {week3_file}")
        print("Skipping Week 3 vs Week 8 comparison table generation.")
    
    # Print summary statistics
    extractor.print_summary()
    
    print("\n" + "=" * 60)
    print("Metric extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()

=======
    if not Path(reports_dir).exists():
        print(f"Error: Directory not found: {reports_dir}")
        sys.exit(1)
    
    extractor = TimingMetricsExtractor(reports_dir)
    extractor.extract_all_metrics()
    
    output_dir = Path(reports_dir)
    extractor.generate_stage_tables(output_dir)
    extractor.generate_json_report(output_dir / "timing_metrics_all.json")

if __name__ == "__main__":
    main()
>>>>>>> 2e9d213 (added assets)
