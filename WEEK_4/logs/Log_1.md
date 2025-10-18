```bash
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ source soc_env/bin/activate
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
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd WEEK_4
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ ls -a
.  ..  week4.pdf
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ echo "working directory for week 4 tasks"
working directory for week 4 tasks
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ git clone https://github.com/kunalg123/sky130CircuitDesignWorkshop.git
Cloning into 'sky130CircuitDesignWorkshop'...
remote: Enumerating objects: 175, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 175 (delta 1), reused 0 (delta 0), pack-reused 166 (from 1)
Receiving objects: 100% (175/175), 1.75 MiB | 6.67 MiB/s, done.
Resolving deltas: 100% (52/52), done.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ ls -a
.  ..  sky130CircuitDesignWorkshop  week4.pdf
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ tree -a
.
├── sky130CircuitDesignWorkshop
│   ├── design
│   │   ├── day1_nfet_idvds_L2_W5.spice
│   │   ├── day2_nfet_idvds_L015_W039.spice
│   │   ├── day2_nfet_idvgs_L015_W039.spice
│   │   ├── day3_inv_tran_Wp084_Wn036.spice
│   │   ├── day3_inv_vtc_Wp084_Wn036.spice
│   │   ├── day4_inv_noisemargin_wp1_wn036.spice
│   │   ├── day5_inv_devicevariation_wp7_wn042.spice
│   │   ├── day5_inv_supplyvariation_Wp1_Wn036.spice
│   │   └── sky130_fd_pr
│   │       ├── cells
│   │       │   ├── nfet_01v8
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__ff.corner.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__ff.pm3.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__fs.corner.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__fs.pm3.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__mismatch.corner.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8.pm3.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__sf.corner.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__sf.pm3.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__ss.corner.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__ss.pm3.spice
│   │       │   │   ├── sky130_fd_pr__nfet_01v8__tt.corner.spice
│   │       │   │   └── sky130_fd_pr__nfet_01v8__tt.pm3.spice
│   │       │   └── pfet_01v8
│   │       │       ├── sky130_fd_pr__pfet_01v8__ff.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__ff.pm3.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__fs.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__fs.pm3.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__mismatch.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8.pm3.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__sf.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__sf.pm3.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__ss.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__ss.pm3.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__tt.corner.spice
│   │       │       ├── sky130_fd_pr__pfet_01v8__tt_discrete.corner.spice
│   │       │       └── sky130_fd_pr__pfet_01v8__tt.pm3.spice
│   │       ├── LICENSE
│   │       ├── models
│   │       │   ├── all.spice
│   │       │   ├── parameters
│   │       │   │   ├── critical.spice
│   │       │   │   ├── fast_70p.spice
│   │       │   │   ├── fast.spice
│   │       │   │   ├── invariant.spice
│   │       │   │   ├── lod.spice
│   │       │   │   ├── montecarlo.spice
│   │       │   │   ├── slow_70p.spice
│   │       │   │   ├── slow.spice
│   │       │   │   └── typical.spice
│   │       │   └── sky130.lib.spice
│   │       └── README.rst
│   ├── .git
│   │   ├── branches
│   │   ├── config
│   │   ├── description
│   │   ├── HEAD
│   │   ├── hooks
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   └── update.sample
│   │   ├── index
│   │   ├── info
│   │   │   └── exclude
│   │   ├── logs
│   │   │   ├── HEAD
│   │   │   └── refs
│   │   │       ├── heads
│   │   │       │   └── main
│   │   │       └── remotes
│   │   │           └── origin
│   │   │               └── HEAD
│   │   ├── objects
│   │   │   ├── info
│   │   │   └── pack
│   │   │       ├── pack-e498ba9f867e1a9faf027e60e75de0d976d06cbc.idx
│   │   │       ├── pack-e498ba9f867e1a9faf027e60e75de0d976d06cbc.pack
│   │   │       └── pack-e498ba9f867e1a9faf027e60e75de0d976d06cbc.rev
│   │   ├── packed-refs
│   │   └── refs
│   │       ├── heads
│   │       │   └── main
│   │       ├── remotes
│   │       │   └── origin
│   │       │       └── HEAD
│   │       └── tags
│   └── README.md
└── week4.pdf

26 directories, 76 files
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ ls -a
.  ..  sky130CircuitDesignWorkshop  week4.pdf
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ cd sky130CircuitDesignWorkshop
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop$ ls
design	README.md
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop$ cd design
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day4_inv_noisemargin_wp1_wn036.spice
day2_nfet_idvds_L015_W039.spice  day5_inv_devicevariation_wp7_wn042.spice
day2_nfet_idvgs_L015_W039.spice  day5_inv_supplyvariation_Wp1_Wn036.spice
day3_inv_tran_Wp084_Wn036.spice  sky130_fd_pr
day3_inv_vtc_Wp084_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ cd sky130_fd_pr
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ ls
cells  LICENSE	models	README.rst
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ cd cells/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ ls
nfet_01v8  pfet_01v8
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ cd nfet_01v8
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ ls
sky130_fd_pr__nfet_01v8__ff.corner.spice	sky130_fd_pr__nfet_01v8__sf.corner.spice
sky130_fd_pr__nfet_01v8__ff.pm3.spice		sky130_fd_pr__nfet_01v8__sf.pm3.spice
sky130_fd_pr__nfet_01v8__fs.corner.spice	sky130_fd_pr__nfet_01v8__ss.corner.spice
sky130_fd_pr__nfet_01v8__fs.pm3.spice		sky130_fd_pr__nfet_01v8__ss.pm3.spice
sky130_fd_pr__nfet_01v8__mismatch.corner.spice	sky130_fd_pr__nfet_01v8__tt.corner.spice
sky130_fd_pr__nfet_01v8.pm3.spice		sky130_fd_pr__nfet_01v8__tt.pm3.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ less sky130_fd_pr__nfet_01v8__tt.pm3.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ less sky130_fd_pr__nfet_01v8__tt.corner.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ cd ../../model/
bash: cd: ../../model/: No such file or directory
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ cd ../../models/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ ls
all.spice  parameters  sky130.lib.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ less sky130.lib.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ cd ../../
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4$ cd sky130CircuitDesignWorkshop
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop$ cd design
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day4_inv_noisemargin_wp1_wn036.spice
day2_nfet_idvds_L015_W039.spice  day5_inv_devicevariation_wp7_wn042.spice
day2_nfet_idvgs_L015_W039.spice  day5_inv_supplyvariation_Wp1_Wn036.spice
day3_inv_tran_Wp084_Wn036.spice  sky130_fd_pr
day3_inv_vtc_Wp084_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day1_nfet_idvds_L2_W5.spice
Gtk-Message: 11:04:17.823: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:23848): GLib-GIO-WARNING **: 11:04:18.619: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day1_nfet_idvds_L2_W5.spice
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 190

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: op1 (Operating Point)
Date: Sat Oct 18 11:06:47  2025

    in                  : voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#body: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 1 long
    n1                  : voltage, real, 1 long
    vdd                 : voltage, real, 1 long [default scale]
    vdd#branch          : current, real, 1 long
    vin#branch          : current, real, 1 long
ngspice 1 -> plot -vdd#branch
ngspice 2 -> /home/ank/tmp/hc24060_0.ps: No such file or directory
/home/ank/tmp/hc24060_1.svg: No such file or directory

x0 = 1.09891, y0 = 0.000276744

x0 = 1.1, y0 = 0.000116744

x0 = 1.02283, y0 = 0.000142791    x1 = 1.1837, y1 = 0.000214419
dx = 0.16087, dy = 7.16279e-05
dy/dx = 0.000445255    dx/dy = 2245.91

x0 = 1.08261, y0 = 0.000214419    x1 = 1.225, y1 = 0.000177674
dx = 0.142391, dy = -3.67442e-05
dy/dx = -0.000258051    dx/dy = -3875.21

x0 = 1.225, y0 = 0.000177674

x0 = 1.225, y0 = 0.000177674    x1 = 1.07065, y1 = 0.000216279
dx = -0.154348, dy = 3.86047e-05
dy/dx = -0.000250115    dx/dy = -3998.17

x0 = 1.07065, y0 = 0.000216279    x1 = 1.21196, y1 = 0.000158605
dx = 0.141304, dy = -5.76744e-05
dy/dx = -0.000408157    dx/dy = -2450.04

x0 = 1.19565, y0 = 0.00011814

ngspice 2 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ cd sky130_fd_pr
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ ls
cells  LICENSE	models	README.rst
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ cd cells/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ ls
nfet_01v8  pfet_01v8
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ cd nfet_01v8/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ ls
sky130_fd_pr__nfet_01v8__ff.corner.spice  sky130_fd_pr__nfet_01v8__fs.pm3.spice		  sky130_fd_pr__nfet_01v8__sf.corner.spice  sky130_fd_pr__nfet_01v8__ss.pm3.spice
sky130_fd_pr__nfet_01v8__ff.pm3.spice	  sky130_fd_pr__nfet_01v8__mismatch.corner.spice  sky130_fd_pr__nfet_01v8__sf.pm3.spice     sky130_fd_pr__nfet_01v8__tt.corner.spice
sky130_fd_pr__nfet_01v8__fs.corner.spice  sky130_fd_pr__nfet_01v8.pm3.spice		  sky130_fd_pr__nfet_01v8__ss.corner.spice  sky130_fd_pr__nfet_01v8__tt.pm3.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells/nfet_01v8$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ ls
nfet_01v8  pfet_01v8
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/cells$ cd ..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ ls
cells  LICENSE	models	README.rst
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr$ cd models/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ ls
all.spice  parameters  sky130.lib.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ less sky130.lib.spice 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ less all.spice 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design/sky130_fd_pr/models$ cd ../../
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day1_nfet_idvds_L2_W5.spice 
Gtk-Message: 11:17:38.477: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:24430): GLib-GIO-WARNING **: 11:17:38.718: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day1_nfet_idvds_L2_W5.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 190

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: op1 (Operating Point)
Date: Sat Oct 18 11:19:30  2025

    in                  : voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#body: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 1 long
    n1                  : voltage, real, 1 long
    vdd                 : voltage, real, 1 long [default scale]
    vdd#branch          : current, real, 1 long
    vin#branch          : current, real, 1 long
ngspice 2 -> plot -vdd#branch
ngspice 3 -> 
x0 = 1.51848, y0 = 1.30233e-05    x1 = 1.79348, y1 = -1.02326e-05
dx = 0.275, dy = -2.32558e-05
dy/dx = -8.45666e-05    dx/dy = -11825

x0 = 1.53804, y0 = 1.2093e-05    x1 = 1.79891, y1 = -4.18605e-06
dx = 0.26087, dy = -1.62791e-05
dy/dx = -6.24031e-05    dx/dy = -16024.8

x0 = 1.30109, y0 = 0.000117674

ngspice 3 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day2_nfet_idv
day2_nfet_idvds_L015_W039.spice  day2_nfet_idvgs_L015_W039.spice  
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day2_nfet_idvds_L015_W039.spice 
Gtk-Message: 11:27:47.148: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:24876): GLib-GIO-WARNING **: 11:27:47.376: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)

(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day2_nfet_idvds_L015_W039.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  1.10000e+00
No. of Data Rows : 190

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: op1 (Operating Point)
Date: Sat Oct 18 11:29:13  2025

    in                  : voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#body: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 1 long
    n1                  : voltage, real, 1 long
    vdd                 : voltage, real, 1 long [default scale]
    vdd#branch          : current, real, 1 long
    vin#branch          : current, real, 1 long
ngspice 3 -> plot -vdd#branch
ngspice 4 -> 
x0 = 1.80204, y0 = 0.000197067

ngspice 4 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day2_nfet_idvgs_L015_W039.spice 
Gtk-Message: 11:32:47.014: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:25246): GLib-GIO-WARNING **: 11:32:47.244: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day2_nfet_idvgs_L015_W039.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 19

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: op1 (Operating Point)
Date: Sat Oct 18 11:33:27  2025

    in                  : voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#body: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 1 long
    n1                  : voltage, real, 1 long
    vdd                 : voltage, real, 1 long [default scale]
    vdd#branch          : current, real, 1 long
    vin#branch          : current, real, 1 long
ngspice 4 -> plot -vdd#branch
ngspice 5 -> 
x0 = 1.8, y0 = 0.000196944

x0 = 1.24174, y0 = 0.000116389    x1 = 1.5513, y1 = 7.88889e-05
dx = 0.309565, dy = -3.75e-05
dy/dx = -0.000121138    dx/dy = -8255.07

x0 = 1.20348, y0 = 0.000139444    x1 = 1.51652, y1 = 8.02778e-05
dx = 0.313043, dy = -5.91667e-05
dy/dx = -0.000189005    dx/dy = -5290.88

x0 = 0.8, y0 = 4.36111e-05    x1 = 1.11478, y1 = 4.16667e-06
dx = 0.314783, dy = -3.94444e-05
dy/dx = -0.000125307    dx/dy = -7980.4

ngspice 5 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day2_nfet_idvgs_L015_W039.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 19

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: op1 (Operating Point)
Date: Sat Oct 18 11:36:22  2025

    in                  : voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#body: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 1 long
    m.xm1.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 1 long
    n1                  : voltage, real, 1 long
    vdd                 : voltage, real, 1 long [default scale]
    vdd#branch          : current, real, 1 long
    vin#branch          : current, real, 1 long
ngspice 5 -> plot -vdd#branch
ngspice 6 -> 
x0 = 0.629348, y0 = 3.95349e-05    x1 = 1.10978, y1 = 0
dx = 0.480435, dy = -3.95349e-05
dy/dx = -8.22898e-05    dx/dy = -12152.2

x0 = 0.770652, y0 = 0

x0 = 1.27391, y0 = 8e-05    x1 = 0.85, y1 = 4.76744e-05
dx = -0.423913, dy = -3.23256e-05
dy/dx = 7.62552e-05    dx/dy = 13113.9

x0 = 0.686957, y0 = 7.39535e-05    x1 = 0.798913, y1 = 5.65116e-05
dx = 0.111957, dy = -1.74419e-05
dy/dx = -0.000155791    dx/dy = -6418.84

ngspice 6 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day3_inv_
Gtk-Message: 11:43:21.680: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:25875): GLib-GIO-WARNING **: 11:43:21.941: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day3_inv_
day3_inv_tran_Wp084_Wn036.spice  day3_inv_vtc_Wp084_Wn036.spice   
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day3_inv_vtc_Wp084_Wn036.spice 
Gtk-Message: 11:43:43.637: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:25975): GLib-GIO-WARNING **: 11:43:43.866: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day3_inv_vtc_Wp084_Wn036.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 181

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: dc1 (DC transfer characteristic)
Date: Sat Oct 18 11:44:33  2025

    in                  : voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#body: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#dbody: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#sbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#body: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 181 long
    out                 : voltage, real, 181 long
    v-sweep             : voltage, real, 181 long [default scale]
    vdd                 : voltage, real, 181 long
    vdd#branch          : current, real, 181 long
    vin#branch          : current, real, 181 long
ngspice 6 -> plot out vs in
ngspice 7 -> 
x0 = 0.788421, y0 = 1.13191    x1 = 0.714737, y1 = 1.1
dx = -0.0736842, dy = -0.0319149
dy/dx = 0.433131    dx/dy = 2.30877

x0 = 0.794737, y0 = 1.13191    x1 = 0.927368, y1 = 0.912766
dx = 0.132632, dy = -0.219149
dy/dx = -1.65231    dx/dy = -0.605212

x0 = 0.794737, y0 = 1.15106    x1 = 0.937895, y1 = 0.855319
dx = 0.143158, dy = -0.295745
dy/dx = -2.06586    dx/dy = -0.484059

x0 = 1.02421, y0 = 0.570213    x1 = 0.835789, y1 = 0.870213
dx = -0.188421, dy = 0.3
dy/dx = -1.59218    dx/dy = -0.62807

x0 = 0.974737, y0 = 0.66383    x1 = 0.817895, y1 = 0.885106
dx = -0.156842, dy = 0.221277
dy/dx = -1.41082    dx/dy = -0.708806

x0 = 0.795789, y0 = 1.11277    x1 = 0.954737, y1 = 0.742553
dx = 0.158947, dy = -0.370213
dy/dx = -2.32915    dx/dy = -0.429341

x0 = 0.868417, y0 = 0.927564    x1 = 0.87375, y1 = 0.88141
dx = 0.00533333, dy = -0.0461538
dy/dx = -8.65385    dx/dy = -0.115556

x0 = 0.876609, y0 = 0.88

x0 = 0.876609, y0 = 0.88

x0 = 0.876609, y0 = 0.88

x0 = 0.875652, y0 = 0.8905

x0 = 0.875304, y0 = 0.89325

x0 = 0.875, y0 = 0.89675

x0 = 0.874783, y0 = 0.90025

x0 = 0.876696, y0 = 0.87975

x0 = 0.877652, y0 = 0.86925

x0 = 0.877522, y0 = 0.8705

x0 = 0.877304, y0 = 0.87275

x0 = 0.877174, y0 = 0.87475

x0 = 0.877, y0 = 0.8765

x0 = 0.87687, y0 = 0.8775

x0 = 0.876609, y0 = 0.87875

x0 = 0.876652, y0 = 0.87875

x0 = 0.87687, y0 = 0.8775

x0 = 0.87687, y0 = 0.8775

ngspice 7 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day3_inv_trans_Wp084_Wn036.spice 
Gtk-Message: 12:05:22.980: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:26716): GLib-GIO-WARNING **: 12:05:23.220: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day3_inv_tran_Wp084_Wn036.spice 
Gtk-Message: 12:06:07.279: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:26849): GLib-GIO-WARNING **: 12:06:07.519: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day3_inv_tran_Wp084_Wn036.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

Initial Transient Solution
--------------------------

Node                                   Voltage
----                                   -------
out                                        1.8
in                                           0
vdd                                        1.8
vin#branch                                   0
vdd#branch                        -1.85734e-12

 Reference value :  0.00000e+00
No. of Data Rows : 97
ngspice 7 -> plot out vs time in
ngspice 8 -> 
x0 = 2.48301e-09, y0 = 0.89973

x0 = 2.15033e-09, y0 = 0.9

x0 = 4.335e-09, y0 = 0.899535

x0 = 4.05e-09, y0 = 0.9

ngspice 8 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day4_inv_noisemargin_wp1_wn036.spice
Gtk-Message: 13:58:47.361: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:30027): GLib-GIO-WARNING **: 13:58:47.617: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day4_inv_noisemargin_wp1_wn036.spice
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 181

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: dc1 (DC transfer characteristic)
Date: Sat Oct 18 13:59:10  2025

    in                  : voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#body: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#dbody: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#sbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#body: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 181 long
    out                 : voltage, real, 181 long
    v-sweep             : voltage, real, 181 long [default scale]
    vdd                 : voltage, real, 181 long
    vdd#branch          : current, real, 181 long
    vin#branch          : current, real, 181 long
ngspice 8 -> plot out vs in
ngspice 9 -> 
x0 = 0.786316, y0 = 1.67872

x0 = 0.975789, y0 = 0.110638

x0 = 0.65625, y0 = 1.8    x1 = 0.90625, y1 = 1.49825
dx = 0.25, dy = -0.301754
dy/dx = -1.20702    dx/dy = -0.828488

x0 = 0.898684, y0 = 0.402985    x1 = 1.29737, y1 = 0.00149254
dx = 0.398684, dy = -0.401493
dy/dx = -1.00704    dx/dy = -0.993005

ngspice 9 -> EXI
EXI: no such command available in ngspice
ngspice 10 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ls
day1_nfet_idvds_L2_W5.spice	 day2_nfet_idvgs_L015_W039.spice  day3_inv_vtc_Wp084_Wn036.spice	day5_inv_devicevariation_wp7_wn042.spice  sky130_fd_pr
day2_nfet_idvds_L015_W039.spice  day3_inv_tran_Wp084_Wn036.spice  day4_inv_noisemargin_wp1_wn036.spice	day5_inv_supplyvariation_Wp1_Wn036.spice
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day_5_inv_s
Gtk-Message: 14:10:21.390: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:30858): GLib-GIO-WARNING **: 14:10:21.631: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day5_inv_supplyvariation_Wp1_Wn036.spice 
Gtk-Message: 14:10:38.690: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:30952): GLib-GIO-WARNING **: 14:10:38.921: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day5_inv_supplyvariation_Wp1_Wn036.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 181
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 181
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 181
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 181
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 181
Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver

No. of Data Rows : 181
ngspice 10 -> 
x0 = 0.410753, y0 = 1.86383

ngspice 10 -> 
x0 = 0.772043, y0 = 1.70426

x0 = 0.98172, y0 = 0.0978723

x0 = 0.491398, y0 = 0.96383

x0 = 0.582796, y0 = 0.0382979

x0 = 0.420408, y0 = 0.780851

x0 = 0.514286, y0 = 0.0191489

ngspice 10 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ gedit day5_inv_devicevariation_wp7_wn042.spice 
Gtk-Message: 14:27:42.738: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:31859): GLib-GIO-WARNING **: 14:27:42.966: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ ngspice day5_inv_devicevariation_wp7_wn042.spice 
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

Note: No compatibility mode selected!


Circuit: *model description

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using SPARSE 1.3 as Direct Linear Solver
 Reference value :  0.00000e+00
No. of Data Rows : 181

No. of Data Rows : 1
Here are the vectors currently active:

Title: *model description
Name: dc1 (DC transfer characteristic)
Date: Sat Oct 18 14:28:07  2025

    in                  : voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#body: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#dbody: voltage, real, 181 long
    m.xm1.msky130_fd_pr__pfet_01v8#sbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#body: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#dbody: voltage, real, 181 long
    m.xm2.msky130_fd_pr__nfet_01v8#sbody: voltage, real, 181 long
    out                 : voltage, real, 181 long
    v-sweep             : voltage, real, 181 long [default scale]
    vdd                 : voltage, real, 181 long
    vdd#branch          : current, real, 181 long
    vin#branch          : current, real, 181 long
ngspice 10 -> plot out vs in
ngspice 11 -> 
x0 = 0.893684, y0 = -0.0319149

x0 = 0.988214, y0 = 0.988197

ngspice 11 -> exit
ngspice-45.2 done
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_4/sky130CircuitDesignWorkshop/design$ 

```
