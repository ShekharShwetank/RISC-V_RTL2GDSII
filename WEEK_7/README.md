# Physical Design of BabySoC using OpenROAD and Sky130 PDK

## Objective

To execute a complete physical design flow for the `vsdbabysoc` design using the OpenROAD toolchain with the Sky130 PDK. This involves a full RTL-to-GDSII implementation, including synthesis, floorplanning, power planning, placement, clock tree synthesis, routing, and final signoff checks.

## Table of Contents

- [Objective](#objective)
- [Why This Task Is Important](#why-this-task-is-important)
- [Prerequisites](#prerequisites)
- [Implementation](#implementation)
  - [1. Environment and Design Setup](#1-environment-and-design-setup)
  - [2. Synthesis](#2-synthesis)
  - [3. Floorplanning and Power Distribution Network (PDN)](#3-floorplanning-and-power-distribution-network-pdn)
  - [4. Placement](#4-placement)
  - [5. Clock Tree Synthesis (CTS)](#5-clock-tree-synthesis-cts)
  - [6. Routing](#6-routing)
  - [7. Final Signoff and GDSII Generation](#7-final-signoff-and-gdsii-generation)
- [Task Reference](#task-reference)
- [Acknowledgements](#acknowledgements)

## Why This Task Is Important

This week’s task integrates all prior concepts into a complete physical design flow for a real System-on-Chip, the BabySoC.

*   **End-to-End Flow Mastery**: It provides hands-on experience with the entire RTL-to-GDSII process, connecting logical design with physical implementation.
*   **Impact of Physical Constraints**: You will learn how floorplan decisions, placement density, and routing choices directly affect the chip's timing, power, and area (PPA).
*   **Parasitic Extraction and STA**: This task highlights the importance of post-route parasitic extraction (SPEF) for accurate static timing analysis (STA), which is crucial for verifying that the chip will function at the desired speed.

## Prerequisites

- Install OpenROAD, Yosys, and GTKWave. Refer to their respective documentation for installation instructions.
- Install Sandpiper for Verilog generation from TL-Verilog: rvmyth is in TL-Verilog.

  ```bash
  pip3 install pyyaml click sandpiper-saas
  sandpiper-saas -i ./src/module/*.tlv -o rvmyth.v --bestsv --noline -p verilog --outdir ./src/module/
  ```

## Implementation

### 1. Environment and Design Setup

First, clone the `VSDBabySoC` repository, which contains all the necessary source files for the design.

```bash
# Clone the repository
git clone https://github.com/manili/VSDBabySoC.git
cd VSDBabySoC
```

Next, launch OpenROAD and prepare the design by loading the required technology files, libraries, and the top-level Verilog source for the BabySoC.

```bash
# Launch OpenROAD
openroad

# Load technology and library files
read_lef ./src/lef/avsddac.lef
read_lef ./src/lef/avsdpll.lef
read_liberty ./src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty ./src/lib/avsddac.lib
read_liberty ./src/lib/avsdpll.lib

# Load the top-level Verilog file
read_verilog ./src/module/vsdbabysoc.v

# Link the design to the libraries
link_design vsdbabysoc
```

### 2. Synthesis

Synthesis translates the RTL Verilog code into a gate-level netlist using standard cells from the Sky130 library. The `yosys.ys` script from the repository is used for this.

```bash
# Run Yosys to perform synthesis
yosys -c ./src/script/yosys.ys
```

This generates the gate-level netlist `vsdbabysoc_netlist.v` in the `reports` directory.

### 3. Floorplanning and Power Distribution Network (PDN)

Floorplanning defines the die and core areas, places I/O pads, and sets up the power distribution network.

```bash
# Initialize floorplan
initialize_floorplan -die_area "0 0 1000 1000" -core_area "10 10 990 990" -site unithd

# Place I/O pads
place_io

# Add tap cells and decap cells
tap_decap_or

# Generate PDN
gen_pdn
```

Screenshots of floorplan setup:

- Floorplan initialization with die and core areas.
- PDN with power rings and straps.

### 4. Placement

Placement positions the standard cells and macros within the core area.

```bash
# Global placement
global_placement

# Detailed placement
detailed_placement

# Check legality
check_placement
```

Screenshots of placement:

- Global placement view.
- Detailed placement with cells aligned to rows.
- Placement density report.

### 5. Clock Tree Synthesis (CTS)

CTS balances clock delays to minimize skew.

```bash
# Perform CTS
clock_tree_synthesis

# Optimize clock tree
clock_tree_optimization
```

### 6. Routing

Routing connects all nets using metal layers.

```bash
# Global routing
global_route

# Detailed routing
detailed_route

# Check DRC
check_drc
```

Screenshots of routing:

- Global routing guides.
- Detailed routed layout.
- DRC check results (no violations).

### 7. Final Signoff and GDSII Generation

Perform final checks and generate GDSII.

```bash
# Extract SPEF for STA
extract_parasitics -spef vsdbabysoc.spef

# Run STA
read_spef vsdbabysoc.spef
report_checks

# Generate GDSII
write_gds vsdbabysoc.gds
```

Screenshots of SPEF generation:

- SPEF extraction output.
- Parasitic report.
- Final GDSII layout.

## Task Reference

- [VSD BabySoC](https://github.com/manili/VSDBabySoC.git)
- [BabySoC Simulation](https://github.com/Subhasis-Sahu/BabySoC_Simulation.git)
- [ASIC Design](https://github.com/Akash-Perla/ASIC-Design.git)

## Acknowledgements

- [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
- [Nickson P Jose](https://github.com/nickson-jose), Physical Design Engineer, Intel Corporation.
- [R. Timothy Edwards](https://github.com/RTimothyEdwards), Senior Vice President of Analog and Design, efabless Corporation.
- [Fayiz Ferosh](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/blob/main/README.md)
