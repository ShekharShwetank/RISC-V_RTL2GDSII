# VSDBabySoC: Post-Synthesis Verification and Static Timing Analysis using OpenSTA

This document provides a comprehensive walkthrough of the post-synthesis verification and static timing analysis (STA) flow for the `vsdbabysoc` System-on-Chip. The project verifies the gate-level netlist (synthesized as per [WEEK_2/VSDBabySoC/README.md](../WEEK_2/VSDBabySoC/README.md)) using Gate-Level Simulation (GLS) and performs STA with OpenSTA to ensure timing closure, validate setup and hold constraints, and identify the critical path limiting performance.

## Table of Contents

0.  [Post-Synthesis Verification (GLS)](#0-post-synthesis-verification-gls)
1.  [STA Flow Overview](#1-sta-flow-overview)
2.  [Key Concept: Timing Constraints and SDC](#2-key-concept-timing-constraints-and-sdc)
3.  [STA Fundamentals](#3-sta-fundamentals)
4.  [The STA Script](#4-the-sta-script)
5.  [Executing STA](#5-executing-sta)
6.  [STA Results](#6-sta-results)
7.  [Timing Analysis and Critical Path Evaluation](#7-timing-analysis-and-critical-path-evaluation)
8.  [Conclusion](#8-conclusion)

## Pre-requisites

- Install OpenSTA, Yosys, Icarus Verilog, and GTKWave. Refer to their respective documentation for installation instructions in WEEK_0 and LOGS.
- Install Sandpiper for Verilog generation from TL-Verilog: rvmyth is in TL-Verilog.

  - **Command**:

    ```bash
    pip3 install pyyaml click sandpiper-saas
    sandpiper-saas -i ./src/module/*.tlv -o rvmyth.v --bestsv --noline -p verilog --outdir ./src/module/
    ```

  - **Note**: The `rvmyth.v` file is generated from `rvmyth.tlv` using Sandpiper. This file is included in the synthesis and simulation processes.

  - **Files**:
    ```bash
    path/to/VSDBabySoC$ tree -a
    .
    ├── assets
    │   ├── opensta_main_view.png
    │   ├── opensta_installation.png
    │   ├── sta_execution.png
    │   ├── setup_path_visual.png
    │   ├── hold_path_visual.png
    │   ├── critical_path_graph.png
    │   ├── sta_summary_report.png
    │   ├── timing_closure.png
    │   └── comp_pre_vs_post_synth_sim.png
    ├── reports
    │   ├── 1_clocks.rpt
    │   ├── 3_setup_report.rpt
    │   ├── 4_hold_report.rpt
    │   ├── 5_total_negative_slack.rpt
    │   ├── 6_worst_negative_slack.rpt
    │   └── 6_critical_path.rpt
    ├── STA
    │   ├── final.sdc
    │   ├── run_sta.tcl
    │   └── sta_run.log
    └── src
        ├── gds
        │   ├── avsddac.gds
        │   └── avsdpll.gds
        ├── gls_model
        │   ├── primitives.v
        │   └── sky130_fd_sc_hd.v
        ├── include
        │   ├── sandpiper_gen.vh
        │   ├── sandpiper.vh
        │   ├── sp_default.vh
        │   └── sp_verilog.vh
        ├── layout_conf
        │   ├── rvmyth
        │   │   ├── config.tcl
        │   │   └── pin_order.cfg
        │   └── vsdbabysoc
        │       ├── config.tcl
        │       ├── macro.cfg
        │       └── pin_order.cfg
        ├── lef
        │   ├── avsddac.lef
        │   └── avsdpll.lef
        ├── lib
        │   ├── avsddac.lib
        │   ├── avsdpll.lib
        │   └── sky130_fd_sc_hd__tt_025C_1v80.lib
        ├── module
        │   ├── avsddac_stub.v
        │   ├── avsddac.v
        │   ├── avsdpll_stub.v
        │   ├── avsdpll.v
        │   ├── clk_gate.v
        │   ├── pseudo_rand_gen.sv
        │   ├── pseudo_rand.sv
        │   ├── rvmyth_gen.v
        │   ├── rvmyth.tlv
        │   ├── rvmyth.v
        │   ├── testbench.rvmyth.post-routing.v
        │   ├── testbench.v
        │   └── vsdbabysoc.v
        ├── script
        │   ├── sta.conf
        │   ├── verilog_to_lib.pl
        │   └── yosys.ys
        └── sdc
            ├── vsdbabysoc_layout.sdc
            └── vsdbabysoc_synthesis.sdc
    ```

## 0\. Post-Synthesis Verification (GLS)

Post-Synthesis Verification (GLS) was performed as detailed in [WEEK_2/VSDBabySoC/README.md](../WEEK_2/VSDBabySoC/README.md), confirming functional equivalence between the RTL and gate-level netlist.

![GLS Waveform Comparison](assets/comp_pre_vs_post_synth_sim.png)

## 1\. STA Flow Overview

The STA process analyzes the timing of the synthesized netlist to ensure it meets timing constraints without setup or hold violations.

  - **Inputs**:
      - Gate-level netlist (`vsdbabysoc_netlist.v`)
      - Technology timing libraries (`.lib` files)
      - SDC constraints file
  - **Tool**: `OpenSTA` Static Timing Analyzer
  - **Output**: Timing reports (setup, hold, critical path)

## 2\. Key Concept: Timing Constraints and SDC

Timing constraints define the operating environment for STA, including clocks, delays, and uncertainties.

#### `STA/final.sdc`

```tcl
create_clock -name core_clk -period 10 [get_ports clk]
set_input_delay 2 -clock core_clk [get_ports reset]
set_output_delay 2 -clock core_clk [all_outputs]
set_clock_uncertainty 0.1 [get_clocks core_clk]
```

- Clock period = 10 ns ⇒ Maximum frequency = 100 MHz.
- Input/Output delays account for external interfacing.
- Clock uncertainty models jitter.

## 3\. STA Fundamentals

Refer to [STA_fundamentals_summary.md](STA_fundamentals_summary.md) for a comprehensive summary of STA concepts from the Udemy course.

## 4\. The STA Script

We use a TCL script (`STA/run_sta.tcl`) to automate OpenSTA analysis.

#### `STA/run_sta.tcl`

```tcl
read_liberty src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_verilog reports/vsdbabysoc_netlist.v
link_design vsdbabysoc
read_sdc STA/final.sdc

report_clocks > reports/1_clocks.rpt
report_checks -path_delay min > reports/4_hold_report.rpt
report_checks -path_delay max > reports/3_setup_report.rpt
report_tns > reports/5_total_negative_slack.rpt
report_wns > reports/6_worst_negative_slack.rpt
report_checks -path_delay max -fields {slew capacitance input_pins nets fanout} -digits 4 > reports/6_critical_path.rpt
```

## 4\. Executing STA

With the script ready, STA is run with:

```bash
sta -no_splash STA/run_sta.tcl | tee STA/sta_run.log
```

The full execution log can be found in `STA/sta_run.log`.

## 5\. STA Results

The STA completed successfully, generating timing reports in `reports/`. Key statistics from the reports:

- Clock: core_clk with period 11.00 ns (from 1_clocks.rpt).
- Worst slack (max) (or) WNS: +2.26 ns (from 5_worst_slack.rpt).
- Setup paths: All met with slack +2.26 ns (from 3_setup_report.rpt).
- Hold paths: All met with slack +0.03 ns (from 4_hold_report.rpt).
- No unconstrained paths with violations (from 2_unconstrained.rpt).
- TNS: 0.00 ns (no violations).

Detailed reports:
- `1_clocks.rpt`: Clock properties.
- `2_unconstrained.rpt`: Unconstrained paths (worst case).
- `3_setup_report.rpt`: Setup timing checks.
- `4_hold_report.rpt`: Hold timing checks.
- `5_worst_slack.rpt`: Worst slack summary.
- `6_critical_path.rpt` and `6_critical_path_full.rpt`: Critical path details.

Additional files:
- `sta_summary.txt`: STA extraction summary.
- `parsed_*.txt`: Parsed timing data.
- `generate_timing_graph.py`: Python script for generating timing graphs.
- Graphviz .dot and .png files: Visualizations of critical paths (e.g., critical_path.png, critical_path_improved.png).
- `pvt/` and `pvt_old/`: Folders for PVT variation analysis (if performed).

![STA Summary Report](assets/sta_summary_report.png)

## 6\. Timing Analysis and Critical Path Evaluation

### Setup Path Analysis

From `reports/3_setup_report.rpt`:

```log
Startpoint: core/_9085_ (rising edge-triggered flip-flop clocked by core_clk)
Endpoint: core/_8462_ (rising edge-triggered flip-flop clocked by core_clk)
Path Group: core_clk
Path Type: max

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock core_clk (rise edge)
   0.00    0.00   clock network delay (ideal)
   0.00    0.00 ^ core/_9085_/CLK (sky130_fd_sc_hd__dfxtp_1)
   8.43    8.43 ^ core/_9085_/Q (sky130_fd_sc_hd__dfxtp_1)
  -0.25    8.19 v core/_6479_/Y (sky130_fd_sc_hd__a21oi_1)
   0.00    8.19 v core/_8462_/D (sky130_fd_sc_hd__dfxtp_1)
           8.19   data arrival time

  11.00   11.00   clock core_clk (rise edge)
   0.00   11.00   clock network delay (ideal)
   0.00   11.00   clock reconvergence pessimism
          11.00 ^ core/_8462_/CLK (sky130_fd_sc_hd__dfxtp_1)
  -0.55   10.45   library setup time
          10.45   data required time
---------------------------------------------------------
          10.45   data required time
          -8.19   data arrival time
---------------------------------------------------------
           2.26   slack (MET)
```

**Setup Slack Formula:**

\[
Slack_{setup} = Required\ Time - Arrival\ Time = 10.45 - 8.19 = +2.26\ ns
\]

✅ Setup timing met.

![Setup Path Visualization](assets/setup_path_visual.png)

### Hold Path Analysis

From `reports/4_hold_report.rpt`:

```log
Startpoint: reset (input port clocked by core_clk)
Endpoint: core/_9088_ (rising edge-triggered flip-flop clocked by core_clk)
Path Group: core_clk
Path Type: min

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock core_clk (rise edge)
   0.00    0.00   clock network delay (ideal)
   0.00    0.00 ^ input external delay
   0.00    0.00 ^ reset (in)
   0.00    0.00 ^ core/_9088_/D (sky130_fd_sc_hd__dfxtp_1)
           0.00   data arrival time

   0.00    0.00   clock core_clk (rise edge)
   0.00    0.00   clock network delay (ideal)
   0.00    0.00   clock reconvergence pessimism
           0.00 ^ core/_9088_/CLK (sky130_fd_sc_hd__dfxtp_1)
  -0.03   -0.03   library hold time
          -0.03   data required time
---------------------------------------------------------
          -0.03   data required time
          -0.00   data arrival time
---------------------------------------------------------
           0.03   slack (MET)
```

**Hold Slack Formula:**

\[
Slack_{hold} = Arrival\ Time - Required\ Time = 0.00 - (-0.03) = +0.03\ ns
\]

✅ Hold timing met.

![Hold Path Visualization](assets/hold_path_visual.png)

### Critical Path Evaluation

The critical path is the longest delay path, limiting clock speed. From `reports/6_critical_path_full.rpt`:

```log
Startpoint: core/_9085_ (rising edge-triggered flip-flop clocked by core_clk)
Endpoint: core/_8462_ (rising edge-triggered flip-flop clocked by core_clk)
Path Group: core_clk
Path Type: max

  Delay    Time   Description
---------------------------------------------------------
   0.00    0.00   clock core_clk (rise edge)
   0.00    0.00   clock network delay (ideal)
   0.00    0.00 ^ core/_9085_/CLK (sky130_fd_sc_hd__dfxtp_1)
   8.43    8.43 ^ core/_9085_/Q (sky130_fd_sc_hd__dfxtp_1)
  -0.25    8.19 v core/_6479_/Y (sky130_fd_sc_hd__a21oi_1)
   0.00    8.19 v core/_8462_/D (sky130_fd_sc_hd__dfxtp_1)
           8.19   data arrival time

  11.00   11.00   clock core_clk (rise edge)
   0.00   11.00   clock network delay (ideal)
   0.00   11.00   clock reconvergence pessimism
          11.00 ^ core/_8462_/CLK (sky130_fd_sc_hd__dfxtp_1)
  -0.55   10.45   library setup time
          10.45   data required time
---------------------------------------------------------
          10.45   data required time
          -8.19   data arrival time
---------------------------------------------------------
           2.26   slack (MET)
```

- Critical path dominated by combinational logic (8.19 ns delay).
- Achievable frequency ≈ 90.9 MHz (1 / (11.0 ns - 2.26 ns slack) ≈ 90.9 MHz).
- Visualizations: reports/critical_path.png, reports/critical_path_improved.png, reports/critical_path_with_lib_delays.png.
- Graphviz .dot files: critical_path.dot, critical_path_improved.dot, etc.
- Parsed data in reports/parsed_critical_path_full.txt.

![Critical Path Graph](assets/critical_path_graph.png)

## 7\. Conclusion

This process successfully verified the `vsdbabysoc` gate-level netlist through GLS and STA. Timing closure was achieved with positive slacks for setup and hold checks. The critical path was identified, confirming the design's performance limits. The design is now ready for physical design stages.
