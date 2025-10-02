ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ cd Desktop
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop$ ls
 ACE_Dereverb_Dataset_1000_unique	   sbd_riscv_tflm_lib_build
 ACE_Dereverb_Dataset_1000_unique.tar.xz   SHELL_SCRIPTING
'ASIC DESIGN'				  'SHELL_SCRIPTING (Copy)'
 CAPSTONE				   SoC_Shwetank
 esc50_classifier.ipynb			   speech-dereverberation-project
 lvlAlpha				   TEST
 LVLALPHA				   test.html
'MONOCULAR SETUP'			   tflm_Archive
 OPTOELECTRONICS			   Verilog_Practice
'Portfolio Website'			   VTVL_SIM_GIT
'REFERNCE RISC'
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop$ cd SoC_Shwetank
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ ls
Documents  ngspice-45.2  soc_env	WEEK_1	yosys
magic	   OpenLane	 verilog_files	WEEK_2
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd WEEK_2
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls
assets	  netlist		     simulation  waveforms
firmware  README.md		     src	 yosys_synthesis_scripts
logs	  README_part_1_refernce.md  testbench
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ mkdir -p babysoc
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls
assets	  logs	     README_part_1_refernce.md	testbench
babysoc   netlist    simulation			waveforms
firmware  README.md  src			yosys_synthesis_scripts
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cd babysanaaaaaaaaaaaaaank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ cd ../../
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ source soc_env/bin/activate
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd WEEK_2/babysoc
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ ls
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ pip3 install pyyaml click sandpiper-saas
Collecting pyyaml
  Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Requirement already satisfied: click in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (8.3.0)
Requirement already satisfied: sandpiper-saas in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (1.1.0)
Requirement already satisfied: Path in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (17.1.1)
Collecting argparse (from sandpiper-saas)
  Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: requests in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (2.32.5)
Requirement already satisfied: charset_normalizer<4,>=2 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2025.8.3)
Downloading pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (807 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 807.9/807.9 kB 3.8 MB/s eta 0:00:00
Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Installing collected packages: argparse, pyyaml
Successfully installed argparse-1.4.0 pyyaml-6.0.3
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ pip3 install pyyaml click sandpiper-saas
Requirement already satisfied: pyyaml in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (6.0.3)
Requirement already satisfied: click in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (8.3.0)
Requirement already satisfied: sandpiper-saas in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (1.1.0)
Requirement already satisfied: Path in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (17.1.1)
Collecting argparse (from sandpiper-saas)
  Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: requests in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (2.32.5)
Requirement already satisfied: charset_normalizer<4,>=2 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2025.8.3)
Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Installing collected packages: argparse
Successfully installed argparse-1.4.0
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ pip3 install pyyaml click sandpiper-saas
Requirement already satisfied: pyyaml in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (6.0.3)
Requirement already satisfied: click in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (8.3.0)
Requirement already satisfied: sandpiper-saas in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (1.1.0)
Requirement already satisfied: Path in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (17.1.1)
Collecting argparse (from sandpiper-saas)
  Using cached argparse-1.4.0-py2.py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: requests in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from sandpiper-saas) (2.32.5)
Requirement already satisfied: charset_normalizer<4,>=2 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /home/ank/Desktop/SoC_Shwetank/soc_env/lib/python3.12/site-packages (from requests->sandpiper-saas) (2025.8.3)
Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Installing collected packages: argparse
Successfully installed argparse-1.4.0
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ which sandpiper-saas
/home/ank/Desktop/SoC_Shwetank/soc_env/bin/sandpiper-saas
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ git clone https://github.com/manili/VSDBabySoC.git
Cloning into 'VSDBabySoC'...
remote: Enumerating objects: 454, done.
remote: Total 454 (delta 0), reused 0 (delta 0), pack-reused 454 (from 1)
Receiving objects: 100% (454/454), 11.21 MiB | 271.00 KiB/s, done.
Resolving deltas: 100% (225/225), done.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ ls
VSDBabySoC
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ cd VSDBabySoC
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ ls -a
.  ..  .git  .gitignore  images  LICENSE  Makefile  README.md  src
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ tree -a
.
├── .git
│   ├── branches
│   ├── config
│   ├── description
│   ├── HEAD
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-merge-commit.sample
│   │   ├── prepare-commit-msg.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── push-to-checkout.sample
│   │   ├── sendemail-validate.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       └── remotes
│   │           └── origin
│   │               └── HEAD
│   ├── objects
│   │   ├── info
│   │   └── pack
│   │       ├── pack-0131ac062d489b7e8a92fecda475c99638c3004b.idx
│   │       ├── pack-0131ac062d489b7e8a92fecda475c99638c3004b.pack
│   │       └── pack-0131ac062d489b7e8a92fecda475c99638c3004b.rev
│   ├── packed-refs
│   └── refs
│       ├── heads
│       │   └── main
│       ├── remotes
│       │   └── origin
│       │       └── HEAD
│       └── tags
├── .gitignore
├── images
│   ├── centralized_avsddac.png
│   ├── inside_dac.png
│   ├── inside_pll.png
│   ├── openlane_flow.png
│   ├── physical_design.png
│   ├── post_routing_sim.png
│   ├── post_synth_sim.png
│   ├── pre_synth_sim.png
│   ├── rvmyth_layout.png
│   ├── selected_dac.png
│   ├── selected_pll.png
│   ├── vsdbabysoc_block_diagram.png
│   └── vsdbabysoc_layout.png
├── LICENSE
├── Makefile
├── README.md
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
    │   ├── avsddac.v
    │   ├── avsdpll.v
    │   ├── clk_gate.v
    │   ├── pseudo_rand_gen.sv
    │   ├── pseudo_rand.sv
    │   ├── rvmyth.tlv
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

