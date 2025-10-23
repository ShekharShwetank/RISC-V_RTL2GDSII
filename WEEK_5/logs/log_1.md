```bash
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
```
