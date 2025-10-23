```bash
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ echo "WEEK_5 | Author: Shwetank Shekhar"
WEEK_5 | Author: Shwetank Shekhar
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ cd Desktop/SoC_Shwetank/OpenROAD-flow-scripts
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ docker images
REPOSITORY                                                                              TAG                                              IMAGE ID       CREATED        SIZE
openroad/flow-ubuntu22.04-builder                                                       ee5a20                                           32acda45f81a   2 hours ago    4.59GB
openroad/flow-ubuntu22.04-dev                                                           ee5a20                                           005d6c3afd37   2 hours ago    3.27GB
openroad/orfs                                                                           latest                                           d7e3cd14164e   10 hours ago   4.63GB
ubuntu                                                                                  
22.04                                            392fa14dddd0   3 weeks ago    77.9MB
ghcr.io/the-openroad-project/openlane                                                   ff5509f65b17bfa4068d5336495ab1718987ff69         ff3bf7bec907   5 weeks ago    1.11GB
ghcr.io/the-openroad-project/openlane                                                   ff5509f65b17bfa4068d5336495ab1718987ff69-amd64   ff3bf7bec907   5 weeks ago    1.11GB

ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ docker run --rm -it -u $(id -u ${USER}):$(id -g ${USER}) -v $(pwd)/flow:/OpenROAD-flow-scripts/flow openroad/flow-ubuntu22.04-builder:ee5a20
groups: cannot find name for group ID 1000
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ source ./env.sh
OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ yosys -version
Error parsing options: Argument 'ersion' failed to parse
Run 'yosys --help' for help.
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ yosys --version
Yosys 0.58+35 (git sha1 UNKNOWN, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ openroad --version
OpenROAD 24Q3-10021-gc8a6603b7f 
Features included (+) or not (-): +GPU +GUI +Python
This program is licensed under the BSD-3 license. See the LICENSE file for details.
Components of this program may be licensed under more restrictive licenses which must be honored.
Usage: openroad [-help] [-version] [-no_init] [-no_splash] [-exit] [-gui] [-threads count|max] [-log file_name] [-metrics file_name] [-db file_name] [-no_settings] [-minimize] cmd_file
  -help                 show help and exit
  -version              show version and exit
  -no_init              do not read .openroad init file
  -threads count|max    use count threads
  -no_splash            do not show the license splash at startup
  -exit                 exit after reading cmd_file
  -gui                  start in gui mode
  -minimize             start the gui minimized
  -no_settings          do not load the previous gui settings
  -python               start with python interpreter [limited to db operations]
  -log <file_name>      write a log in <file_name>
  -metrics <file_name>  write metrics in <file_name> in JSON format
  -db <file_name>      open a .odb database at startup
  cmd_file              source cmd_file
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ openroad -version
24Q3-10021-gc8a6603b7f 
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts$ cd flow
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts/flow$ make
./logs/nangate45/gcd/base
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
1_1_yosys_canonicalize             0             40 e25a778b8828075f6910
1_2_yosys                          0             43 b493eb7923d7e3489ff2
2_1_floorplan                      0            121 f1c432f93fea530b0ca3
2_2_floorplan_macro                0             97 f1c432f93fea530b0ca3
2_3_floorplan_tapcell              0             96 4dbc8d6c74715b852a5a
2_4_floorplan_pdn                  0             99 53250f9289c62312a7bb
3_1_place_gp_skip_io               0             98 5905b0f4c0c0a03b79bd
3_2_place_iop                      0             97 73a7cb0630cf5c88c628
3_3_place_gp                       0            212 01b5b2efc39ab0ad03d5
3_4_place_resized                  0            117 01b5b2efc39ab0ad03d5
3_5_place_dp                       0            103 d6264844858807cdbbc1
4_1_cts                            1            125 80dfde6ed7c4e186f939
5_1_grt                            4            218 aeb3f9e6f5cf1d1c82c7
5_2_route                         11           1283 70d72f78711812b117ef
5_3_fillcell                       0             99 9793df0f24cf34ea457e
6_1_fill                           0             98 9793df0f24cf34ea457e
6_1_merge                          1            422                  N/A
6_report                           1            166                  N/A
Total                             18           1283                     
I have no name!@d2fd00a6efa9:/OpenROAD-flow-scripts/flow$ exit
exit
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ echo "else you can run using the "util/docker_shell <command>""
bash: command: No such file or directory
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ echo "else you can run using the 'util/docker_shell <command>'"
else you can run using the 'util/docker_shell <command>'
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ echo "else you can run using the (util/docker_shell <command>)"
else you can run using the (util/docker_shell <command>)
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts$ cd flow
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow$ util/docker_shell make
+++ dirname util/docker_shell
++ cd util
++ pwd
+ DIR=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow/util
+ get_container_engine
++ docker --version
+ local 'DOCKER_VERSION_STRING=Docker version 28.5.1, build e180ab8'
+ [[ Docker version 28.5.1, build e180ab8 == *\D\o\c\k\e\r* ]]
+ container_engine=docker
++ pwd
+ WORKSPACE=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow
+ YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys
+ OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad
+ KLAYOUT_CMD=/usr/bin/klayout
+ XSOCK=/tmp/.X11-unix
+ XAUTH=/tmp/.docker.xauth
+ xauth nlist :0
+ sed -e 's/^..../ffff/'
+ xauth -f /tmp/.docker.xauth nmerge -
+ ARGUMENTS=make
+ test -t 0
+ DOCKER_INTERACTIVE=-ti
+ [[ docker == \p\o\d\m\a\n ]]
++ id -u ank
++ id -g ank
+ user_args='-u 1000:1000'
+ docker run -u 1000:1000 -e LIBGL_ALWAYS_SOFTWARE=1 -e QT_X11_NO_MITSHM=1 -e XDG_RUNTIME_DIR=/tmp/xdg-run -e DISPLAY=:0 -e QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth -e XAUTHORITY=/tmp/.docker.xauth -e FLOW_HOME=/OpenROAD-flow-scripts/flow/ -e YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys -e OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad -e KLAYOUT_CMD=/usr/bin/klayout -v /home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow:/OpenROAD-flow-scripts/flow:Z --network host -ti openroad/orfs:latest bash -c 'set -ex
 mkdir /tmp/xdg-run
 cd /OpenROAD-flow-scripts/flow
 . ../env.sh
 make
'
+ mkdir /tmp/xdg-run
+ cd /OpenROAD-flow-scripts/flow
+ . ../env.sh
++ __setpaths
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++++ readlink -f ../env.sh
+++ dirname /OpenROAD-flow-scripts/env.sh
++ DIR=/OpenROAD-flow-scripts
++ export OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ echo 'OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD'
OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD
++ export PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ export PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++ export FLOW_HOME=/OpenROAD-flow-scripts/flow
++ FLOW_HOME=/OpenROAD-flow-scripts/flow
++ unset -f __setpaths
+ make
./logs/nangate45/gcd/base
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
1_1_yosys_canonicalize             0             40 e25a778b8828075f6910
1_2_yosys                          0             43 b493eb7923d7e3489ff2
2_1_floorplan                      0            121 f1c432f93fea530b0ca3
2_2_floorplan_macro                0             97 f1c432f93fea530b0ca3
2_3_floorplan_tapcell              0             96 4dbc8d6c74715b852a5a
2_4_floorplan_pdn                  0             99 53250f9289c62312a7bb
3_1_place_gp_skip_io               0             98 5905b0f4c0c0a03b79bd
3_2_place_iop                      0             97 73a7cb0630cf5c88c628
3_3_place_gp                       0            212 01b5b2efc39ab0ad03d5
3_4_place_resized                  0            117 01b5b2efc39ab0ad03d5
3_5_place_dp                       0            103 d6264844858807cdbbc1
4_1_cts                            1            125 80dfde6ed7c4e186f939
5_1_grt                            4            218 aeb3f9e6f5cf1d1c82c7
5_2_route                         11           1283 70d72f78711812b117ef
5_3_fillcell                       0             99 9793df0f24cf34ea457e
6_1_fill                           0             98 9793df0f24cf34ea457e
6_1_merge                          1            422                  N/A
6_report                           1            166                  N/A
Total                             18           1283                     
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow$ util/docker_shell gui_final
+++ dirname util/docker_shell
++ cd util
++ pwd
+ DIR=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow/util
+ get_container_engine
++ docker --version
+ local 'DOCKER_VERSION_STRING=Docker version 28.5.1, build e180ab8'
+ [[ Docker version 28.5.1, build e180ab8 == *\D\o\c\k\e\r* ]]
+ container_engine=docker
++ pwd
+ WORKSPACE=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow
+ YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys
+ OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad
+ KLAYOUT_CMD=/usr/bin/klayout
+ XSOCK=/tmp/.X11-unix
+ XAUTH=/tmp/.docker.xauth
+ xauth nlist :0
+ sed -e 's/^..../ffff/'
+ xauth -f /tmp/.docker.xauth nmerge -
+ ARGUMENTS=gui_final
+ test -t 0
+ DOCKER_INTERACTIVE=-ti
+ [[ docker == \p\o\d\m\a\n ]]
++ id -u ank
++ id -g ank
+ user_args='-u 1000:1000'
+ docker run -u 1000:1000 -e LIBGL_ALWAYS_SOFTWARE=1 -e QT_X11_NO_MITSHM=1 -e XDG_RUNTIME_DIR=/tmp/xdg-run -e DISPLAY=:0 -e QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth -e XAUTHORITY=/tmp/.docker.xauth -e FLOW_HOME=/OpenROAD-flow-scripts/flow/ -e YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys -e OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad -e KLAYOUT_CMD=/usr/bin/klayout -v /home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow:/OpenROAD-flow-scripts/flow:Z --network host -ti openroad/orfs:latest bash -c 'set -ex
 mkdir /tmp/xdg-run
 cd /OpenROAD-flow-scripts/flow
 . ../env.sh
 gui_final
'
+ mkdir /tmp/xdg-run
+ cd /OpenROAD-flow-scripts/flow
+ . ../env.sh
++ __setpaths
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++++ readlink -f ../env.sh
+++ dirname /OpenROAD-flow-scripts/env.sh
++ DIR=/OpenROAD-flow-scripts
++ export OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ echo 'OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD'
OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD
++ export PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ export PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++ export FLOW_HOME=/OpenROAD-flow-scripts/flow
++ FLOW_HOME=/OpenROAD-flow-scripts/flow
++ unset -f __setpaths
+ gui_final
bash: line 5: gui_final: command not found
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow$ util/docker_shell make gui_final
+++ dirname util/docker_shell
++ cd util
++ pwd
+ DIR=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow/util
+ get_container_engine
++ docker --version
+ local 'DOCKER_VERSION_STRING=Docker version 28.5.1, build e180ab8'
+ [[ Docker version 28.5.1, build e180ab8 == *\D\o\c\k\e\r* ]]
+ container_engine=docker
++ pwd
+ WORKSPACE=/home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow
+ YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys
+ OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad
+ KLAYOUT_CMD=/usr/bin/klayout
+ XSOCK=/tmp/.X11-unix
+ XAUTH=/tmp/.docker.xauth
+ xauth nlist :0
+ sed -e 's/^..../ffff/'
+ xauth -f /tmp/.docker.xauth nmerge -
+ ARGUMENTS='make gui_final'
+ test -t 0
+ DOCKER_INTERACTIVE=-ti
+ [[ docker == \p\o\d\m\a\n ]]
++ id -u ank
++ id -g ank
+ user_args='-u 1000:1000'
+ docker run -u 1000:1000 -e LIBGL_ALWAYS_SOFTWARE=1 -e QT_X11_NO_MITSHM=1 -e XDG_RUNTIME_DIR=/tmp/xdg-run -e DISPLAY=:0 -e QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth -e XAUTHORITY=/tmp/.docker.xauth -e FLOW_HOME=/OpenROAD-flow-scripts/flow/ -e YOSYS_EXE=/OpenROAD-flow-scripts/tools/install/yosys/bin/yosys -e OPENROAD_EXE=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad -e KLAYOUT_CMD=/usr/bin/klayout -v /home/ank/Desktop/SoC_Shwetank/OpenROAD-flow-scripts/flow:/OpenROAD-flow-scripts/flow:Z --network host -ti openroad/orfs:latest bash -c 'set -ex
 mkdir /tmp/xdg-run
 cd /OpenROAD-flow-scripts/flow
 . ../env.sh
 make gui_final
'
+ mkdir /tmp/xdg-run
+ cd /OpenROAD-flow-scripts/flow
+ . ../env.sh
++ __setpaths
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++++ readlink -f ../env.sh
+++ dirname /OpenROAD-flow-scripts/env.sh
++ DIR=/OpenROAD-flow-scripts
++ export OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ OPENROAD=/OpenROAD-flow-scripts/tools/OpenROAD
++ echo 'OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD'
OPENROAD: /OpenROAD-flow-scripts/tools/OpenROAD
++ export PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ export PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ PATH=/OpenROAD-flow-scripts/tools/install/yosys/bin:/OpenROAD-flow-scripts/tools/install/OpenROAD/bin:/usr/local/bin/wrapped-cc:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
++ [[ linux-gnu == \d\a\r\w\i\n* ]]
++ export FLOW_HOME=/OpenROAD-flow-scripts/flow
++ FLOW_HOME=/OpenROAD-flow-scripts/flow
++ unset -f __setpaths
+ make gui_final
ODB_FILE=./results/nangate45/gcd/base/6_final.odb /OpenROAD-flow-scripts/tools/install/OpenROAD/bin/openroad -gui  /OpenROAD-flow-scripts/flow/scripts/open.tcl
QStandardPaths: wrong permissions on runtime directory /tmp/xdg-run, 0755 instead of 0700
OpenROAD 24Q3-10021-gc8a6603b7f 
Features included (+) or not (-): +GPU +GUI +Python
This program is licensed under the BSD-3 license. See the LICENSE file for details.
Components of this program may be licensed under more restrictive licenses which must be honored.
read_liberty /OpenROAD-flow-scripts/flow/platforms/nangate45/lib/NangateOpenCellLibrary_typical.lib
read_db ./results/nangate45/gcd/base/6_final.odb
GUI_TIMING=1 reading timing, takes a little while for large designs...
read_sdc /OpenROAD-flow-scripts/flow/results/nangate45/gcd/base/6_final.sdc
read_spef ./results/nangate45/gcd/base/6_final.spef
sta::find_timing
sta::find_requireds
gui::select_chart "Endpoint Slack"
gui::update_timing_report
```
