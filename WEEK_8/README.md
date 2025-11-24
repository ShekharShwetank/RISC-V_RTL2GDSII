# Week 8: Multi-Corner, Multi-Stage Static Timing Analysis (STA) for VSDBabySoC

## Executive Summary

This deliverable presents a comprehensive **multi-corner, multi-stage Static Timing Analysis (STA)** of the VSDBabySoC design implemented on the **SkyWater 130nm (sky130hd) PDK** using the **OpenROAD** flow. The analysis systematically evaluates timing closure across **16 industry-standard PVT corners** and **4 critical design stages** (post-synthesis → post-routing), providing complete visibility into design timing robustness.

### Key Findings

| Metric | Post-Synthesis | Post-Route | Status |
|--------|----------------|------------|--------|
| **Setup Violations** | 4/16 corners | 6/16 corners | SS corners require optimization |
| **Hold Violations** | 0/16 corners | 0/16 corners | All corners clean |
| **Best WNS** | 8.79 ns (ff_100C_1v95) | 7.76 ns (ff_100C_1v95) | Fast corners meet timing |
| **Worst WNS** | -8.94 ns (ss_n40C_1v35) | -4.90 ns (ss_100C_1v40) | Slow corners need work |

---

## Table of Contents

1. [Overview](#overview)
2. [Design Configuration](#design-configuration)
3. [PVT Corners Analyzed](#pvt-corners-analyzed)
4. [Methodology](#methodology)
5. [Directory Structure](#directory-structure)
6. [Flow Scripts](#flow-scripts)
7. [How to Run](#how-to-run)
8. [Results Analysis](#results-analysis)
9. [Timing Visualizations](#timing-visualizations)
10. [Week 3 vs Week 8 Comparison](#week-3-vs-week-8-comparison)
11. [Conclusions and Recommendations](#conclusions-and-recommendations)
12. [References](#references)

---

## Overview

Static Timing Analysis (STA) is a critical verification methodology that validates timing performance without requiring dynamic simulation. This multi-corner analysis ensures the VSDBabySoC design meets timing requirements across all expected Process, Voltage, and Temperature (PVT) variations that the chip may encounter during operation.

### Objectives

- Perform STA at **4 design stages**: Post-Synthesis, Post-Placement, Post-CTS, and Post-Route
- Analyze timing across **16 PVT corners** covering TT, FF, and SS process conditions
- Extract key timing metrics: **WNS**, **TNS**, **WHS**, **THS**
- Track timing evolution through the physical design flow
- Identify critical paths and corners requiring optimization
- Generate automated reports and visualizations for signoff

---

## Design Configuration

| Parameter | Value |
|-----------|-------|
| **Design Name** | VSDBabySoC |
| **Technology Node** | SkyWater 130nm (sky130hd) |
| **Target Clock Period** | 11 ns (~91 MHz) |
| **Clock Source** | `pll/CLK` (PLL-generated clock) |
| **EDA Tool** | OpenROAD v2.0-26087-g3bcda7705d |
| **SPEF File Size** | 23 MB (extracted parasitics) |

### Design Components

- **RISC-V Core**: rvmyth (TL-Verilog generated Verilog)
- **PLL Macro**: avsdpll (analog IP)
- **DAC Macro**: avsddac (analog IP)
- **Standard Cells**: sky130_fd_sc_hd library

---

## PVT Corners Analyzed

The analysis covers **16 comprehensive PVT corners** to ensure robust timing closure:

### Corner Classification

| Process | Temperature | Voltages | Purpose |
|---------|-------------|----------|---------|
| **TT** (Typical-Typical) | 25°C, 100°C | 1.80V | Nominal operation |
| **FF** (Fast-Fast) | -40°C, 100°C | 1.56V, 1.65V, 1.76V, 1.95V | Hold time analysis (best-case) |
| **SS** (Slow-Slow) | -40°C, 100°C | 1.28V, 1.35V, 1.40V, 1.44V, 1.60V, 1.76V | Setup time analysis (worst-case) |

### Complete Corner List

```
TT Corners (2):     tt_025C_1v80, tt_100C_1v80
FF Corners (6):     ff_100C_1v65, ff_100C_1v95, ff_n40C_1v56, ff_n40C_1v65, ff_n40C_1v76, ff_n40C_1v95
SS Corners (8):     ss_100C_1v40, ss_100C_1v60, ss_n40C_1v28, ss_n40C_1v35, ss_n40C_1v40, ss_n40C_1v44, ss_n40C_1v60, ss_n40C_1v76
```

---

## Methodology

### Design Stages Analyzed

| Stage | Database | SDC | Parasitics | Description |
|-------|----------|-----|------------|-------------|
| **Post-Synthesis** | `1_synth.v` | `1_synth.sdc` | Estimated | Gate-level netlist timing |
| **Post-Placement** | `3_place.odb` | `3_place.sdc` | Estimated | After standard cell placement |
| **Post-CTS** | `4_cts.odb` | `4_cts.sdc` | Estimated | After clock tree insertion |
| **Post-Route** | `5_route.odb` | `5_route.sdc` | `6_final.spef` | Final signoff timing |

### Timing Metrics Extracted

| Metric | Description | Signoff Requirement |
|--------|-------------|---------------------|
| **WNS** (Worst Negative Slack) | Most critical setup timing violation | WNS ≥ 0 |
| **TNS** (Total Negative Slack) | Sum of all setup violations | TNS = 0 |
| **WHS** (Worst Hold Slack) | Most critical hold timing violation | WHS ≥ 0 |
| **THS** (Total Hold Slack) | Sum of all hold violations | THS = 0 |

### Slack Equations

**Setup Slack:**
\[
\text{WNS}_{\text{setup}} = T_{\text{clk}} - (T_{\text{clk-q}} + T_{\text{logic}} + T_{\text{setup}} + T_{\text{skew}} + T_{\text{uncertainty}})
\]

**Hold Slack:**
\[
\text{WHS}_{\text{hold}} = T_{\text{clk-q}} + T_{\text{logic}} - (T_{\text{hold}} + T_{\text{skew}})
\]

---

## Directory Structure

```
WEEK_8/
├── README.md                           # This documentation file
├── week8.pdf                           # Assignment instructions
│
└── flow/
    ├── run_multi_corner_sta.sh         # Main STA automation script
    ├── extract_timing_metrics.py       # Metrics extraction script
    ├── plot_timing_graphs.py           # Visualization generation script
    │
    ├── designs/sky130hd/VSDBabySoC/
    │   ├── config.mk                   # Design configuration
    │   ├── src/module/                 # RTL source files
    │   │   ├── vsdbabysoc.v            # Top-level SoC module
    │   │   ├── rvmyth.v                # RISC-V CPU core
    │   │   ├── avsdpll.v               # PLL behavioral model
    │   │   └── avsddac.v               # DAC behavioral model
    │   ├── sdc/                        # Timing constraints
    │   ├── lib/                        # Macro liberty files
    │   ├── lef/                        # Macro LEF files
    │   └── gds/                        # Macro GDSII files
    │
    ├── platforms/sky130hd/lib/         # 16 PVT corner liberty files
    │   ├── sky130_fd_sc_hd__tt_025C_1v80.lib
    │   ├── sky130_fd_sc_hd__ff_*.lib   # Fast corners
    │   └── sky130_fd_sc_hd__ss_*.lib   # Slow corners
    │
    ├── results/sky130hd/VSDBabySoC/base/
    │   ├── 1_synth.v                   # Synthesized netlist
    │   ├── 3_place.odb                 # Post-placement database
    │   ├── 4_cts.odb                   # Post-CTS database
    │   ├── 5_route.odb                 # Post-route database
    │   ├── 6_final.spef                # Extracted parasitics (23MB)
    │   └── 6_final.gds                 # Final GDSII layout
    │
    ├── logs/sta_corners/               # 64 individual STA log files
    │   └── {stage}_{corner}.log
    │
    └── reports/sta_across_pvt/
        ├── {stage}_{corner}_setup.rpt  # 128 detailed timing reports
        ├── {stage}_{corner}_hold.rpt
        ├── {stage}_{corner}_summary.txt # 64 summary files
        ├── timing_metrics_all.csv      # Consolidated CSV metrics
        ├── timing_metrics_all.json     # Structured JSON metrics
        ├── week3_baseline.json         # Week 3 reference data
        ├── week3_vs_week8_comparison.csv
        └── graphs/
            ├── setup_slack_heatmap.png
            ├── wns_comparison.png
            ├── tns_comparison.png
            ├── whs_comparison.png
            ├── ths_comparison.png
            └── violations_by_corner_type.png
```

---

## Flow Scripts

### 1. `run_multi_corner_sta.sh`

**Purpose:** Automates STA execution across all 64 combinations (16 corners × 4 stages)

**Key Features:**
- Iterates through all PVT corners and design stages
- Loads appropriate liberty files for each corner
- Reads design databases (ODB) or netlists (Verilog)
- Applies SPEF parasitics for post-route analysis
- Generates setup and hold timing reports
- Extracts WNS, TNS, WHS, THS metrics

**Usage:**
```bash
cd ~/OpenROAD-flow-scripts/flow
./run_multi_corner_sta.sh
```

**Key Code Sections:**
```bash
# PVT Corner Definition
declare -A CORNERS=(
  ["tt_025C_1v80"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
  ["ff_100C_1v95"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_100C_1v95.lib"
  ["ss_n40C_1v28"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v28.lib"
  # ... 16 total corners
)

# STA Commands (Tcl)
report_checks -path_delay max -format full_clock_expanded  # Setup analysis
report_checks -path_delay min -format full_clock_expanded  # Hold analysis
set wns_max [sta::worst_slack_cmd "max"]
set tns_max [sta::total_negative_slack_cmd "max"]
```

### 2. `extract_timing_metrics.py`

**Purpose:** Parses STA reports and generates consolidated summaries

**Key Features:**
- Extracts WNS, TNS, WHS, THS from summary files
- Generates CSV and JSON output formats
- Creates Week 3 vs Week 8 comparison tables
- Prints summary statistics

**Usage:**
```bash
python3 extract_timing_metrics.py reports/sta_across_pvt
```

**Output Files:**
- `timing_metrics_all.csv` - Human-readable table (4.6 KB)
- `timing_metrics_all.json` - Structured data (8.5 KB)
- `week3_vs_week8_comparison.csv` - Progress tracking

### 3. `plot_timing_graphs.py`

**Purpose:** Generates timing visualization graphs

**Key Features:**
- Line plots for WNS, TNS, WHS, THS across stages
- Heatmap showing setup slack distribution
- Bar charts for violations by corner type
- Color-coded corner regions (TT/FF/SS)

**Usage:**
```bash
python3 plot_timing_graphs.py reports/sta_across_pvt/timing_metrics_all.json reports/sta_across_pvt/graphs
```

**Output Graphs:**
- `wns_comparison.png` - WNS across all corners and stages
- `tns_comparison.png` - Total negative slack trends
- `whs_comparison.png` - Hold slack analysis
- `setup_slack_heatmap.png` - Visual corner/stage matrix
- `violations_by_corner_type.png` - Violation distribution

---

## How to Run

### Prerequisites

```bash
# System Requirements
- Ubuntu 24.04 LTS (or compatible)
- OpenROAD-flow-scripts installed
- Python 3.10+ with matplotlib, numpy

# Install Python dependencies
pip3 install matplotlib numpy
```

### Step-by-Step Execution

```bash
# Step 1: Navigate to flow directory
cd ~/OpenROAD-flow-scripts/flow

# Step 2: Source environment
source ../env.sh

# Step 3: Run multi-corner STA (generates 64 analyses)
chmod +x run_multi_corner_sta.sh
./run_multi_corner_sta.sh
# Runtime: ~30-60 minutes depending on system

# Step 4: Extract timing metrics
chmod +x extract_timing_metrics.py
python3 extract_timing_metrics.py reports/sta_across_pvt

# Step 5: Generate visualization graphs
chmod +x plot_timing_graphs.py
python3 plot_timing_graphs.py reports/sta_across_pvt/timing_metrics_all.json reports/sta_across_pvt/graphs

# Step 6: Verify outputs
ls -lh reports/sta_across_pvt/*.csv
ls -lh reports/sta_across_pvt/graphs/*.png
```

### Expected Output Files

```
64 summary files:     reports/sta_across_pvt/*_summary.txt
128 timing reports:   reports/sta_across_pvt/*.rpt
1 CSV summary:        reports/sta_across_pvt/timing_metrics_all.csv
1 JSON summary:       reports/sta_across_pvt/timing_metrics_all.json
6 visualization PNGs: reports/sta_across_pvt/graphs/*.png
```

---

## Results Analysis

### Setup Slack (WNS) Summary

#### Post-Synthesis Results

| Corner Type | Corners | Violations | WNS Range |
|-------------|---------|------------|-----------|
| **TT** | 2 | 0 | +7.43 to +7.51 ns |
| **FF** | 6 | 0 | +7.35 to +8.79 ns |
| **SS** | 8 | 4 | -8.94 to +6.21 ns |

#### Post-Route Results (Final Signoff)

| Corner Type | Corners | Violations | WNS Range | TNS |
|-------------|---------|------------|-----------|-----|
| **TT** | 2 | 0 | +5.61 to +5.81 ns | 0 |
| **FF** | 6 | 0 | +5.27 to +7.76 ns | 0 |
| **SS** | 8 | 6 | -4.90 to +3.53 ns | -32.0 ns total |

**Critical Failing Corners (Post-Route):**
- `ss_100C_1v40`: WNS = -4.90 ns, TNS = -6.34 ns
- `ss_n40C_1v28`: WNS = -3.65 ns, TNS = -1.56 ns
- `ss_n40C_1v60`: WNS = -2.24 ns, TNS = -9.89 ns
- `ss_n40C_1v35`: WNS = -2.10 ns, TNS = -7.57 ns
- `ss_n40C_1v40`: WNS = -1.45 ns, TNS = -4.18 ns
- `ss_n40C_1v44`: WNS = -1.07 ns, TNS = -2.40 ns

### Hold Slack (WHS) Summary

| Stage | Min WHS | Max WHS | Violations |
|-------|---------|---------|------------|
| Post-Synthesis | +1.12 ns | +9.91 ns | **0** |
| Post-Placement | +1.09 ns | +9.57 ns | **0** |
| Post-CTS | +1.08 ns | +9.50 ns | **0** |
| Post-Route | +1.02 ns | +9.00 ns | **0** |

**All 16 corners pass hold timing at all stages** - excellent hold margin maintained throughout the flow.

### Timing Evolution Across Stages

The data shows typical timing degradation patterns:

1. **Post-Synthesis → Post-Placement:** Minimal change (~0.1-0.2 ns degradation)
2. **Post-Placement → Post-CTS:** Slight improvement due to clock tree optimization
3. **Post-CTS → Post-Route:** Significant degradation (~1.5-2.0 ns) due to wire parasitics

---

## Timing Visualizations

### Setup Slack Heatmap

![Setup Slack Heatmap](flow/reports/sta_across_pvt/graphs/setup_slack_heatmap.png)

The heatmap provides a visual overview of setup slack across all corners and stages:
- **Green cells**: Positive slack (timing met)
- **Red cells**: Negative slack (timing violations)
- **SS corners** (right side) show the most critical timing

### WNS Comparison Across Stages

![WNS Comparison](flow/reports/sta_across_pvt/graphs/wns_comparison.png)

Key observations:
- FF corners maintain comfortable positive slack throughout
- SS corners degrade significantly after routing
- Worst corner transitions from `ss_n40C_1v35` (synthesis) to `ss_100C_1v40` (route)

### Violations by Corner Type

![Violations by Corner Type](flow/reports/sta_across_pvt/graphs/violations_by_corner_type.png)

Setup violations occur **exclusively in SS (slow) corners**, which is expected behavior:
- TT corners: 0 violations at all stages
- FF corners: 0 violations at all stages
- SS corners: 4-6 violations depending on stage

---

## Week 3 vs Week 8 Comparison

This comparison tracks design progress from initial synthesis (Week 3) to post-route signoff (Week 8):

### Dramatic TNS Improvements

| Corner | Week 3 TNS | Week 8 TNS | Improvement |
|--------|------------|------------|-------------|
| ss_n40C_1v28 | -48,146 ns | -1.56 ns | **99.997%** |
| ss_n40C_1v35 | -29,840 ns | -7.57 ns | **99.975%** |
| ss_n40C_1v40 | -22,478 ns | -4.18 ns | **99.981%** |
| ss_n40C_1v44 | -18,686 ns | -2.40 ns | **99.987%** |
| ss_n40C_1v60 | -7,746 ns | -9.89 ns | **99.872%** |

### WNS Improvements

| Corner | Week 3 WNS | Week 8 WNS | Δ WNS |
|--------|------------|------------|-------|
| ss_n40C_1v28 | -56.02 ns | -3.65 ns | **+52.37 ns** |
| ss_n40C_1v35 | -35.33 ns | -2.10 ns | **+33.23 ns** |
| ss_n40C_1v40 | -27.19 ns | -1.45 ns | **+25.74 ns** |

**Key Insight:** The physical design flow (synthesis → P&R) has achieved **massive timing improvements** through:
- Logic optimization during synthesis
- Timing-driven placement
- Clock tree synthesis optimization
- Post-route optimization passes

---

## Conclusions and Recommendations

### Summary

1. **Hold Timing: PASS** - All 16 corners meet hold requirements at all stages
2. **Setup Timing (TT/FF): PASS** - 10/16 corners meet setup requirements
3. **Setup Timing (SS): NEEDS WORK** - 6 SS corners have setup violations

### Root Cause Analysis

The setup violations in SS corners are primarily due to:
- **Low voltage operation** (1.28V - 1.44V) causing slower cell delays
- **Cold temperature (-40°C)** reducing carrier mobility
- **Wire parasitics** adding ~1.5-2 ns after routing

### Recommended Optimization Strategies

1. **Frequency Reduction** (Simplest)
   - Increase clock period from 11 ns to 13-14 ns
   - Eliminates all SS corner violations

2. **Aggressive Synthesis Optimization**
   ```tcl
   # In Yosys/ABC
   set_max_delay -to [all_registers] 8
   synth -top vsdbabysoc -flatten
   abc -dff -D 11000
   ```

3. **Path-Specific Optimization**
   - Identify critical paths in SS corners
   - Apply buffer insertion on long nets
   - Consider cell upsizing (HVT → SVT → LVT)

4. **Clock Tree Optimization**
   ```tcl
   # In OpenROAD CTS
   set_wire_rc -clock -layer met3
   clock_tree_synthesis -max_cap 0.15 -max_fanout 10
   ```

5. **Useful Skew Insertion**
   - Adjust clock arrival times to relax critical endpoints
   - Must be balanced with hold requirements

### Signoff Checklist

| Check | Status | Notes |
|-------|--------|-------|
| Hold timing all corners | Pass | WHS ≥ 1.02 ns |
| Setup timing TT corners | Pass | WNS ≥ 5.61 ns |
| Setup timing FF corners | Pass | WNS ≥ 5.27 ns |
| Setup timing SS corners | 6 fails | Needs optimization |
| DRC clean | Pass | See 5_route_drc.rpt |
| LVS clean | Pass | Layout matches schematic |

---

## References

### OpenROAD Documentation
- [OpenROAD Flow Scripts](https://openroad-flow-scripts.readthedocs.io/)
- [OpenROAD STA Commands](https://openroad.readthedocs.io/en/latest/user/GettingStarted.html)

### SkyWater PDK Resources
- [SkyWater SKY130 PDK Documentation](https://skywater-pdk.readthedocs.io/)
- [sky130_fd_sc_hd Standard Cell Library](https://github.com/google/skywater-pdk)

### Timing Analysis References
- Multi-Corner Multi-Mode (MCMM) Optimization Methodology
- Static Timing Analysis Fundamentals (Setup/Hold Slack Equations)

### Project Repository
- **GitHub**: [ShekharShwetank/RISC-V_RTL2GDSII](https://github.com/ShekharShwetank/RISC-V_RTL2GDSII)

---

## Author : Shwetank Shekhar

Multi-Corner, Multi-Stage STA Analysis  
VSDBabySoC Physical Design Flow  
SkyWater 130nm Technology Node  

---

*Document generated: November 2025*  
*OpenROAD Version: v2.0-26087-g3bcda7705d*
