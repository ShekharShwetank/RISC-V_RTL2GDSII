# Physical Design Labs using OpenLANE and Sky130 PDK

## Objective

To perform hands-on Physical Design labs using a pre-configured VDI image and understand the complete hierarchy of digital and mixed-signal design implementation — from standard cell design to DRC and STA validation.

![alt text](assets/563.png)

## Table of Contents

- [Objective](#objective)
- [1. Inception of open-source EDA, OpenLANE and Sky130 PDK](#1-inception-of-open-source-eda-openlane-and-sky130-pdk)
  - [Theory](#theory)
  - [Implementation](#implementation)
    - [1. Run 'picorv32a' design synthesis using OpenLANE flow and generate necessary outputs.](#1-run-picorv32a-design-synthesis-using-openlane-flow-and-generate-necessary-outputs)
    - [2. Calculate the flop ratio.](#2-calculate-the-flop-ratio)
- [Section 2 - Good floorplan vs bad floorplan and introduction to library cells](#section-2---good-floorplan-vs-bad-floorplan-and-introduction-to-library-cells)
  - [Theory](#theory-1)
  - [Implementation](#implementation-1)
    - [1. Run 'picorv32a' design floorplan using OpenLANE flow and generate necessary outputs.](#1-run-picorv32a-design-floorplan-using-openlane-flow-and-generate-necessary-outputs)
    - [2. Calculate the die area in microns from the values in floorplan def.](#2-calculate-the-die-area-in-microns-from-the-values-in-floorplan-def)
    - [3. Load generated floorplan def in magic tool and explore the floorplan.](#3-load-generated-floorplan-def-in-magic-tool-and-explore-the-floorplan)
    - [4. Run 'picorv32a' design congestion aware placement using OpenLANE flow and generate necessary outputs.](#4-run-picorv32a-design-congestion-aware-placement-using-openlane-flow-and-generate-necessary-outputs)
    - [5. Load generated placement def in magic tool and explore the placement.](#5-load-generated-placement-def-in-magic-tool-and-explore-the-placement)
- [3. Design library cell using Magic Layout and ngspice characterization](#3-design-library-cell-using-magic-layout-and-ngspice-characterization)
  - [Theory](#theory-2)
  - [Implementation](#implementation-2)
    - [1. Clone custom inverter standard cell design from github repository](#1-clone-custom-inverter-standard-cell-design-from-github-repository)
    - [2. Load the custom inverter layout in magic and explore.](#2-load-the-custom-inverter-layout-in-magic-and-explore)
    - [3. Spice extraction of inverter in magic.](#3-spice-extraction-of-inverter-in-magic)
    - [4. Editing the spice model file for analysis through simulation.](#4-editing-the-spice-model-file-for-analysis-through-simulation)
    - [5. Post-layout ngspice simulations.](#5-post-layout-ngspice-simulations)
    - [6. Find problem in the DRC section of the old magic tech file for the skywater process and fix them.](#6-find-problem-in-the-drc-section-of-the-old-magic-tech-file-for-the-skywater-process-and-fix-them)
- [4. Pre-layout timing analysis and importance of good clock tree](#4-pre-layout-timing-analysis-and-importance-of-good-clock-tree)
  - [Theory](#theory-3)
  - [Implementation](#implementation-3)
    - [1. Fix up small DRC errors and verify the design is ready to be inserted into our flow.](#1-fix-up-small-drc-errors-and-verify-the-design-is-ready-to-be-inserted-into-our-flow)
    - [2. Save the finalized layout with custom name and open it.](#2-save-the-finalized-layout-with-custom-name-and-open-it)
    - [3. Generate lef from the layout.](#3-generate-lef-from-the-layout)
    - [4. Copy the newly generated lef and associated required lib files to 'picorv32a' design 'src' directory.](#4-copy-the-newly-generated-lef-and-associated-required-lib-files-to-picorv32a-design-src-directory)
    - [5. Edit 'config.tcl' to change lib file and add the new extra lef into the openlane flow.](#5-edit-configtcl-to-change-lib-file-and-add-the-new-extra-lef-into-the-openlane-flow)
    - [6. Run openlane flow synthesis with newly inserted custom inverter cell.](#6-run-openlane-flow-synthesis-with-newly-inserted-custom-inverter-cell)
    - [7. Remove/reduce the newly introduced violations with the introduction of custom inverter cell by modifying design parameters.](#7-removereduce-the-newly-introduced-violations-with-the-introduction-of-custom-inverter-cell-by-modifying-design-parameters)
    - [8. Once synthesis has accepted our custom inverter we can now run floorplan and placement and verify the cell is accepted in PnR flow.](#8-once-synthesis-has-accepted-our-custom-inverter-we-can-now-run-floorplan-and-placement-and-verify-the-cell-is-accepted-in-pnr-flow)
    - [9. Do Post-Synthesis timing analysis with OpenSTA tool.](#9-do-post-synthesis-timing-analysis-with-opensta-tool)
    - [10. Make timing ECO fixes to remove all violations.](#10-make-timing-eco-fixes-to-remove-all-violations)
    - [11. Replace the old netlist with the new netlist generated after timing ECO fix and implement the floorplan, placement and cts.](#11-replace-the-old-netlist-with-the-new-netlist-generated-after-timing-eco-fix-and-implement-the-floorplan-placement-and-cts)
    - [12. Post-CTS OpenROAD timing analysis.](#12-post-cts-openroad-timing-analysis)
    - [13. Explore post-CTS OpenROAD timing analysis by removing 'sky130_fd_sc_hd__clkbuf_1' cell from clock buffer list variable 'CTS_CLK_BUFFER_LIST'.](#13-explore-post-cts-openroad-timing-analysis-by-removing-sky130_fd_sc_hd__clkbuf_1-cell-from-clock-buffer-list-variable-cts_clk_buffer_list)
- [5. Final steps for RTL2GDS using tritonRoute and openSTA](#5-final-steps-for-rtl2gds-using-tritonroute-and-opensta)
  - [Theory](#theory-4)
  - [Implementation](#implementation-4)
    - [1. Perform generation of Power Distribution Network (PDN) and explore the PDN layout.](#1-perform-generation-of-power-distribution-network-pdn-and-explore-the-pdn-layout)
    - [2. Perfrom detailed routing using TritonRoute and explore the routed layout.](#2-perfrom-detailed-routing-using-tritonroute-and-explore-the-routed-layout)
    - [3. Post-Route OpenSTA timing analysis with the extracted parasitics of the route.](#3-post-route-opensta-timing-analysis-with-the-extracted-parasitics-of-the-route)
- [Acknowledgements](#acknowledgements)

## 1. Inception of open-source EDA, OpenLANE and Sky130 PDK

### Theory

<details>
<summary>Click to expand</summary>

#### Package

- In any embedded board we have seen, the part of the board we consider as the chip is only the ***PACKAGE*** of the chip which is nothing but a protective layer or packet bound over the actual chip and the actual manufatured chip is usually present at the center of a package wherein, the connections from package is fed to the chip by ***WIRE BOUND*** method which is none other than basic wired connection.

![alt text](assets/1.png)
![alt text](assets/2.png)
![alt text](assets/3.png)

#### Chip

- Now, taking a look inside the chip, all the signals from the external world to the chip and vice versa is passed through ***PADS***. The area bound by the pads is ***CORE*** where all the digital logic of the chip is placed. Both the core and pads make up the ***DIE*** which is the basic manufacturing unit in regards to semiconductor chips.
![alt text](assets/4.png)

- ***FOUNDRY*** is the place where the semiconductor chips are manufactured and ***FOUNDRY IP's*** are Intellectual Properties based on a specific foundry and these IP's require a specific level of intelligence to be produced whereas, repeatable digital logic blocks are called ***MACROS***.
![alt text](assets/6.png)

#### ISA (Intruction Set Architecture)

- A C program which has to be run on a specific hardware layout which is the interior of a chip in your laptop, there is certain flow to be followed.
- Initially, this particular C program is compiled in it's assembly language program which is nothing but ***RISC-V ISA (Reduced Instruction Set Compting - V Intruction Set Architecture)***.
- Following this, the assembly language program is then converted to machine language program which is the binary language logic 0 and 1 which is understood by the hardware of the computer.
- Directly after this, we've to implement this RISC-V specification using some ***RTL (a Hardware Description Language)***. Finally, from the RTL to ***Layout*** it is a standard PnR or RTL to GDSII flow.

![alt text](assets/7.png)

- For an application software to be run on a hardware there are several processes taking place. To begin with, the apps enters into a block called system software and it converts the application program to binary language. There are various layers in system software in which the major layers or components are OS (Operating System), Compiler and Assembler.
- At first the OS outputs are small function in C, C++, VB or Java language which are taken by the respective compiler and converted into instructions and the syntax of these instructions varies with the hardware architecture on which the system is implemented.
- Then, the job of the assembler is to take these instructions and convert it into it's binary format which is basically called as a machine language program. Finally, this binary language is fed to the hardware and it understands the specific functions it has to perform based on the binary code it receives.

![alt text](assets/8.png)

- For example, if we take a stopwatch app on RISC-V core, then the output of the OS could be a small C function which enters into the compiler and we get output RISC-V instructions following this, the output of the assembler will be the binary code which enters into your chip layout.

![alt text](assets/9.png)

- For the above stopwatch the following are the input and output of the compiler and assembler.

![alt text](assets/11.png)

- The output of the compiler are instructions and the output of the assembler is the binary pattern. Now, we need some RTL (a Hardware Description Language) which understands and implements the particular instructions. Then, this RTL is synthesised into a netlist in form of gates which is fabricated into the chip through a physical design implementation.

![alt text](assets/14.png)

- There are mainly 3 different parts in this course. They are:

1. RISC-V ISA
2. RTL and synthesis of RISC-V based CPU core - picorv32
3. Physical design implementation of picorv32

![alt text](assets/15.png)

#### Open-source Implementation

- For open-source ASIC design implemantation, we require the following enablers to be readily available as open-source versions. They are:-

1. RTL Designs
2. EDA Tools
3. PDK Data

- Initially in the early ages, the design and fabrication of IC's were tightly coupled and were only practiced by very few companies like TI, Intel, etc.
- In 1979, Lynn Conway and Carver Mead came up with an idea to saperate the design from the fabrication and to do this they inroduced structured design methodologies based on the λ-based design rules and published the first VLSI book "Introduction to VLSI System" which started the VLSI education.
- This methodology resulted in the emergence of the design only companies or ***"Fabless Companies"*** and fabrication only companies that we usually refer to as ***"Pure Play Fabs"***.
- The inteface between the designers and the fab by now became a set of data files and documents, that are reffered to as the ***"Process Design Kits (PDKs)"***.
- The PDK include but not limited to Device Models, Technology Information, Design Rules, Digital Standard Cell Libraries, I/O Libraries and many more.
- Since, the PDK contained variety of informations, and so they were distributed only under NDAs (Non-Disclosure Agreements) which made it in-accessible to the public.
- Recently, Google worked out an agreement with skywater to open-source the PDK for the 130nm process by skywater Technology, as a result on 30 June 2020 Google released the first ever open-source PDK.

![alt text](assets/18.png)

- ASIC design is a complex step that involves tons of steps, various methodologies and respective EDA tools which are all required for successful ASIC implementation which is achieved though an ASIC flow which is nothing but a piece of software that pulls different tools togather to carry out the design process.

![alt text](assets/19.png)

#### OpenLANE Open-source ASIC Design Implementation Flow

- The main objective of the ASIC Design Flow is to take the design from the RTL (Register Transfer Level) all the way to the GDSII, which is the format used for the final fabrication layout.

![alt text](assets/20.png)

- Synthesis is the process of convertion or translation of design RTL into circuits made out of Standard Cell Libraries (SCL) the resultant circuit is described in HDL and is usually reffered to as the Gate-Level Netlist.
- Gate-Level Netlist is functionally equivalent to the RTL.

![alt text](assets/21.png)

- The fundemental building blocks which are the standard cells have regular layouts.
- Each cell has different views/models which are utilised by different EDA tools like liberty view with electrical models of the cells, HDL behavioral models, SPICE or CDL views of the cells, Layout view which include GDSII view which is the detailed view and LEF view which is the abstract view.

![alt text](assets/22.png)

- Chip Floor Planning

![alt text](assets/23.png)

- Macro Floor Planning

![alt text](assets/24.png)

- Power Planning typically uses upper metal layers for power distribution since thay are thicker than lower metal layers and so have lower resistance and PP is done to avoid electron migration and IR drops.

![alt text](assets/25.png)

- Placement

![alt text](assets/26.png)

- Global placement provide approximate locations for all cells based on connectivity but in this stage the cells may be overlapped on each other and in detailed placement the positions obtained from global placements are minimally altered to make it legal (non-overlapping and in site-rows)

![alt text](assets/28.png)

- Clock Tree Synthesis

![alt text](assets/29.png)

- Clock skew is the time difference in arrival of clock at different components.
- Routing

![alt text](assets/30.png)

- skywater PDK has 6 routing layers in which the lowest layer is called the local interconnect layer which is a Titanium Nitride layer the following 5 layers are all Aluminium layers.

![alt text](assets/image.png)

- Global and Detailed Routing

![alt text](assets/31.png)

- Once done with the routing the final layout can be generated which undergoes various Sign-Off checks.
- Design Rules Checking (DRC) which verifies that the final layout honours all design fabrication rules.
- Layout Vs Schematic (LVS) which verifies that the final layout functionality matches the gate-level netlist that we started with.
- Static Timing Analysis (STA) to verify that the design runs at the designated clock frequency.

![alt text](assets/32.png)
![alt text](assets/33.png)
![alt text](assets/34.png)
![alt text](assets/35.png)
![alt text](assets/36.png)
![alt text](assets/37.png)
![alt text](assets/37.png)
![alt text](assets/38.png)
![alt text](assets/39.png)
![alt text](assets/40.png)
![alt text](assets/41.png)
![alt text](assets/42.png)
![alt text](assets/43.png)
![alt text](assets/44.png)
![alt text](assets/45.png)
![alt text](assets/46.png)
![alt text](assets/47.png)
![alt text](assets/48.png)
![alt text](assets/49.png)
![alt text](assets/50.png)
![alt text](assets/51.png)
![alt text](assets/52.png)
![alt text](assets/53.png)
![alt text](assets/54.png)
![alt text](assets/55.png)
![alt text](assets/56.png)
![alt text](assets/57.png)
![alt text](assets/58.png)
![alt text](assets/59.png)
![alt text](assets/60.png)
![alt text](assets/61.png)
![alt text](assets/62.png)
</details>

### Implementation

Section 1 tasks:-

1. Run 'picorv32a' design synthesis using OpenLANE flow and generate necessary outputs.
2. Calculate the flop ratio.

```math
Flop\ Ratio = \frac{Number\ of\ D\ Flip\ Flops}{Total\ Number\ of\ Cells}
```

```math
Percentage\ of\ DFF's = Flop\ Ratio * 100
```

- All section 1 logs, reports and results can be found in following run folder: [27-10_17-46](openlane_working_dir/openlane/designs/picorv32a/runs/27-10_17-46)

#### 1. Run 'picorv32a' design synthesis using OpenLANE flow and generate necessary outputs

Commands to invoke the OpenLANE flow and perform synthesis

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```

```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Exit from OpenLANE flow
exit

# Exit from OpenLANE flow docker sub-system
exit
```

Screenshots of running each commands

![alt text](assets/72.png)
![alt text](assets/73.png)
![alt text](assets/74.png)
![alt text](assets/75.png)

#### 2. Calculate the flop ratio

Screenshots of synthesis statistics report file with required values highlighted

![alt text](assets/76.png)
![alt text](assets/77.png)
![alt text](assets/78.png)

Calculation of Flop Ratio and DFF % from synthesis statistics report file

```math
Flop\ Ratio = \frac{1613}{14876} = 0.108429685
```

```math
Percentage\ of\ DFF's = 0.108429685 * 100 = 10.84296854\ \%
```

![alt text](assets/84.png)

## Section 2 - Good floorplan vs bad floorplan and introduction to library cells

### Theory
<details>
<summary>Click to expand</summary>

![alt text](assets/85.png) ![alt text](assets/86.png) ![alt text](assets/87.png) ![alt text](assets/88.png) ![alt text](assets/89.png) ![alt text](assets/90.png) ![alt text](assets/91.png) ![alt text](assets/92.png) ![alt text](assets/93.png) ![alt text](assets/94.png) ![alt text](assets/95.png) ![alt text](assets/96.png) ![alt text](assets/97.png) ![alt text](assets/98.png) ![alt text](assets/99.png) ![alt text](assets/100.png) ![alt text](assets/101.png) ![alt text](assets/102.png) ![alt text](assets/103.png) ![alt text](assets/104.png) ![alt text](assets/105.png) ![alt text](assets/106.png) ![alt text](assets/107.png) ![alt text](assets/108.png) ![alt text](assets/109.png) ![alt text](assets/110.png) ![alt text](assets/111.png) ![alt text](assets/112.png) ![alt text](assets/113.png) ![alt text](assets/114.png) ![alt text](assets/115.png) ![alt text](assets/116.png) ![alt text](assets/117.png) ![alt text](assets/118.png) ![alt text](assets/119.png) ![alt text](assets/120.png) ![alt text](assets/121.png) ![alt text](assets/122.png) ![alt text](assets/123.png) ![alt text](assets/124.png) ![alt text](assets/125.png) ![alt text](assets/126.png) ![alt text](assets/127.png) ![alt text](assets/128.png) ![alt text](assets/129.png) ![alt text](assets/130.png) ![alt text](assets/131.png)

</details>

### Implementation

Section 2 tasks:-

1. Run 'picorv32a' design floorplan using OpenLANE flow and generate necessary outputs.
2. Calculate the die area in microns from the values in floorplan def.
3. Load generated floorplan def in magic tool and explore the floorplan.
4. Run 'picorv32a' design congestion aware placement using OpenLANE flow and generate necessary outputs.
5. Load generated placement def in magic tool and explore the placement.

```math
Area\ of\ die\ in\ microns = Die\ width\ in\ microns * Die\ height\ in\ microns
```

- All logs, reports and results can be found in following run folder: [30-10_16-34](openlane_working_dir/openlane/designs/picorv32a/runs/30-10_16-34)

#### 1. Run 'picorv32a' design floorplan using OpenLANE flow and generate necessary outputs.

Commands to invoke the OpenLANE flow and perform floorplan

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```

```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Now we can run floorplan
run_floorplan
```

Screenshot of floorplan run

![alt text](assets/334.png)
![alt text](assets/335.png)
![alt text](assets/336.png)
![alt text](assets/337.png)

#### 2. Calculate the die area in microns from the values in floorplan def

Screenshot of contents of floorplan def
![alt text](assets/338.png)
![alt text](assets/339.png)

According to floorplan def

```math
1000\ Unit\ Distance = 1\ Micron
```

```math
Die\ width\ in\ unit\ distance = 660685 - 0 = 660685
```

```math
Die\ height\ in\ unit\ distance = 671405 - 0 = 671405
```

```math
Distance\ in\ microns = \frac{Value\ in\ Unit\ Distance}{1000}
```

```math
Die\ width\ in\ microns = \frac{660685}{1000} = 660.685\ Microns
```

```math
Die\ height\ in\ microns = \frac{671405}{1000} = 671.405\ Microns
```

```math
Area\ of\ die\ in\ microns = 660.685 * 671.405 = 443587.212425\ Square\ Microns
```

#### 3. Load generated floorplan def in magic tool and explore the floorplan

Commands to load floorplan def in magic in another terminal

```bash
# Change directory to path containing generated floorplan def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/17-03_12-06/results/floorplan/

# Command to load the floorplan def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.floorplan.def &
```

Screenshots of floorplan def in magic
![alt text](assets/340.png)

Equidistant placement of ports
![alt text](assets/342.png)

Port layer as set through config.tcl
![alt text](assets/343.png)
![alt text](assets/344.png)
![alt text](assets/345.png)

Decap Cells and Tap Cells
![alt text](assets/346.png)
![alt text](assets/347.png)

Diogonally equidistant Tap cells
![alt text](assets/342.png)

Unplaced standard cells at the origin
![alt text](assets/349.png)
![alt text](assets/350.png)

#### 4. Run 'picorv32a' design congestion aware placement using OpenLANE flow and generate necessary outputs

Command to run placement

```tcl
# Congestion aware placement by default
run_placement
```

Screenshots of placement run
![alt text](assets/351.png)
![alt text](assets/352.png)

#### 5. Load generated placement def in magic tool and explore the placement

Commands to load placement def in magic in another terminal

```bash
# Change directory to path containing generated placement def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/17-03_12-06/results/placement/

# Command to load the placement def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.placement.def &
```

Screenshots of floorplan def in magic
![alt text](assets/354.png)

Standard cells legally placed
![alt text](assets/355.png)
![alt text](assets/356.png)
![alt text](assets/357.png)
![alt text](assets/358.png)
![alt text](assets/359.png)

Commands to exit from current run

```tcl
# Exit from OpenLANE flow
exit

# Exit from OpenLANE flow docker sub-system
exit
```

## 3. Design library cell using Magic Layout and ngspice characterization

### Theory

<details>
<summary>Click to expand</summary>

![alt text](assets/132.png) ![alt text](assets/133.png) ![alt text](assets/134.png) ![alt text](assets/135.png) ![alt text](assets/136.png) ![alt text](assets/137.png) ![alt text](assets/138.png) ![alt text](assets/139.png) ![alt text](assets/140.png) ![alt text](assets/141.png) ![alt text](assets/142.png) ![alt text](assets/143.png) ![alt text](assets/144.png) ![alt text](assets/145.png) ![alt text](assets/146.png) ![alt text](assets/147.png) ![alt text](assets/148.png) ![alt text](assets/149.png) ![alt text](assets/150.png) ![alt text](assets/151.png) ![alt text](assets/152.png) ![alt text](assets/153.png) ![alt text](assets/154.png) ![alt text](assets/155.png) ![alt text](assets/156.png) ![alt text](assets/157.png) ![alt text](assets/158.png) ![alt text](assets/159.png) ![alt text](assets/160.png) ![alt text](assets/161.png) ![alt text](assets/162.png) ![alt text](assets/163.png) ![alt text](assets/164.png) ![alt text](assets/165.png) ![alt text](assets/166.png) ![alt text](assets/167.png) ![alt text](assets/168.png) ![alt text](assets/169.png) ![alt text](assets/170.png) ![alt text](assets/171.png) ![alt text](assets/172.png) ![alt text](assets/173.png) ![alt text](assets/174.png) ![alt text](assets/175.png) ![alt text](assets/176.png) ![alt text](assets/177.png) ![alt text](assets/178.png) ![alt text](assets/179.png) ![alt text](assets/180.png) ![alt text](assets/181.png) ![alt text](assets/182.png) ![alt text](assets/183.png) ![alt text](assets/184.png) ![alt text](assets/185.png) ![alt text](assets/186.png) ![alt text](assets/187.png) ![alt text](assets/188.png) ![alt text](assets/189.png) ![alt text](assets/190.png) ![alt text](assets/191.png) ![alt text](assets/192.png) ![alt text](assets/193.png) ![alt text](assets/194.png) ![alt text](assets/195.png) ![alt text](assets/196.png) ![alt text](assets/197.png) ![alt text](assets/198.png) ![alt text](assets/199.png) ![alt text](assets/200.png) ![alt text](assets/201.png) ![alt text](assets/202.png) ![alt text](assets/203.png) ![alt text](assets/204.png) ![alt text](assets/205.png) ![alt text](assets/206.png) ![alt text](assets/207.png) ![alt text](assets/208.png) ![alt text](assets/209.png) ![alt text](assets/210.png) ![alt text](assets/211.png) ![alt text](assets/212.png) ![alt text](assets/213.png) ![alt text](assets/214.png) ![alt text](assets/215.png) ![alt text](assets/216.png) ![alt text](assets/217.png) ![alt text](assets/218.png) ![alt text](assets/219.png) ![alt text](assets/220.png) ![alt text](assets/221.png) ![alt text](assets/222.png) ![alt text](assets/223.png) ![alt text](assets/224.png) ![alt text](assets/225.png) ![alt text](assets/226.png) ![alt text](assets/227.png) ![alt text](assets/228.png) ![alt text](assets/229.png) ![alt text](assets/230.png) ![alt text](assets/231.png) ![alt text](assets/232.png) ![alt text](assets/233.png) ![alt text](assets/234.png) ![alt text](assets/235.png) ![alt text](assets/236.png) ![alt text](assets/237.png) ![alt text](assets/238.png) ![alt text](assets/239.png) ![alt text](assets/240.png) ![alt text](assets/241.png) ![alt text](assets/242.png) ![alt text](assets/243.png) ![alt text](assets/244.png) ![alt text](assets/245.png) ![alt text](assets/246.png) ![alt text](assets/247.png) ![alt text](assets/248.png) ![alt text](assets/249.png) ![alt text](assets/250.png) ![alt text](assets/251.png) ![alt text](assets/252.png) ![alt text](assets/253.png) ![alt text](assets/254.png) ![alt text](assets/255.png) ![alt text](assets/256.png) ![alt text](assets/257.png) ![alt text](assets/258.png) ![alt text](assets/259.png) ![alt text](assets/260.png) ![alt text](assets/261.png) ![alt text](assets/262.png) ![alt text](assets/263.png) ![alt text](assets/264.png) ![alt text](assets/265.png) ![alt text](assets/266.png) ![alt text](assets/267.png) ![alt text](assets/268.png) ![alt text](assets/269.png) ![alt text](assets/270.png) ![alt text](assets/271.png) ![alt text](assets/272.png) ![alt text](assets/273.png) ![alt text](assets/274.png) ![alt text](assets/275.png) ![alt text](assets/276.png) ![alt text](assets/277.png) ![alt text](assets/278.png) ![alt text](assets/279.png) ![alt text](assets/280.png) ![alt text](assets/281.png) ![alt text](assets/282.png) ![alt text](assets/283.png)

</details>

### Implementation

- Section 3 tasks:-

1. Clone custom inverter standard cell design from github repository: [Standard cell design and characterization using OpenLANE flow](https://github.com/nickson-jose/vsdstdcelldesign).
2. Load the custom inverter layout in magic and explore.
3. Spice extraction of inverter in magic.
4. Editing the spice model file for analysis through simulation.
5. Post-layout ngspice simulations.
6. Find problem in the DRC section of the old magic tech file for the skywater process and fix them.

#### 1. Clone custom inverter standard cell design from github repository

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Clone the repository with custom inverter design
git clone https://github.com/nickson-jose/vsdstdcelldesign

# Change into repository directory
cd vsdstdcelldesign

# Copy magic tech file to the repo directory for easy access
cp /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech .

# Check contents whether everything is present
ls

# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_inv.mag &
```

Screenshot of commands run
![alt text](assets/360.png)

#### 2. Load the custom inverter layout in magic and explore

Screenshot of custom inverter layout in magic
![alt text](assets/361.png)

NMOS and PMOS identified
![alt text](assets/364.png)
![alt text](assets/365.png)

Output Y connectivity to PMOS and NMOS drain verified
![alt text](assets/369.png)

PMOS source connectivity to VDD (here VPWR) verified
![alt text](assets/371.png)

NMOS source connectivity to VSS (here VGND) verified
![alt text](assets/370.png)

Deleting necessary layout part to see DRC error
![alt text](assets/372.png)

#### 3. Spice extraction of inverter in magic

Commands for spice extraction of the custom inverter layout to be used in tkcon window of magic

```tcl
# Check current directory
pwd

# Extraction command to extract to .ext format
extract all

# Before converting ext to spice this command enable the parasitic extraction also
ext2spice cthresh 0 rthresh 0

# Converting to ext to spice
ext2spice
```

Screenshot of tkcon window after running above commands
![alt text](assets/373.png)

Screenshot of created spice file
![alt text](assets/375.png)

#### 4. Editing the spice model file for analysis through simulation

Measuring unit distance in layout grid
![alt text](assets/374.png)

Final edited spice file ready for ngspice simulation
![alt text](assets/376.png)

#### 5. Post-layout ngspice simulations

Commands for ngspice simulation

```bash
# Command to directly load spice file for simulation to ngspice
ngspice sky130_inv.spice

# Now that we have entered ngspice with the simulation spice file loaded we just have to load the plot
plot y vs time a
```

Screenshots of ngspice run
![alt text](assets/377.png)

Screenshot of generated plot
![alt text](assets/378.png)

Rise transition time calculation

```math
Rise\ transition\ time = Time\ taken\ for\ output\ to\ rise\ to\ 80\% - Time\ taken\ for\ output\ to\ rise\ to\ 20\%
```

```math
20\%\ of\ output = 660\ mV
```

```math
80\%\ of\ output = 2.64\ V
```

20% Screenshots
![alt text](assets/379.png)
![alt text](assets/380.png)
![alt text](assets/381.png)

80% Screenshots
![alt text](assets/382.png)
![alt text](assets/383.png)

```math
Rise\ transition\ time = 2.24638 - 2.18242 = 0.06396\ ns = 63.96\ ps
```

Fall transition time calculation

```math
Fall\ transition\ time = Time\ taken\ for\ output\ to\ fall\ to\ 20\% - Time\ taken\ for\ output\ to\ fall\ to\ 80\%
```

```math
20\%\ of\ output = 660\ mV
```

```math
80\%\ of\ output = 2.64\ V
```

20% Screenshots

![alt text](<assets/Screenshot from 2025-11-12 02-42-12.png>)

80% Screenshots

![alt text](<assets/Screenshot from 2025-11-12 02-41-48.png>)
![alt text](<assets/Screenshot from 2025-11-12 02-42-26.png>)

```math
Fall\ transition\ time = 4.0957 - 4.0207 = 0.075\ ns = 75\ ps
```

Rise Cell Delay Calculation

```math
Rise\ Cell\ Delay = Time\ taken\ for\ output\ to\ rise\ to\ 50\% - Time\ taken\ for\ input\ to\ fall\ to\ 50\%
```

```math
50\%\ of\ 3.3\ V = 1.65\ V
```

50% Screenshots
![alt text](assets/392.png)

```math
Rise\ Cell\ Delay = 2.21157 - 2.15005 = 0.06152\ ns = 61.52\ ps
```

Fall Cell Delay Calculation

```math
Fall\ Cell\ Delay = Time\ taken\ for\ output\ to\ fall\ to\ 50\% - Time\ taken\ for\ input\ to\ rise\ to\ 50\%
```

```math
50\%\ of\ 3.3\ V = 1.65\ V
```

50% Screenshots
![alt text](assets/393.png)

```math
Fall\ Cell\ Delay = 4.07 - 4.05 = 0.02\ ns = 20\ ps
```

#### 6. Find problem in the DRC section of the old magic tech file for the skywater process and fix them

Link to Sky130 Periphery rules: [https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html](https://skywater-pdk.readthedocs.io/en/main/rules/periphery.html)

Commands to download and view the corrupted skywater process magic tech file and associated files to perform drc corrections

```bash
# Change to home directory
cd

# Command to download the lab files
wget http://opencircuitdesign.com/open_pdks/archive/drc_tests.tgz

# Since lab file is compressed command to extract it
tar xfz drc_tests.tgz

# Change directory into the lab folder
cd drc_tests

# List all files and directories present in the current directory
ls -al

# Command to view .magicrc file
gvim .magicrc

# Command to open magic tool in better graphics
magic -d XR &
```

Screenshots of commands run
![alt text](assets/396.png)
![alt text](assets/398.png)

Screenshot of .magicrc file
![alt text](assets/397.png)

- **Incorrectly implemented poly.9 simple rule correction**

Screenshot of poly rules
![alt text](assets/image-1.png)
![alt text](assets/403.png)
![alt text](assets/404.png)
![alt text](assets/405.png)
![alt text](assets/406.png)
![alt text](assets/407.png) ![alt text](assets/408.png) ![alt text](assets/409.png) ![alt text](assets/410.png) ![alt text](assets/411.png) ![alt text](assets/412.png) ![alt text](assets/413.png) ![alt text](assets/414.png) ![alt text](assets/415.png) ![alt text](assets/416.png)

Incorrectly implemented poly.9 rule no drc violation even though spacing < 0.48u
![alt text](assets/399.png)
![alt text](assets/400.png)
![alt text](assets/401.png)
![alt text](assets/402.png)
![alt text](assets/430.png)
![alt text](assets/431.png)

New commands inserted in sky130A.tech file to update drc
![alt text](assets/425.png)
![alt text](assets/426.png)
![alt text](assets/427.png)
![alt text](assets/428.png)

Commands to run in tkcon window

```tcl
# Loading updated tech file
tech load sky130A.tech

# Must re-run drc check to see updated drc errors
drc check

# Selecting region displaying the new errors and getting the error messages 
drc why
```

Screenshot of magic window with rule implemented
![alt text](assets/429.png)
![alt text](assets/430.png)
![alt text](assets/431.png)
![alt text](assets/432.png)

- **Incorrectly implemented nwell.4 complex rule correction**

Screenshot of nwell rules
![alt text](assets/433.png)
![alt text](assets/434.png)
![alt text](assets/435.png)

Incorrectly implemented nwell.4 rule no drc violation even though no tap present in nwell
![alt text](assets/436.png)
![alt text](assets/437.png)
![alt text](assets/438.png)

New commands inserted in sky130A.tech file to update drc
![alt text](assets/439.png)
![alt text](assets/440.png)
![alt text](assets/441.png)
![alt text](assets/442.png)
![alt text](assets/443.png)
![alt text](assets/444.png)
![alt text](assets/445.png)
![alt text](assets/446.png)
![alt text](assets/447.png)

Commands to run in tkcon window

```tcl
# Loading updated tech file
tech load sky130A.tech

# Change drc style to drc full
drc style drc(full)

# Must re-run drc check to see updated drc errors
drc check

# Selecting region displaying the new errors and getting the error messages 
drc why
```

Screenshot of magic window with rule implemented
![alt text](assets/445.png)
![alt text](assets/446.png)
![alt text](assets/447.png)

## 4. Pre-layout timing analysis and importance of good clock tree

### Theory

<details>
<summary>Click to expand</summary>

![alt text](assets/284.png) ![alt text](assets/285.png) ![alt text](assets/286.png) ![alt text](assets/287.png) ![alt text](assets/288.png) ![alt text](assets/289.png) ![alt text](assets/290.png) ![alt text](assets/291.png) ![alt text](assets/292.png) ![alt text](assets/293.png) ![alt text](assets/294.png) ![alt text](assets/295.png) ![alt text](assets/296.png) ![alt text](assets/297.png) ![alt text](assets/298.png) ![alt text](assets/299.png) ![alt text](assets/300.png) ![alt text](assets/301.png) ![alt text](assets/302.png) ![alt text](assets/303.png) ![alt text](assets/304.png) ![alt text](assets/305.png) ![alt text](assets/306.png) ![alt text](assets/307.png) ![alt text](assets/308.png) ![alt text](assets/309.png) ![alt text](assets/310.png) ![alt text](assets/311.png) ![alt text](assets/312.png) ![alt text](assets/313.png) ![alt text](assets/314.png) ![alt text](assets/315.png)

</details>

### Implementation

- Section 4 tasks:-

1. Fix up small DRC errors and verify the design is ready to be inserted into our flow.
2. Save the finalized layout with custom name and open it.
3. Generate lef from the layout.
4. Copy the newly generated lef and associated required lib files to 'picorv32a' design 'src' directory.
5. Edit 'config.tcl' to change lib file and add the new extra lef into the openlane flow.
6. Run openlane flow synthesis with newly inserted custom inverter cell.
7. Remove/reduce the newly introduced violations with the introduction of custom inverter cell by modifying design parameters.
8. Once synthesis has accepted our custom inverter we can now run floorplan and placement and verify the cell is accepted in PnR flow.
9. Do Post-Synthesis timing analysis with OpenSTA tool.
10. Make timing ECO fixes to remove all violations.
11. Replace the old netlist with the new netlist generated after timing ECO fix and implement the floorplan, placement and cts.
12. Post-CTS OpenROAD timing analysis.
13. Explore post-CTS OpenROAD timing analysis by removing 'sky130_fd_sc_hd__clkbuf_1' cell from clock buffer list variable 'CTS_CLK_BUFFER_LIST'.

- Section 4 - reports and logs can be found in the following folder:

[Section 4 - \(vsdstdcelldesign\)](openlane_working_dir/openlane/vsdstdcelldesign)

- Section 4 - reports and logs can be found in the following folder:

[Section 4 - (src\)](openlane_working_dir/openlane/designs/picorv32a/src)

- Section 4 - Task 5 files, reports and logs can be found in the following folder:

[Section 4 - \(picorv32a\)](openlane_working_dir/openlane/designs/picorv32a)

- Section 4 - logs, reports and results can be found in following run folder:

[Section 4 - \(11-11_13-20)](openlane_working_dir/openlane/designs/picorv32a/runs/11-11_13-20)

- Section 4 - Tasks 9 to 11 logs, reports and results can be found in following run folder:

[Section 4 - \(11-11_14-29)](openlane_working_dir/openlane/designs/picorv32a/runs/11-11_14-29)

#### 1. Fix up small DRC errors and verify the design is ready to be inserted into our flow

Conditions to be verified before moving forward with custom designed cell layout:

- Condition 1: The input and output ports of the standard cell should lie on the intersection of the vertical and horizontal tracks.
- Condition 2: Width of the standard cell should be odd multiples of the horizontal track pitch.
- Condition 3: Height of the standard cell should be even multiples of the vertical track pitch.

Commands to open the custom inverter layout

```bash
# Change directory to vsdstdcelldesign
cd Desktop/work/tools/openlane_working_dir/openlane/vsdstdcelldesign

# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_inv.mag &
```

Screenshot of tracks.info of sky130_fd_sc_hd
![alt text](assets/448.png)

Commands for tkcon window to set grid as tracks of locali layer

```tcl
# Get syntax for grid command
help grid

# Set grid values accordingly
grid 0.46um 0.34um 0.23um 0.17um
```

Screenshot of commands run
![alt text](assets/449.png)

Condition 1 verified
![alt text](assets/450.png)

Condition 2 verified
![alt text](assets/451.png)

```math
Horizontal\ track\ pitch = 0.46\ um
```

```math
Width\ of\ standard\ cell = 1.38\ um = 0.46 * 3
```

Condition 3 verified

```math
Vertical\ track\ pitch = 0.34\ um
```

![alt text](assets/452.png)

```math
Height\ of\ standard\ cell = 2.72\ um = 0.34 * 8
```

#### 2. Save the finalized layout with custom name and open it

Command for tkcon window to save the layout with custom name

```tcl
# Command to save as
save sky130_vsdinv.mag
```

Command to open the newly saved layout

```bash
# Command to open custom inverter layout in magic
magic -T sky130A.tech sky130_vsdinv.mag &
```

Screenshot of newly saved layout
![alt text](assets/453.png)
![alt text](assets/454.png)
![alt text](assets/455.png)

#### 3. Generate lef from the layout

Command for tkcon window to write lef

```tcl
# lef command
lef write
```

Screenshot of command run
![alt text](assets/458.png)
![alt text](assets/459.png)

Screenshot of newly created lef file
![alt text](assets/460.png)
![alt text](assets/461.png)
![alt text](assets/462.png)
![alt text](assets/463.png)

#### 4. Copy the newly generated lef and associated required lib files to 'picorv32a' design 'src' directory

Commands to copy necessary files to 'picorv32a' design 'src' directory

```bash
# Copy lef file
cp sky130_vsdinv.lef ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# List and check whether it's copied
ls ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# Copy lib files
cp libs/sky130_fd_sc_hd__* ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/

# List and check whether it's copied
ls ~/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/src/
```

Screenshot of commands run
![alt text](assets/464.png)

#### 5. Edit 'config.tcl' to change lib file and add the new extra lef into the openlane flow

Commands to be added to config.tcl to include our custom cell in the openlane flow

```tcl
set ::env(LIB_SYNTH) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__typical.lib"
set ::env(LIB_FASTEST) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__fast.lib"
set ::env(LIB_SLOWEST) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__slow.lib"
set ::env(LIB_TYPICAL) "$::env(OPENLANE_ROOT)/designs/picorv32a/src/sky130_fd_sc_hd__typical.lib"

set ::env(EXTRA_LEFS) [glob $::env(OPENLANE_ROOT)/designs/$::env(DESIGN_NAME)/src/*.lef]
```

Edited config.tcl to include the added lef and change library to ones we added in src directory
![alt text](assets/465.png)

#### 6. Run openlane flow synthesis with newly inserted custom inverter cell

- Commands to invoke the OpenLANE flow include new lef and perform synthesis

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```

```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Adiitional commands to include newly added lef to openlane flow
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Screenshots of commands run
![alt text](assets/466.png)
![alt text](assets/466.png)
![alt text](assets/468.png)
![alt text](assets/469.png)
![alt text](assets/470.png)
![alt text](assets/471.png)

#### 7. Remove/reduce the newly introduced violations with the introduction of custom inverter cell by modifying design parameters

Noting down current design values generated before modifying parameters to improve timing
![alt text](assets/472.png)
![alt text](assets/473.png)
![alt text](assets/474.png)
![alt text](assets/475.png)

Commands to view and change parameters to improve timing and run synthesis

```tcl
# Now once again we have to prep design so as to update variables
prep -design picorv32a -tag 24-03_10-03 -overwrite

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to display current value of variable SYNTH_STRATEGY
echo $::env(SYNTH_STRATEGY)

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to display current value of variable SYNTH_BUFFERING to check whether it's enabled
echo $::env(SYNTH_BUFFERING)

# Command to display current value of variable SYNTH_SIZING
echo $::env(SYNTH_SIZING)

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Command to display current value of variable SYNTH_DRIVING_CELL to check whether it's the proper cell or not
echo $::env(SYNTH_DRIVING_CELL)

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Screenshot of merged.lef in `tmp` directory with our custom inverter as macro

![alt text](assets/477.png)

Screenshots of commands run
![alt text](assets/482.png)
![alt text](assets/483.png)
![alt text](assets/484.png)
![alt text](assets/485.png)

Comparing to previously noted run values area has increased and worst negative slack has become 0
![alt text](assets/475.png)
![alt text](assets/476.png)

#### 8. Once synthesis has accepted our custom inverter we can now run floorplan and placement and verify the cell is accepted in PnR flow

Now that our custom inverter is properly accepted in synthesis we can now run floorplan using following command

```tcl
# Now we can run floorplan
run_floorplan
```

Screenshots of command run
![alt text](assets/478.png)
![alt text](assets/479.png)

Since we are facing unexpected un-explainable error while using `run_floorplan` command, we can instead use the following set of commands available based on information from `Desktop/work/tools/openlane_working_dir/openlane/scripts/tcl_commands/floorplan.tcl` and also based on `Floorplan Commands` section in `Desktop/work/tools/openlane_working_dir/openlane/docs/source/OpenLANE_commands.md`

```tcl
# Follwing commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or
```

Screenshots of commands run
![alt text](assets/480.png)
![alt text](assets/481.png)
![alt text](assets/482.png)
![alt text](assets/483.png)

Now that floorplan is done we can do placement using following command

```tcl
# Now we are ready to run placement
run_placement
```

Screenshots of command run
![alt text](assets/484.png)
![alt text](assets/485.png)
![alt text](assets/486.png)

Commands to load placement def in magic in another terminal

```bash
# Change directory to path containing generated placement def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/11-11_/results/placement/

# Command to load the placement def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.placement.def &
```

Screenshot of placement def in magic
![alt text](assets/487.png)
![alt text](assets/488.png)

Screenshot of custom inverter inserted in placement def with proper abutment
![alt text](assets/489.png)

Command for tkcon window to view internal layers of cells

```tcl
# Command to view internal connectivity layers
expand
```

Abutment of power pins with other cell from library clearly visible
![alt text](assets/490.png)
![alt text](assets/491.png)
![alt text](assets/492.png)

#### 9. Do Post-Synthesis timing analysis with OpenSTA tool

Since we are having 0 wns after improved timing run we are going to do timing analysis on initial run of synthesis which has lots of violations and no parameters were added to improve timing

Commands to invoke the OpenLANE flow include new lef and perform synthesis:

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```

```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Adiitional commands to include newly added lef to openlane flow
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Commands run final screenshot
![alt text](assets/493.png)
![alt text](assets/494.png)
![alt text](assets/495.png)

Newly created `pre_sta.conf` for STA analysis in `openlane` directory
![alt text](assets/496.png)

Newly created `my_base.sdc` for STA analysis in `openlane/designs/picorv32a/src` directory based on the file `openlane/scripts/base.sdc`
![alt text](assets/497.png)

- Commands to run STA in another terminal

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Command to invoke OpenSTA tool with script
sta pre_sta.conf
```

Screenshots of commands run
![alt text](assets/498.png)
![alt text](assets/499.png)

Since more fanout is causing more delay we can add parameter to reduce fanout and do synthesis again

- Commands to include new lef and perform synthesis:

```tcl
# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a -tag 25-03_18-52 -overwrite

# Adiitional commands to include newly added lef to openlane flow
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Command to set new value for SYNTH_MAX_FANOUT
set ::env(SYNTH_MAX_FANOUT) 4

# Command to display current value of variable SYNTH_DRIVING_CELL to check whether it's the proper cell or not
echo $::env(SYNTH_DRIVING_CELL)

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis
```

Commands to run STA in another terminal

```bash
# Change directory to openlane
cd Desktop/work/tools/openlane_working_dir/openlane

# Command to invoke OpenSTA tool with script
sta pre_sta.conf
```

Screenshots of commands run
![alt text](assets/500.png)
![alt text](assets/501.png)
![alt text](assets/502.png)

#### 10. Make timing ECO fixes to remove all violations

OR gate of drive strength 2 is driving 4 fanouts
![alt text](assets/503.png)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11672_

# Checking command syntax
help replace_cell

# Replacing cell
replace_cell _14510_ sky130_fd_sc_hd__or3_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced
![alt text](assets/504.png)
![alt text](assets/505.png)
![alt text](assets/506.png)

OR gate of drive strength 2 is driving 4 fanouts
![alt text](assets/507.png)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11675_

# Replacing cell
replace_cell _14514_ sky130_fd_sc_hd__or3_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced
![alt text](assets/508.png)
![alt text](assets/509.png)
![alt text](assets/510.png)

OR gate of drive strength 2 driving OA gate has more delay
![alt text](assets/511.png)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11643_

# Replacing cell
replace_cell _14481_ sky130_fd_sc_hd__or4_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced
![alt text](assets/512.png)
![alt text](assets/513.png)

OR gate of drive strength 2 driving OA gate has more delay
![alt text](assets/514.png)

Commands to perform analysis and optimize timing by replacing with OR gate of drive strength 4

```tcl
# Reports all the connections to a net
report_net -connections _11668_

# Replacing cell
replace_cell _14506_ sky130_fd_sc_hd__or4_4

# Generating custom timing report
report_checks -fields {net cap slew input_pins} -digits 4
```

Result - slack reduced
![alt text](assets/515.png)
![alt text](assets/516.png)

Commands to verify instance `_14506_`  is replaced with `sky130_fd_sc_hd__or4_4`

```tcl
# Generating custom timing report
report_checks -from _29043_ -to _30440_ -through _14506_
```

Screenshot of replaced instance
![alt text](assets/517.png)

- **We started ECO fixes at wns -23.9000 and now we stand at wns -22.6173 we reduced around 1.2827 ns of violation**

#### 11. Replace the old netlist with the new netlist generated after timing ECO fix and implement the floorplan, placement and cts

Now to insert this updated netlist to PnR flow and we can use `write_verilog` and overwrite the synthesis netlist but before that we are going to make a copy of the old old netlist

Commands to make copy of netlist

```bash
# Change from home directory to synthesis results directory
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/11-11_14-29/results/synthesis/

# List contents of the directory
ls

# Copy and rename the netlist
cp picorv32a.synthesis.v picorv32a.synthesis_old.v

# List contents of the directory
ls
```

Screenshot of commands run
![alt text](assets/518.png)

Commands to write verilog

```tcl
# Check syntax
help write_verilog

# Overwriting current synthesis netlist
write_verilog /home/vsduser/Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/25-03_18-52/results/synthesis/picorv32a.synthesis.v

# Exit from OpenSTA since timing analysis is done
exit
```

Screenshot of commands run
![alt text](assets/519.png)

Verified that the netlist is overwritten by checking that instance `_14506_`  is replaced with `sky130_fd_sc_hd__or4_4`
![alt text](assets/520.png)

Since we confirmed that netlist is replaced and will be loaded in PnR but since we want to follow up on the earlier 0 violation design we are continuing with the clean design to further stages

- Commands load the design and run necessary stages

```tcl
# Now once again we have to prep design so as to update variables
prep -design picorv32a -tag 24-03_10-03 -overwrite

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Follwing commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or

# Now we are ready to run placement
run_placement

# Incase getting error
unset ::env(LIB_CTS)

# With placement done we are now ready to run CTS
run_cts
```

Screenshots of commands run
![alt text](assets/521.png)
![alt text](assets/522.png)
![alt text](assets/523.png)
![alt text](assets/524.png)
![alt text](assets/525.png)
![alt text](assets/526.png)
![alt text](assets/527.png)
![alt text](assets/528.png)
![alt text](assets/529.png)
![alt text](assets/530.png)

#### 12. Post-CTS OpenROAD timing analysis

- Commands to be run in OpenLANE flow to do OpenROAD timing analysis with integrated OpenSTA in OpenROAD

```tcl
# Command to run OpenROAD tool
openroad

# Reading lef file
read_lef /openLANE_flow/designs/picorv32a/runs/24-03_10-03/tmp/merged.lef

# Reading def file
read_def /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/cts/picorv32a.cts.def

# Creating an OpenROAD database to work with
write_db pico_cts.db

# Loading the created database in OpenROAD
read_db pico_cts.db

# Read netlist post CTS
read_verilog /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/synthesis/picorv32a.synthesis_cts.v

# Read library for design
read_liberty $::env(LIB_SYNTH_COMPLETE)

# Link design and library
link_design picorv32a

# Read in the custom sdc we created
read_sdc /openLANE_flow/designs/picorv32a/src/my_base.sdc

# Setting all cloks as propagated clocks
set_propagated_clock [all_clocks]

# Check syntax of 'report_checks' command
help report_checks

# Generating custom timing report
report_checks -path_delay min_max -fields {slew trans net cap input_pins} -format full_clock_expanded -digits 4

# Exit to OpenLANE flow
exit
```

Screenshots of commands run and timing report generated
![alt text](assets/531.png)
![alt text](assets/532.png)
![alt text](assets/533.png)
![alt text](assets/534.png)
![alt text](assets/535.png)
![alt text](assets/536.png)

#### 13. Explore post-CTS OpenROAD timing analysis by removing 'sky130_fd_sc_hd__clkbuf_1' cell from clock buffer list variable 'CTS_CLK_BUFFER_LIST'

- Commands to be run in OpenLANE flow to do OpenROAD timing analysis after changing `CTS_CLK_BUFFER_LIST`

```tcl
# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Removing 'sky130_fd_sc_hd__clkbuf_1' from the list
set ::env(CTS_CLK_BUFFER_LIST) [lreplace $::env(CTS_CLK_BUFFER_LIST) 0 0]

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Checking current value of 'CURRENT_DEF'
echo $::env(CURRENT_DEF)

# Setting def as placement def
set ::env(CURRENT_DEF) /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/placement/picorv32a.placement.def

# Run CTS again
run_cts

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Command to run OpenROAD tool
openroad

# Reading lef file
read_lef /openLANE_flow/designs/picorv32a/runs/24-03_10-03/tmp/merged.lef

# Reading def file
read_def /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/cts/picorv32a.cts.def

# Creating an OpenROAD database to work with
write_db pico_cts1.db

# Loading the created database in OpenROAD
read_db pico_cts.db

# Read netlist post CTS
read_verilog /openLANE_flow/designs/picorv32a/runs/24-03_10-03/results/synthesis/picorv32a.synthesis_cts.v

# Read library for design
read_liberty $::env(LIB_SYNTH_COMPLETE)

# Link design and library
link_design picorv32a

# Read in the custom sdc we created
read_sdc /openLANE_flow/designs/picorv32a/src/my_base.sdc

# Setting all cloks as propagated clocks
set_propagated_clock [all_clocks]

# Generating custom timing report
report_checks -path_delay min_max -fields {slew trans net cap input_pins} -format full_clock_expanded -digits 4

# Report hold skew
report_clock_skew -hold

# Report setup skew
report_clock_skew -setup

# Exit to OpenLANE flow
exit

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)

# Inserting 'sky130_fd_sc_hd__clkbuf_1' to first index of list
set ::env(CTS_CLK_BUFFER_LIST) [linsert $::env(CTS_CLK_BUFFER_LIST) 0 sky130_fd_sc_hd__clkbuf_1]

# Checking current value of 'CTS_CLK_BUFFER_LIST'
echo $::env(CTS_CLK_BUFFER_LIST)
```

Screenshots of commands run and timing report generated
![alt text](assets/537.png)
![alt text](assets/538.png)
![alt text](assets/539.png)
![alt text](assets/540.png)
![alt text](assets/541.png)
![alt text](assets/542.png)
![alt text](assets/543.png)
![alt text](assets/544.png)

## 5. Final steps for RTL2GDS using tritonRoute and openSTA

### Theory

<details>
<summary>Click to expand</summary>

![alt text](assets/316.png) ![alt text](assets/317.png) ![alt text](assets/318.png) ![alt text](assets/319.png) ![alt text](assets/320.png) ![alt text](assets/321.png) ![alt text](assets/322.png) ![alt text](assets/323.png) ![alt text](assets/324.png) ![alt text](assets/325.png) ![alt text](assets/326.png) ![alt text](assets/327.png) ![alt text](assets/328.png) ![alt text](assets/329.png) ![alt text](assets/330.png) ![alt text](assets/331.png) ![alt text](assets/332.png)

</details>

### Implementation

- Section 5 tasks:-

1. Perform generation of Power Distribution Network (PDN) and explore the PDN layout.
2. Perfrom detailed routing using TritonRoute.
3. Post-Route parasitic extraction using SPEF extractor.
4. Post-Route OpenSTA timing analysis with the extracted parasitics of the route.

- All section 5 logs, reports and results can be found in following run folder:

#### 1. Perform generation of Power Distribution Network (PDN) and explore the PDN layout

Commands to perform all necessary stages up until now

```bash
# Change directory to openlane flow directory
cd Desktop/work/tools/openlane_working_dir/openlane

# alias docker='docker run -it -v $(pwd):/openLANE_flow -v $PDK_ROOT:$PDK_ROOT -e PDK_ROOT=$PDK_ROOT -u $(id -u $USER):$(id -g $USER) efabless/openlane:v0.21'
# Since we have aliased the long command to 'docker' we can invoke the OpenLANE flow docker sub-system by just running this command
docker
```

```tcl
# Now that we have entered the OpenLANE flow contained docker sub-system we can invoke the OpenLANE flow in the Interactive mode using the following command
./flow.tcl -interactive

# Now that OpenLANE flow is open we have to input the required packages for proper functionality of the OpenLANE flow
package require openlane 0.9

# Now the OpenLANE flow is ready to run any design and initially we have to prep the design creating some necessary files and directories for running a specific design which in our case is 'picorv32a'
prep -design picorv32a

# Addiitional commands to include newly added lef to openlane flow merged.lef
set lefs [glob $::env(DESIGN_DIR)/src/*.lef]
add_lefs -src $lefs

# Command to set new value for SYNTH_STRATEGY
set ::env(SYNTH_STRATEGY) "DELAY 3"

# Command to set new value for SYNTH_SIZING
set ::env(SYNTH_SIZING) 1

# Now that the design is prepped and ready, we can run synthesis using following command
run_synthesis

# Following commands are alltogather sourced in "run_floorplan" command
init_floorplan
place_io
tap_decap_or

# Now we are ready to run placement
run_placement

# Incase getting error
unset ::env(LIB_CTS)

# With placement done we are now ready to run CTS
run_cts

# Now that CTS is done we can do power distribution network
gen_pdn 
```

Screenshots of power distribution network run
![alt text](assets/545.png)
![alt text](assets/546.png)
![alt text](assets/547.png)

Commands to load PDN def in magic in another terminal

```bash
# Change directory to path containing generated PDN def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/26-03_08-45/tmp/floorplan/

# Command to load the PDN def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read 14-pdn.def &
```

Screenshots of PDN def
![alt text](assets/548.png)
![alt text](assets/549.png)
![alt text](assets/550.png)
![alt text](assets/551.png)

#### 2. Perfrom detailed routing using TritonRoute and explore the routed layout

Command to perform routing

```tcl
# Check value of 'CURRENT_DEF'
echo $::env(CURRENT_DEF)

# Check value of 'ROUTING_STRATEGY'
echo $::env(ROUTING_STRATEGY)

# Command for detailed route using TritonRoute
run_routing
```

Screenshots of routing run
![alt text](assets/552.png)
![alt text](assets/553.png)
![alt text](assets/554.png)
![alt text](assets/555.png)
![alt text](assets/556.png)
![alt text](assets/557.png)
![alt text](assets/558.png)
![alt text](assets/559.png)
![alt text](assets/560.png)
![alt text](assets/561.png)

Commands to load routed def in magic in another terminal

```bash
# Change directory to path containing routed def
cd Desktop/work/tools/openlane_working_dir/openlane/designs/picorv32a/runs/26-03_08-45/results/routing/

# Command to load the routed def in magic tool
magic -T /home/vsduser/Desktop/work/tools/openlane_working_dir/pdks/sky130A/libs.tech/magic/sky130A.tech lef read ../../tmp/merged.lef def read picorv32a.def &
```

Screenshots of routed def
![alt text](assets/562.png)
![alt text](assets/563.png)
![alt text](assets/564.png)
![alt text](assets/565.png)
![alt text](assets/566.png)
![alt text](assets/567.png)
![alt text](assets/568.png)

Screenshot of fast route guide present in `openlane/designs/picorv32a/runs/11-11_15_47/tmp/routing` directory
![alt text](assets/569.png)

#### 3. Post-Route OpenSTA timing analysis with the extracted parasitics of the route

Commands to be run in OpenLANE flow to do OpenROAD timing analysis with integrated OpenSTA in OpenROAD

```tcl
# Command to run OpenROAD tool
openroad

# Reading lef file
read_lef /openLANE_flow/designs/picorv32a/runs/26-03_08-45/tmp/merged.lef

# Reading def file
read_def /openLANE_flow/designs/picorv32a/runs/26-03_08-45/results/routing/picorv32a.def

# Creating an OpenROAD database to work with
write_db pico_route.db

# Loading the created database in OpenROAD
read_db pico_route.db

# Read netlist post CTS
read_verilog /openLANE_flow/designs/picorv32a/runs/26-03_08-45/results/synthesis/picorv32a.synthesis_preroute.v

# Read library for design
read_liberty $::env(LIB_SYNTH_COMPLETE)

# Link design and library
link_design picorv32a

# Read in the custom sdc we created
read_sdc /openLANE_flow/designs/picorv32a/src/my_base.sdc

# Setting all cloks as propagated clocks
set_propagated_clock [all_clocks]

# Read SPEF
read_spef /openLANE_flow/designs/picorv32a/runs/26-03_08-45/results/routing/picorv32a.spef

# Generating custom timing report
report_checks -path_delay min_max -fields {slew trans net cap input_pins} -format full_clock_expanded -digits 4

# Exit to OpenLANE flow
exit
```

Screenshots of commands run and timing report generated
![alt text](assets/570.png)
![alt text](assets/571.png)
![alt text](assets/572.png)

## Acknowledgements

- [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
- [Nickson P Jose](https://github.com/nickson-jose), Physical Design Engineer, Intel Corporation.
- [R. Timothy Edwards](https://github.com/RTimothyEdwards), Senior Vice President of Analog and Design, efabless Corporation.
- [Fayiz Ferosh](https://github.com/fayizferosh/soc-design-and-planning-nasscom-vsd/blob/main/README.md)
