# Installation Verification Logs

This file contains the logs for the verification of each tool installation.

``` bash

(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenLane$ echo "Shwetank Shekhar WEEK 0 SETUP TEST LOGS"
Shwetank Shekhar WEEK 0 SETUP TEST LOGS
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenLane$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ yosys --version
Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ iverilog -V
Icarus Verilog version 12.0 (stable) ()

Copyright (c) 2000-2021 Stephen Williams (steve@icarus.com)

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Icarus Verilog Preprocessor version 12.0 (stable) ()

Copyright (c) 1999-2021 Stephen Williams (steve@icarus.com)

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

Icarus Verilog Parser/Elaborator version 12.0 (stable) ()

Copyright (c) 1998-2021 Stephen Williams (steve@icarus.com)

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

 FLAGS DLL vvp.tgt
vvp.tgt: Icarus Verilog VVP Code Generator 12.0 (stable) ()

Copyright (c) 2001-2021 Stephen Williams (steve@icarus.com)

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License along
  with this program; if not, write to the Free Software Foundation, Inc.,
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ gtkwave --version
GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ ngspice -v
******
** ngspice-45.2 : Circuit level simulation program
** Compiled with KLU Direct Linear Solver
** The U. C. Berkeley CAD Group
** Copyright 1985-1994, Regents of the University of California.
** Copyright 2001-2025, The ngspice team.
** Please get your ngspice manual from https://ngspice.sourceforge.io/docs.html
** Please file your bug-reports at http://ngspice.sourceforge.net/bugrep.html
** Creation Date: Fri Sep 19 18:26:11 UTC 2025
******
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ magic --version
8.3.552
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd OpenLane
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenLane$ make pdk
./venv/bin/ciel enable --pdk-family sky130A 0fe599b2afb6708d281543108caf8310912f54af
Version 0fe599b2afb6708d281543108caf8310912f54af enabled for the sky130 PDK.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenLane$ make test
cd /home/ank/Desktop/SoC_Shwetank/OpenLane && \
	docker run --rm -v /home/ank/Desktop/SoC_Shwetank/OpenLane:/openlane -v /home/ank/Desktop/SoC_Shwetank/OpenLane/designs:/openlane/install -v /home/ank:/home/ank -v /home/ank/.ciel:/home/ank/.ciel -e PDK_ROOT=/home/ank/.ciel -e PDK=sky130A  --user 1000:1000 -e DISPLAY=:1 -v /tmp/.X11-unix:/tmp/.X11-unix --network host --security-opt seccomp=unconfined -v /home/ank/.Xauthority:/.Xauthority ghcr.io/the-openroad-project/openlane:ff5509f65b17bfa4068d5336495ab1718987ff69-amd64 sh -c "./flow.tcl -design spm -tag openlane_test -overwrite"
OpenLane v1.0.2 (ff5509f65b17bfa4068d5336495ab1718987ff69)
All rights reserved. (c) 2020-2025 Efabless Corporation and contributors.
Available under the Apache License, version 2.0. See the LICENSE file for more details.

[INFO]: Using configuration in 'designs/spm/config.json'...
[INFO]: PDK Root: /home/ank/.ciel
[INFO]: Process Design Kit: sky130A
[INFO]: Standard Cell Library: sky130_fd_sc_hd
[INFO]: Optimization Standard Cell Library: sky130_fd_sc_hd
[INFO]: Run Directory: /openlane/designs/spm/runs/openlane_test
[INFO]: Removing existing /openlane/designs/spm/runs/openlane_test...
[INFO]: Saving runtime environment...
[INFO]: Preparing LEF files for the nom corner...
[INFO]: Preparing LEF files for the min corner...
[INFO]: Preparing LEF files for the max corner...
[INFO]: Running linter (Verilator) (log: designs/spm/runs/openlane_test/logs/synthesis/linter.log)...
[INFO]: 0 errors found by linter
[WARNING]: 1 warnings found by linter
[STEP 1]
[INFO]: Running Synthesis (log: designs/spm/runs/openlane_test/logs/synthesis/1-synthesis.log)...
[STEP 2]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/synthesis/2-sta.log)...
[STEP 3]
[INFO]: Running Initial Floorplanning (log: designs/spm/runs/openlane_test/logs/floorplan/3-initial_fp.log)...
[WARNING]: Current core area is too small for the power grid settings chosen. The power grid will be scaled down.
[INFO]: Floorplanned with width 90.62 and height 89.76.
[STEP 4]
[INFO]: Running IO Placement (log: designs/spm/runs/openlane_test/logs/floorplan/4-place_io.log)...
[STEP 5]
[INFO]: Running Tap/Decap Insertion (log: designs/spm/runs/openlane_test/logs/floorplan/5-tap.log)...
[INFO]: Power planning with power {VPWR} and ground {VGND}...
[STEP 6]
[INFO]: Generating PDN (log: designs/spm/runs/openlane_test/logs/floorplan/6-pdn.log)...
[STEP 7]
[INFO]: Running Global Placement (log: designs/spm/runs/openlane_test/logs/placement/7-global.log)...
[STEP 8]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/placement/8-gpl_sta.log)...
[STEP 9]
[INFO]: Running Placement Resizer Design Optimizations (log: designs/spm/runs/openlane_test/logs/placement/9-resizer.log)...
[STEP 10]
[INFO]: Running Detailed Placement (log: designs/spm/runs/openlane_test/logs/placement/10-detailed.log)...
[STEP 11]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/placement/11-dpl_sta.log)...
[STEP 12]
[INFO]: Running Clock Tree Synthesis (log: designs/spm/runs/openlane_test/logs/cts/12-cts.log)...
[STEP 13]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/cts/13-cts_sta.log)...
[STEP 14]
[INFO]: Running Placement Resizer Timing Optimizations (log: designs/spm/runs/openlane_test/logs/cts/14-resizer.log)...
[STEP 15]
[INFO]: Running Global Routing Resizer Design Optimizations (log: designs/spm/runs/openlane_test/logs/routing/15-resizer_design.log)...
[STEP 16]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/routing/16-rsz_design_sta.log)...
[STEP 17]
[INFO]: Running Global Routing Resizer Timing Optimizations (log: designs/spm/runs/openlane_test/logs/routing/17-resizer_timing.log)...
[STEP 18]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/routing/18-rsz_timing_sta.log)...
[STEP 19]
[INFO]: Running Global Routing (log: designs/spm/runs/openlane_test/logs/routing/19-global.log)...
[INFO]: Starting OpenROAD Antenna Repair Iterations...
[STEP 20]
[INFO]: Writing Verilog (log: designs/spm/runs/openlane_test/logs/routing/19-global_write_netlist.log)...
[STEP 21]
[INFO]: Running Single-Corner Static Timing Analysis (log: designs/spm/runs/openlane_test/logs/routing/21-grt_sta.log)...
[STEP 22]
[INFO]: Running Fill Insertion (log: designs/spm/runs/openlane_test/logs/routing/22-fill.log)...
[STEP 23]
[INFO]: Running Detailed Routing (log: designs/spm/runs/openlane_test/logs/routing/23-detailed.log)...
[INFO]: No DRC violations after detailed routing.
[STEP 24]
[INFO]: Checking Wire Lengths (log: designs/spm/runs/openlane_test/logs/routing/24-wire_lengths.log)...
[STEP 25]
[INFO]: Running SPEF Extraction at the min process corner (log: designs/spm/runs/openlane_test/logs/signoff/25-parasitics_extraction.min.log)...
[STEP 26]
[INFO]: Running Multi-Corner Static Timing Analysis at the min process corner (log: designs/spm/runs/openlane_test/logs/signoff/26-rcx_mcsta.min.log)...
[STEP 27]
[INFO]: Running SPEF Extraction at the max process corner (log: designs/spm/runs/openlane_test/logs/signoff/27-parasitics_extraction.max.log)...
[STEP 28]
[INFO]: Running Multi-Corner Static Timing Analysis at the max process corner (log: designs/spm/runs/openlane_test/logs/signoff/28-rcx_mcsta.max.log)...
[STEP 29]
[INFO]: Running SPEF Extraction at the nom process corner (log: designs/spm/runs/openlane_test/logs/signoff/29-parasitics_extraction.nom.log)...
[STEP 30]
[INFO]: Running Multi-Corner Static Timing Analysis at the nom process corner (log: designs/spm/runs/openlane_test/logs/signoff/30-rcx_mcsta.nom.log)...
[STEP 31]
[INFO]: Running Single-Corner Static Timing Analysis at the nom process corner (log: designs/spm/runs/openlane_test/logs/signoff/31-rcx_sta.log)...
[WARNING]: Module sky130_fd_sc_hd__tapvpwrvgnd_1 blackboxed during sta
[WARNING]: Module sky130_ef_sc_hd__decap_12 blackboxed during sta
[WARNING]: Module sky130_fd_sc_hd__fill_1 blackboxed during sta
[WARNING]: Module sky130_fd_sc_hd__fill_2 blackboxed during sta
[STEP 32]
[INFO]: Creating IR Drop Report (log: designs/spm/runs/openlane_test/logs/signoff/32-irdrop.log)...
[WARNING]: VSRC_LOC_FILES is not defined. The IR drop analysis will run, but the values may be inaccurate.
[STEP 33]
[INFO]: Running Magic to generate various views...
[INFO]: Streaming out GDSII with Magic (log: designs/spm/runs/openlane_test/logs/signoff/33-gdsii.log)...
[INFO]: Generating MAGLEF views...
[INFO]: Generating lef with Magic (/openlane/designs/spm/runs/openlane_test/logs/signoff/33-lef.log)...
[STEP 34]
[INFO]: Streaming out GDSII with KLayout (log: designs/spm/runs/openlane_test/logs/signoff/34-gdsii-klayout.log)...
[STEP 35]
[INFO]: Running XOR on the layouts using KLayout (log: designs/spm/runs/openlane_test/logs/signoff/35-xor.log)...
[INFO]: No XOR differences between KLayout and Magic gds.
[STEP 36]
[INFO]: Running Magic Spice Export from LEF (log: designs/spm/runs/openlane_test/logs/signoff/36-spice.log)...
[STEP 37]
[INFO]: Writing Powered Verilog (logs: designs/spm/runs/openlane_test/logs/signoff/37-write_powered_def.log, designs/spm/runs/openlane_test/logs/signoff/37-write_powered_verilog.log)...
[STEP 38]
[INFO]: Writing Verilog (log: designs/spm/runs/openlane_test/logs/signoff/37-write_powered_verilog.log)...
[STEP 39]
[INFO]: Running LVS (log: designs/spm/runs/openlane_test/logs/signoff/39-lvs.lef.log)...
[STEP 40]
[INFO]: Running Magic DRC (log: designs/spm/runs/openlane_test/logs/signoff/40-drc.log)...
[INFO]: Converting Magic DRC database to various tool-readable formats...
[INFO]: No DRC violations after GDS streaming out.
[STEP 41]
[INFO]: Running OpenROAD Antenna Rule Checker (log: designs/spm/runs/openlane_test/logs/signoff/41-arc.log)...
[STEP 42]
[INFO]: Running Circuit Validity Checker ERC (log: designs/spm/runs/openlane_test/logs/signoff/42-erc_screen.log)...
[INFO]: Saving current set of views in 'designs/spm/runs/openlane_test/results/final'...
[INFO]: Saving runtime environment...
[INFO]: Generating final set of reports...
[INFO]: Created manufacturability report at 'designs/spm/runs/openlane_test/reports/manufacturability.rpt'.
[INFO]: Created metrics report at 'designs/spm/runs/openlane_test/reports/metrics.csv'.
[WARNING]: There are max fanout violations in the design at the typical corner. Please refer to 'designs/spm/runs/openlane_test/reports/signoff/31-rcx_sta.checks.rpt'.
[INFO]: There are no hold violations in the design at the typical corner.
[INFO]: There are no setup violations in the design at the typical corner.
[SUCCESS]: Flow complete.
[INFO]: Note that the following warnings have been generated:
[WARNING]: 1 warnings found by linter
[WARNING]: Current core area is too small for the power grid settings chosen. The power grid will be scaled down.
[WARNING]: Module sky130_fd_sc_hd__tapvpwrvgnd_1 blackboxed during sta
[WARNING]: Module sky130_ef_sc_hd__decap_12 blackboxed during sta
[WARNING]: Module sky130_fd_sc_hd__fill_1 blackboxed during sta
[WARNING]: Module sky130_fd_sc_hd__fill_2 blackboxed during sta
[WARNING]: VSRC_LOC_FILES is not defined. The IR drop analysis will run, but the values may be inaccurate.
[WARNING]: There are max fanout violations in the design at the typical corner. Please refer to 'designs/spm/runs/openlane_test/reports/signoff/31-rcx_sta.checks.rpt'.

Basic test passed
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenLane$ 

```