31 directories, 77 files
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ sandpiper-saas -i ./src/module/*.tlv -o rvmyth.v --bestsv --noline -p verilog --outdir ./src/module/
You have agreed to our Terms of Service here: https://makerchip.com/terms.
INFORM(0) (PROD_INFO):
	SandPiper(TM) 1.14-2022/10/10-beta-Pro from Redwood EDA, LLC
	(DEV) Run as: "java -jar sandpiper.jar --bestsv --noline -p verilog --outdir=out --nopath -i ./rvmyth.m4out.tlv -o rvmyth.v
	For help, including product info, run with -h.

INFORM(0) (LICENSE):
	Licensed to "Redwood EDA, LLC" as: Full Edition.

INFORM(0) (FILES):
	Reading "./rvmyth.m4out.tlv"
	to produce:
		Translated HDL File: "out/rvmyth.v"
		Generated HDL File: "out/rvmyth_gen.v"

(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ ls
images	LICENSE  Makefile  README.md  src
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ ls
VSDBabySoC
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ tree -a
.
└── VSDBabySoC
    ├── .git
    │   ├── branches
    │   ├── config
    │   ├── description
    │   ├── HEAD
    │   ├── hooks
    │   │   ├── applypatch-msg.sample
    │   │   ├── commit-msg.sample
    │   │   ├── fsmonitor-watchman.sample
    │   │   ├── post-update.sample
    │   │   ├── pre-applypatch.sample
    │   │   ├── pre-commit.sample
    │   │   ├── pre-merge-commit.sample
    │   │   ├── prepare-commit-msg.sample
    │   │   ├── pre-push.sample
    │   │   ├── pre-rebase.sample
    │   │   ├── pre-receive.sample
    │   │   ├── push-to-checkout.sample
    │   │   ├── sendemail-validate.sample
    │   │   └── update.sample
    │   ├── index
    │   ├── info
    │   │   └── exclude
    │   ├── logs
    │   │   ├── HEAD
    │   │   └── refs
    │   │       ├── heads
    │   │       │   └── main
    │   │       └── remotes
    │   │           └── origin
    │   │               └── HEAD
    │   ├── objects
    │   │   ├── info
    │   │   └── pack
    │   │       ├── pack-0131ac062d489b7e8a92fecda475c99638c3004b.idx
    │   │       ├── pack-0131ac062d489b7e8a92fecda475c99638c3004b.pack
    │   │       └── pack-0131ac062d489b7e8a92fecda475c99638c3004b.rev
    │   ├── packed-refs
    │   └── refs
    │       ├── heads
    │       │   └── main
    │       ├── remotes
    │       │   └── origin
    │       │       └── HEAD
    │       └── tags
    ├── .gitignore
    ├── images
    │   ├── centralized_avsddac.png
    │   ├── inside_dac.png
    │   ├── inside_pll.png
    │   ├── openlane_flow.png
    │   ├── physical_design.png
    │   ├── post_routing_sim.png
    │   ├── post_synth_sim.png
    │   ├── pre_synth_sim.png
    │   ├── rvmyth_layout.png
    │   ├── selected_dac.png
    │   ├── selected_pll.png
    │   ├── vsdbabysoc_block_diagram.png
    │   └── vsdbabysoc_layout.png
    ├── LICENSE
    ├── Makefile
    ├── README.md
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
        │   ├── avsddac.v
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

32 directories, 79 files
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ mkdir simulation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ ls
simulation  VSDBabySoC
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc$ cd VSDBabySoC
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ iverilog -o output/pre_synth_sim.out -DPRE_SYNTH_SIM src/module/testbench.v -I src/include -I src/module
output/pre_synth_sim.out: No such file or directory
error: Code generator failure: -1
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ ls -a
.  ..  .git  .gitignore  images  LICENSE  Makefile  README.md  src
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ cd simulation
bash: cd: simulation: No such file or directory
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ mkdir simulation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ iverilog -o simulation/pre_synth_sim.out -DPRE_SYNTH_SIM src/module/testbench.v -I src/include -I src/module
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ cd simulation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ ls
pre_synth_sim.out
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ ./pre_synth_sim.out
VCD info: dumpfile pre_synth_sim.vcd opened for output.
src/module/testbench.v:63: $finish called at 84999000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ iverilog -o simulation/pre_synth_sim.out -DPRE_SYNTH_SIM src/module/testbench.v -I src/include -I src/module
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC$ cd simulation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ ./pre_synth_sim.out
VCD info: dumpfile pre_synth_sim.vcd opened for output.
src/module/testbench.v:63: $finish called at 84999000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ gtkwave pre_synth_sim.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[84999000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ gtkwave pre_synth_sim.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[84999000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ gtkwave pre_synth_sim.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[84999000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2/babysoc/VSDBabySoC/simulation$ 

