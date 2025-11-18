# Physical Design of BabySoC using OpenROAD and Sky130 PDK

## Objective

To execute a complete physical design flow for the `vsdbabysoc` design using the OpenROAD toolchain with the Sky130 PDK. This involves a full RTL-to-GDSII implementation, including synthesis, floorplanning, power planning, placement, clock tree synthesis, routing, parasitic extraction (SPEF), and final signoff checks. The goal is to experience a real SoC backend flow, connecting RTL design with physical implementation, and understanding the impact of physical constraints on timing, power, and area (PPA).

## Table of Contents

- [Objective](#objective)
- [Why This Task Is Important](#why-this-task-is-important)
- [Prerequisites](#prerequisites)
- [Setup of VSDBabySoC in OpenROAD Flow Scripts Directory](#setup-of-vsdbabysoc-in-openroad-flow-scripts-directory)
- [Introduction to config.mk in OpenROAD Flow](#introduction-to-configmk-in-openroad-flow)
- [Implementation](#implementation)
  - [1. Environment and Design Setup](#1-environment-and-design-setup)
  - [2. Synthesis](#2-synthesis)
  - [3. Floorplanning and Power Distribution Network (PDN)](#3-floorplanning-and-power-distribution-network-pdn)
  - [4. Placement](#4-placement)
  - [5. Clock Tree Synthesis (CTS)](#5-clock-tree-synthesis-cts)
  - [6. Routing](#6-routing)
  - [7. Parasitic Extraction (SPEF)](#7-parasitic-extraction-spef)
- [Task Reference](#task-reference)
- [Acknowledgements](#acknowledgements)

- Verification of Outputs generated at various stages of the flow:
![alt text](assets/25.png)

## Why This Task Is Important

This week’s task integrates all prior concepts into a complete physical design flow for a real System-on-Chip, the BabySoC.

*   **End-to-End Flow Mastery**: It provides hands-on experience with the entire RTL-to-GDSII process, connecting logical design with physical implementation.
*   **Impact of Physical Constraints**: You will learn how floorplan decisions, placement density, and routing choices directly affect the chip's timing, power, and area (PPA).
*   **Parasitic Extraction and STA**: This task highlights the importance of post-route parasitic extraction (SPEF) for accurate static timing analysis (STA), which is crucial for verifying that the chip will function at the desired speed. SPEF captures real parasitic R and C values for signoff-level timing analysis.
*   **Mixed-Signal Integration**: VSDBabySoC includes analog macros (PLL and DAC), making this a comprehensive example of mixed-signal physical design.

## Prerequisites

- Install OpenROAD, Yosys, and GTKWave. Refer to their respective documentation for installation instructions.
- Install Sandpiper for Verilog generation from TL-Verilog: rvmyth is in TL-Verilog.

```bash
pip3 install pyyaml click sandpiper-saas
sandpiper-saas -i ./src/module/*.tlv -o rvmyth.v --bestsv --noline -p verilog --outdir ./src/module/
```

- Clone and set up OpenROAD-flow-scripts (ORFS) for automated physical design flow.

## Setup of VSDBabySoC in OpenROAD Flow Scripts Directory

Before starting synthesis, floorplanning, placement, and routing, you must properly add the BabySoC design directories into the official OpenROAD-flow-scripts environment.

**Below are the mandatory setup steps.**

```bash
OpenROAD-flow-scripts/
└── flow/
    └── designs/
        └── sky130hd/
            └── vsdbabysoc/
                │
                ├── config.mk                   # Main OpenROAD flow config
                ├── vsdbabysoc_synthesis.sdc    # Synthesis constraints file
                ├── macro.cfg                   # Macro placement configuration
                ├── pin_order.cfg               # Pin placement order file
                │
                ├── src/                        # RTL source files for VSDBabySoC
                │   ├── vsdbabysoc.v
                │   ├── rvmyth.v
                │   ├── rvmyth_gen.v
                │   ├── clk_gate.v
                │   ├── avsddac.v
                │   └── avsdpll.v
                │
                ├── include/                    # SandPiper-generated header files
                │   ├── sandpiper.vh
                │   ├── sandpiper_gen.vh
                │   ├── sp_default.vh
                │   └── sp_verilog.vh
                │
                ├── gds/                        # Macro GDS files
                │   ├── avsddac.gds
                │   └── avsdpll.gds
                │
                ├── lef/                        # Macro LEF files
                │   ├── avsddac.lef
                │   └── avsdpll.lef
                │
                └── lib/                        # Macro Liberty timing files
                    ├── avsddac.lib
                    └── avsdpll.lib
```

## Introduction to config.mk in OpenROAD Flow

Before starting the physical design (back-end flow) in OpenROAD, the tool must know what design we are working on, where all the design files are kept, and what external IPs or macros the SoC uses.
This information is not detected automatically — we have to explicitly specify it.

This is done using a file called `config.mk`.

The `config.mk` file acts as the central configuration file for a custom design inside OpenROAD-flow-scripts. It provides all the paths and parameters required for:

a. RTL synthesis
b. Macro integration (DAC, PLL, etc.)
c. Constraint loading
d. Placement and routing setup
e. Output directory creation

**In simple words:**

- `config.mk` is the file that tells OpenROAD “this is my design, these are my RTL files, these are my macros, and this is how you should run the flow.”

- Without this file, OpenROAD will not know:
    Which Verilog files to synthesize
    Which IP blocks (macros) to include
    Where LEF/GDS/LIB files are stored
    What timing constraints to apply
    What top module to pick

Thus, `config.mk` is essential to correctly registering your design inside the OpenROAD-flow-scripts directory structure and ensuring that the entire PnR flow runs with the right inputs.

[Complete config.mk file used for VSDBabySoC:](config.mk)

## Implementation

### 1. Environment and Design Setup

Set up OpenROAD-flow-scripts:

```bash
# Clone ORFS
git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts
cd OpenROAD-flow-scripts

# Setup dependencies
sudo ./setup.sh

# Build OpenROAD locally
./build_openroad.sh --local

# Source environment
source ./env.sh
```

Verify installation:

```bash
yosys -help
openroad -help
cd flow
make
```

### 2. Synthesis

Synthesis translates the RTL Verilog code into a gate-level netlist using standard cells from the Sky130 library. Use the OpenROAD flow for synthesis.

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk synth
```

This generates the gate-level netlist and reports synthesis statistics, including cell count and area.

Screenshots of synthesis:
![alt text](assets/1.png)

### 3. Floorplanning and Power Distribution Network (PDN)

Floorplanning defines the die and core areas, places I/O pads, and sets up the power distribution network.

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk floorplan
```

To view the floorplan:

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_floorplan
```

Screenshots of floorplan setup:
![alt text](assets/2.png)
![alt text](assets/3.png)
![alt text](assets/4.png)
![alt text](assets/5.png)
![alt text](assets/6.png)

### 4. Placement

Placement positions the standard cells and macros within the core area.

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk place
```

To view placement and congestion:

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_place
```

Screenshots of placement:
![alt text](assets/7.png)
![alt text](assets/8.png)
![alt text](assets/9.png)
![alt text](assets/10.png)
![alt text](assets/11.png)
![alt text](assets/12.png)
![alt text](assets/13.png)

### 5. Clock Tree Synthesis (CTS)

CTS balances clock delays to minimize skew.

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk cts
```

Post-CTS timing reports are generated, including WNS, TNS, and violations.

[To view CTS results:](assets/reports/4_cts_final.rpt)

Screenshots of CTS:

![alt text](assets/14.png)
![alt text](assets/15.png)
![alt text](assets/16.png)
![alt text](assets/17.png)
![alt text](assets/18.png)
![alt text](assets/19.png)

### 6. Routing

Routing connects all nets using metal layers.

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk route
```

To view the routed layout:

```bash
make DESIGN_CONFIG=./designs/sky130hd/vsdbabysoc/config.mk gui_route
```

This is the most critical phase. The design fails with [ERROR GRT-0116] Global routing finished with congestion.

The Problem: The default configuration had high penalties for Metal 1 and Metal 2 layers (met1:0.25, etc.) and a high GRT_ADJUSTMENT (0.40), causing the router to run out of resources near the standard cells.

The Fix (under work): Modified config.mk to relax these constraints:

- Changed GRT_ADJUSTMENT to 0.15.
- Removed GRT_LAYER_ADJUSTMENTS to fully utilize met1 and met2.

Screenshots of routing:
![alt text](assets/21.png)
![alt text](assets/22.png)

### 7. Parasitic Extraction (SPEF)

Extract parasitics for accurate post-route STA.

SPEF (Standard Parasitic Exchange Format) contains the real, extracted parasitic R and C values for every net. This is essential for signoff STA, as pre-route estimates are inaccurate.

Use the following TCL script for extraction:

```tcl
# Extraction
if { $rcx_rules_file != "" } {
  define_process_corner -ext_model_index 0 X
  extract_parasitics -ext_model_file $rcx_rules_file

  set spef_file [make_result_file ${design}_${platform}.spef]
  write_spef $spef_file

  read_spef $spef_file
} else {
  # Use global routing based parasitics in lieu of rc extraction
  estimate_parasitics -global_routing
}
```

![alt text](assets/23.png)
![alt text](assets/24.png)
![alt text](assets/25.png)

## Task Reference

- [VSD BabySoC](https://github.com/manili/VSDBabySoC.git)
- [BabySoC Simulation](https://github.com/Subhasis-Sahu/BabySoC_Simulation.git)
- [ASIC Design](https://github.com/Akash-Perla/ASIC-Design.git)

## Acknowledgements

- [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
- [Nickson P Jose](https://github.com/nickson-jose), Physical Design Engineer, Intel Corporation.
- [R. Timothy Edwards](https://github.com/RTimothyEdwards), Senior Vice President of Analog and Design, efabless Corporation.
- [Fayiz Ferosh](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/blob/main/README.md)
