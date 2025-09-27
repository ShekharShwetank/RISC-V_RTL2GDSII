(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_good_mux.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_good_mux.v:23: $finish called at 300000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_good_mux.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[300000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v /home/ank/Desktop/SoC_Shwetank/verilog_files/blocking_caveat.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_blocking_caveat.v
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1160: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1160: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1161: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1161: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1162: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1162: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1163: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1163: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1164: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1164: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44983: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44983: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44984: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44984: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44985: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44985: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44986: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44986: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44987: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44987: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44988: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44988: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45404: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45404: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45405: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45405: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45406: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45406: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45407: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45407: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45408: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45408: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45409: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45409: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45817: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45817: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45818: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45818: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45819: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45819: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45820: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45820: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45821: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45821: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45822: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45822: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46193: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46193: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46194: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46194: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46195: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46195: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46565: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46565: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46566: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46566: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46567: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46567: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46936: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46936: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46937: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46937: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46938: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46938: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47294: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47294: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47295: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47295: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47296: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47296: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47652: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47652: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47653: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47653: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47654: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47654: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48010: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48010: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48011: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48011: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48012: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48012: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48384: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48384: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48385: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48385: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48386: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48386: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48758: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48758: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48759: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48759: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48760: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48760: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49116: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49116: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49117: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49117: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49118: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49118: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49474: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49474: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49475: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49475: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49476: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49476: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49832: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49832: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49833: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49833: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49834: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49834: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50176: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50176: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50177: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50177: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50516: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50516: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50517: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50517: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50842: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50842: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50843: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50843: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51168: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51168: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51169: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51169: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51494: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51494: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51495: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51495: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52076: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52076: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52077: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52077: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52408: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52408: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52409: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52409: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52740: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52740: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52741: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52741: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53129: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53129: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53130: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53130: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53131: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53131: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53522: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53522: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53523: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53523: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53524: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53524: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53907: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53907: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53908: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53908: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53909: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53909: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54292: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54292: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54293: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54293: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54294: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54294: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54662: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54662: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54663: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54663: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54664: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54664: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55032: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55032: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55033: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55033: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55034: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55034: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55402: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55402: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55403: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55403: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55404: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55404: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55769: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55769: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55770: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55770: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55771: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55771: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56136: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56136: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56137: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56137: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56138: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56138: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56503: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56503: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56504: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56504: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56505: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56505: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56857: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56857: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56858: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56858: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57207: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57207: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57208: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57208: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57549: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57549: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57550: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57550: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57883: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57883: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57884: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57884: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58217: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58217: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58218: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58218: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58551: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58551: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58552: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58552: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58877: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58877: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58878: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58878: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62269: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62269: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62270: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62270: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62271: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62271: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62272: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62272: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62626: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62626: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62627: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62627: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62628: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62628: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62629: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62629: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77991: warning: Timing checks are not supported and delayed signal "SLEEP_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77991: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77992: warning: Timing checks are not supported and delayed signal "SLEEP_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77992: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135137: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135137: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135138: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135138: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135139: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135139: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135140: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135140: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135141: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135141: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135142: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135142: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135143: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135143: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135144: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135144: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135145: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135145: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135146: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135146: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135606: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135606: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135607: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135607: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135608: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135608: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135609: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135609: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135610: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135610: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135611: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135611: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135612: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135612: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135613: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135613: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135614: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135614: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135615: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135615: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136067: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136067: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136068: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136068: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136069: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136069: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136070: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136070: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136071: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136071: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136072: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136072: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136073: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136073: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136074: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136074: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136075: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136075: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136076: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136076: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136498: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136498: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136499: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136499: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136500: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136500: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136501: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136501: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136502: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136502: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136503: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136503: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136504: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136504: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136925: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136925: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136926: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136926: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136927: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136927: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136928: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136928: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136929: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136929: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136930: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136930: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136931: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136931: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137344: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137344: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137345: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137345: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137346: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137346: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137347: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137347: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137348: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137348: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137349: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137349: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137350: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137350: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137755: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137755: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137756: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137756: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137757: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137757: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137758: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137758: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137759: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137759: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137760: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137760: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137761: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137761: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138166: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138166: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138167: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138167: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138168: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138168: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138169: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138169: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138170: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138170: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138171: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138171: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138172: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138172: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138577: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138577: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138578: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138578: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138579: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138579: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138580: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138580: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138581: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138581: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138582: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138582: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138583: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138583: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139004: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139004: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139005: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139005: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139006: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139006: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139007: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139007: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139008: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139008: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139009: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139009: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139010: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139010: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139431: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139431: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139432: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139432: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139433: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139433: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139434: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139434: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139435: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139435: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139436: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139436: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139437: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139437: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139842: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139842: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139843: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139843: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139844: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139844: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139845: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139845: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139846: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139846: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139847: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139847: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139848: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139848: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140253: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140253: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140254: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140254: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140255: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140255: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140256: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140256: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140257: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140257: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140258: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140258: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140259: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140259: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140664: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140664: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140665: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140665: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140666: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140666: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140667: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140667: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140668: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140668: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140669: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140669: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140670: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140670: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141054: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141054: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141055: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141055: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141056: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141056: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141057: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141057: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141058: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141058: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141059: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141059: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141442: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141442: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141443: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141443: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141444: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141444: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141445: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141445: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141446: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141446: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141447: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141447: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141816: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141816: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141817: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141817: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141818: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141818: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141819: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141819: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141820: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141820: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141821: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141821: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142190: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142190: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142191: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142191: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142192: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142192: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142193: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142193: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142194: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142194: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142195: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142195: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142564: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142564: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142565: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142565: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142566: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142566: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142567: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142567: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142568: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142568: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142569: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142569: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142937: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142937: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142938: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142938: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142939: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142939: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142940: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142940: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143307: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143307: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143308: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143308: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143309: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143309: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143310: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143310: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143677: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143677: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143678: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143678: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143679: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143679: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143680: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143680: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144087: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144087: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144088: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144088: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144089: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144089: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144090: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144090: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144091: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144091: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144092: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144092: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144093: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144093: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144094: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144094: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144502: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144502: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144503: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144503: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144504: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144504: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144505: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144505: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144506: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144506: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144507: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144507: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144508: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144508: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144509: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144509: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144903: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144903: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144904: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144904: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144905: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144905: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144906: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144906: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144907: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144907: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144908: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144908: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144909: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144909: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144910: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144910: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145304: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145304: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145305: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145305: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145306: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145306: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145307: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145307: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145308: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145308: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145309: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145309: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145310: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145310: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145311: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145311: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145705: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145705: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145706: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145706: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145707: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145707: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145708: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145708: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145709: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145709: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145710: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145710: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145711: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145711: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145712: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145712: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_blocking_caveat.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_blocking_caveat.v:24: $finish called at 3000000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_blocking_caveat.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3000000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ echo "WEEK_1_DAY_5"
WEEK_1_DAY_5
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_if.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_incomp_if.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_if.v:27: $finish called at 3000000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_incomp_if.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3000000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_if2.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_incomp_if2.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_if2.v:29: $finish called at 3000000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_incomp_if2.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3000000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_case.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_incomp_case.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_incomp_case.v:37: $finish called at 5011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_incomp_case.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[5011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_bad_case.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_bad_case.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_bad_case.v:36: $finish called at 3011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_bad_case.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_comp_case.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_comp_case.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_comp_case.v:38: $finish called at 5011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_comp_case.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[5011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_demux_case.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_demux_case.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_demux_case.v:38: $finish called at 3911000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_demux_case.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3911000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:7: syntax error
I give up.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:1: syntax error
I give up.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:10: syntax error
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:10: error: Invalid module instantiation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16: syntax error
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16: error: Invalid module instantiation
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16: error: port ``i3'' is not a port of uut.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16: warning: Port 4 (sel) of partial_case_assign expects 2 bits, got 1.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16:        : Padding 1 high bits of the port.
1 error(s) during elaboration.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16: warning: Port 4 (sel) of partial_case_assign expects 2 bits, got 1.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:16:        : Padding 1 high bits of the port.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_partial_case_assign.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:39: $finish called at 5011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_partial_case_assign.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_partial_case_assign.v:39: $finish called at 6011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_partial_case_assign.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[6011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_mux_generate.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_mux_generate.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_mux_generate.v:37: $finish called at 3011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_mux_generate.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_demux_generate.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_demux_generate.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_demux_generate.v:39: $finish called at 3911000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_demux_generate.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3911000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v /home/ank/Desktop/SoC_Shwetank/verilog_files/rca.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_rca.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_rca.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_rca.v:23: $finish called at 30011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_rca.v

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

Error opening  .vcd file 'tb_rca.v'.
Why: No such file or directory
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_rca.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[30011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v /home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v /home/ank/Desktop/SoC_Shwetank/verilog_files/rca.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_rca.v
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1160: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1160: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1161: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1161: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1162: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1162: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1163: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1163: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1164: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:1164: warning: Choosing typ expression.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44983: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44983: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44984: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44984: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44985: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44985: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44986: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44986: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44987: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44987: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44988: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:44988: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45404: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45404: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45405: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45405: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45406: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45406: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45407: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45407: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45408: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45408: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45409: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45409: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45817: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45817: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45818: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45818: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45819: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45819: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45820: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45820: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45821: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45821: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45822: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:45822: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46193: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46193: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46194: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46194: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46195: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46195: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46565: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46565: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46566: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46566: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46567: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46567: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46936: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46936: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46937: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46937: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46938: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:46938: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47294: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47294: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47295: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47295: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47296: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47296: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47652: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47652: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47653: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47653: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47654: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:47654: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48010: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48010: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48011: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48011: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48012: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48012: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48384: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48384: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48385: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48385: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48386: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48386: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48758: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48758: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48759: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48759: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48760: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:48760: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49116: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49116: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49117: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49117: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49118: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49118: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49474: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49474: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49475: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49475: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49476: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49476: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49832: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49832: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49833: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49833: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49834: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:49834: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50176: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50176: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50177: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50177: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50516: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50516: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50517: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50517: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50842: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50842: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50843: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:50843: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51168: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51168: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51169: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51169: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51494: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51494: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51495: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:51495: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52076: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52076: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52077: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52077: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52408: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52408: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52409: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52409: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52740: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52740: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52741: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:52741: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53129: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53129: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53130: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53130: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53131: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53131: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53522: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53522: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53523: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53523: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53524: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53524: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53907: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53907: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53908: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53908: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53909: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:53909: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54292: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54292: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54293: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54293: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54294: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54294: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54662: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54662: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54663: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54663: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54664: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:54664: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55032: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55032: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55033: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55033: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55034: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55034: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55402: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55402: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55403: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55403: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55404: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55404: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55769: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55769: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55770: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55770: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55771: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:55771: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56136: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56136: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56137: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56137: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56138: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56138: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56503: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56503: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56504: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56504: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56505: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56505: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56857: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56857: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56858: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:56858: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57207: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57207: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57208: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57208: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57549: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57549: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57550: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57550: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57883: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57883: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57884: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:57884: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58217: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58217: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58218: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58218: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58551: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58551: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58552: warning: Timing checks are not supported and delayed signal "GATE_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58552: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58877: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58877: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58878: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:58878: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62269: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62269: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62270: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62270: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62271: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62271: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62272: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62272: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62626: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62626: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62627: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62627: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62628: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62628: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62629: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:62629: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77991: warning: Timing checks are not supported and delayed signal "SLEEP_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77991: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77992: warning: Timing checks are not supported and delayed signal "SLEEP_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:77992: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135137: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135137: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135138: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135138: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135139: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135139: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135140: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135140: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135141: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135141: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135142: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135142: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135143: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135143: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135144: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135144: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135145: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135145: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135146: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135146: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135606: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135606: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135607: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135607: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135608: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135608: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135609: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135609: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135610: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135610: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135611: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135611: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135612: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135612: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135613: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135613: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135614: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135614: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135615: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:135615: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136067: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136067: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136068: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136068: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136069: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136069: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136070: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136070: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136071: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136071: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136072: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136072: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136073: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136073: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136074: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136074: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136075: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136075: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136076: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136076: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136498: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136498: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136499: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136499: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136500: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136500: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136501: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136501: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136502: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136502: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136503: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136503: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136504: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136504: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136925: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136925: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136926: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136926: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136927: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136927: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136928: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136928: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136929: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136929: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136930: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136930: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136931: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:136931: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137344: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137344: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137345: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137345: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137346: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137346: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137347: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137347: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137348: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137348: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137349: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137349: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137350: warning: Timing checks are not supported and delayed signal "CLK_N_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137350: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137755: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137755: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137756: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137756: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137757: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137757: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137758: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137758: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137759: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137759: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137760: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137760: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137761: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:137761: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138166: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138166: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138167: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138167: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138168: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138168: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138169: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138169: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138170: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138170: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138171: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138171: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138172: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138172: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138577: warning: Timing checks are not supported and delayed signal "RESET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138577: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138578: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138578: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138579: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138579: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138580: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138580: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138581: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138581: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138582: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138582: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138583: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:138583: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139004: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139004: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139005: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139005: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139006: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139006: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139007: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139007: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139008: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139008: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139009: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139009: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139010: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139010: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139431: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139431: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139432: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139432: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139433: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139433: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139434: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139434: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139435: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139435: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139436: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139436: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139437: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139437: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139842: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139842: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139843: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139843: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139844: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139844: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139845: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139845: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139846: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139846: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139847: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139847: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139848: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:139848: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140253: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140253: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140254: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140254: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140255: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140255: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140256: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140256: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140257: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140257: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140258: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140258: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140259: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140259: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140664: warning: Timing checks are not supported and delayed signal "SET_B_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140664: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140665: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140665: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140666: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140666: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140667: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140667: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140668: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140668: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140669: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140669: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140670: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:140670: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141054: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141054: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141055: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141055: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141056: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141056: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141057: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141057: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141058: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141058: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141059: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141059: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141442: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141442: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141443: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141443: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141444: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141444: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141445: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141445: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141446: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141446: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141447: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141447: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141816: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141816: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141817: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141817: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141818: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141818: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141819: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141819: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141820: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141820: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141821: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:141821: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142190: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142190: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142191: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142191: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142192: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142192: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142193: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142193: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142194: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142194: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142195: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142195: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142564: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142564: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142565: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142565: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142566: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142566: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142567: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142567: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142568: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142568: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142569: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142569: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142937: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142937: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142938: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142938: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142939: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142939: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142940: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:142940: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143307: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143307: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143308: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143308: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143309: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143309: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143310: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143310: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143677: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143677: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143678: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143678: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143679: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143679: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143680: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:143680: warning: Timing checks are not supported and delayed signal "GATE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144087: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144087: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144088: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144088: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144089: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144089: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144090: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144090: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144091: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144091: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144092: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144092: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144093: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144093: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144094: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144094: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144502: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144502: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144503: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144503: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144504: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144504: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144505: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144505: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144506: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144506: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144507: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144507: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144508: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144508: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144509: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144509: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144903: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144903: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144904: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144904: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144905: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144905: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144906: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144906: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144907: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144907: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144908: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144908: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144909: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144909: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144910: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:144910: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145304: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145304: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145305: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145305: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145306: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145306: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145307: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145307: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145308: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145308: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145309: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145309: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145310: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145310: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145311: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145311: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145705: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145705: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145706: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145706: warning: Timing checks are not supported and delayed signal "DE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145707: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145707: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145708: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145708: warning: Timing checks are not supported and delayed signal "D_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145709: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145709: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145710: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145710: warning: Timing checks are not supported and delayed signal "SCD_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145711: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145711: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145712: warning: Timing checks are not supported and delayed signal "CLK_delayed" will not be driven.
/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v:145712: warning: Timing checks are not supported and delayed signal "SCE_delayed" will not be driven.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_rca.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_rca.v:23: $finish called at 30011000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_rca.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[30011000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ yosys

 /----------------------------------------------------------------------------\
 |  yosys -- Yosys Open SYnthesis Suite                                       |
 |  Copyright (C) 2012 - 2025  Claire Xenia Wolf <claire@yosyshq.com>         |
 |  Distributed under an ISC-like license, type "license" to see terms        |
 \----------------------------------------------------------------------------/
 Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)

yosys> read_liberty -lib /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

1. Executing Liberty frontend: /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
Imported 428 cell types from liberty file.

yosys> read_verilog incomp_if.v
ERROR: File `incomp_if.v' not found or is a directory

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v

2. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v' to AST representation.
Generating RTLIL representation for module `\incomp_if'.
Successfully finished Verilog frontend.

yosys> synth -top incomp_if

3. Executing SYNTH pass.

3.1. Executing HIERARCHY pass (managing design hierarchy).

3.1.1. Analyzing design hierarchy..
Top module:  \incomp_if

3.1.2. Analyzing design hierarchy..
Top module:  \incomp_if
Removed 0 unused modules.

3.2. Executing PROC pass (convert processes to netlists).

3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed a total of 0 dead cases.

3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 0 assignments to connections.

3.2.4. Executing PROC_INIT pass (extract init attributes).

3.2.5. Executing PROC_ARST pass (detect async resets in processes).

3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\incomp_if.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v:2$1'.
     1/1: $0\y[0:0]

3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
Latch inferred for signal `\incomp_if.\y' from process `\incomp_if.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v:2$1': $auto$proc_dlatch.cc:432:proc_dlatch$14

3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\incomp_if.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v:2$1'.
Removing empty process `incomp_if.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if.v:2$1'.
Cleaned up 1 empty switch.

3.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.
<suppressed ~7 debug messages>

3.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..
Removed 1 unused cells and 8 unused wires.
<suppressed ~2 debug messages>

3.5. Executing CHECK pass (checking for obvious problems).
Checking module incomp_if...
Found and reported 0 problems.

3.6. Executing OPT pass (performing simple optimizations).

3.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if.
Performed a total of 0 changes.

3.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.6.6. Executing OPT_DFF pass (perform DFF optimizations).

3.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.6.9. Finished fast OPT passes. (There is nothing left to do.)

3.7. Executing FSM pass (extract and optimize FSM).

3.7.1. Executing FSM_DETECT pass (finding FSMs in design).

3.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

3.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

3.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

3.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

3.8. Executing OPT pass (performing simple optimizations).

3.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if.
Performed a total of 0 changes.

3.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.8.6. Executing OPT_DFF pass (perform DFF optimizations).

3.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.8.9. Finished fast OPT passes. (There is nothing left to do.)

3.9. Executing WREDUCE pass (reducing word size of cells).

3.10. Executing PEEPOPT pass (run peephole optimizers).

3.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module incomp_if:
  created 0 $alu and 0 $macc cells.

3.13. Executing SHARE pass (SAT-based resource sharing).

3.14. Executing OPT pass (performing simple optimizations).

3.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if.
Performed a total of 0 changes.

3.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.14.6. Executing OPT_DFF pass (perform DFF optimizations).

3.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.14.9. Finished fast OPT passes. (There is nothing left to do.)

3.15. Executing MEMORY pass.

3.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

3.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

3.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

3.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

3.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

3.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

3.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

3.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.17. Executing OPT pass (performing simple optimizations).

3.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.17.3. Executing OPT_DFF pass (perform DFF optimizations).

3.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.17.5. Finished fast OPT passes.

3.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

3.19. Executing OPT pass (performing simple optimizations).

3.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if.
Performed a total of 0 changes.

3.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.19.6. Executing OPT_SHARE pass.

3.19.7. Executing OPT_DFF pass (perform DFF optimizations).

3.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.19.10. Finished fast OPT passes. (There is nothing left to do.)

3.20. Executing TECHMAP pass (map to technology primitives).

3.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

3.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $dlatch.
No more expansions possible.
<suppressed ~78 debug messages>

3.21. Executing OPT pass (performing simple optimizations).

3.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.21.3. Executing OPT_DFF pass (perform DFF optimizations).

3.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.21.5. Finished fast OPT passes.

3.22. Executing ABC pass (technology mapping using ABC).

3.22.1. Extracting gate netlist of module `\incomp_if' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

3.22.1.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.
Removing global temp directory.

3.23. Executing OPT pass (performing simple optimizations).

3.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if.

3.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if'.
Removed a total of 0 cells.

3.23.3. Executing OPT_DFF pass (perform DFF optimizations).

3.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if..

3.23.5. Finished fast OPT passes.

3.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `incomp_if'. Setting top module to incomp_if.

3.24.1. Analyzing design hierarchy..
Top module:  \incomp_if

3.24.2. Analyzing design hierarchy..
Top module:  \incomp_if
Removed 0 unused modules.

3.25. Printing statistics.

=== incomp_if ===

        +----------Local Count, excluding submodules.
        | 
        4 wires
        4 wire bits
        4 public wires
        4 public wire bits
        4 ports
        4 port bits
        1 cells
        1   $_DLATCH_P_

3.26. Executing CHECK pass (checking for obvious problems).
Checking module incomp_if...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

4. Executing ABC pass (technology mapping using ABC).

4.1. Extracting gate netlist of module `\incomp_if' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

4.1.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr incomp_if_noattr_generated_netlist.v

5. Executing Verilog backend.

5.1. Executing BMUXMAP pass.

5.2. Executing DEMUXMAP pass.
Dumping module `\incomp_if'.

yosys> show

6. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module incomp_if to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v

7. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v' to AST representation.
Generating RTLIL representation for module `\incomp_if2'.
Successfully finished Verilog frontend.

yosys> synth -top incomp_if2

8. Executing SYNTH pass.

8.1. Executing HIERARCHY pass (managing design hierarchy).

8.1.1. Analyzing design hierarchy..
Top module:  \incomp_if2

8.1.2. Analyzing design hierarchy..
Top module:  \incomp_if2
Removing unused module `\incomp_if'.
Removed 1 unused modules.

8.2. Executing PROC pass (convert processes to netlists).

8.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

8.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v:3$95 in module incomp_if2.
Removed a total of 0 dead cases.

8.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 0 assignments to connections.

8.2.4. Executing PROC_INIT pass (extract init attributes).

8.2.5. Executing PROC_ARST pass (detect async resets in processes).

8.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~2 debug messages>

8.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\incomp_if2.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v:3$95'.
     1/1: $0\y[0:0]

8.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
Latch inferred for signal `\incomp_if2.\y' from process `\incomp_if2.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v:3$95': $auto$proc_dlatch.cc:432:proc_dlatch$119

8.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

8.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

8.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 2 empty switches in `\incomp_if2.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v:3$95'.
Removing empty process `incomp_if2.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_if2.v:3$95'.
Cleaned up 2 empty switches.

8.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.
<suppressed ~7 debug messages>

8.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..
Removed 1 unused cells and 10 unused wires.
<suppressed ~2 debug messages>

8.5. Executing CHECK pass (checking for obvious problems).
Checking module incomp_if2...
Found and reported 0 problems.

8.6. Executing OPT pass (performing simple optimizations).

8.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if2..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

8.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if2.
Performed a total of 0 changes.

8.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.6.6. Executing OPT_DFF pass (perform DFF optimizations).

8.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.6.9. Finished fast OPT passes. (There is nothing left to do.)

8.7. Executing FSM pass (extract and optimize FSM).

8.7.1. Executing FSM_DETECT pass (finding FSMs in design).

8.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

8.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

8.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

8.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

8.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

8.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

8.8. Executing OPT pass (performing simple optimizations).

8.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if2..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

8.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if2.
Performed a total of 0 changes.

8.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.8.6. Executing OPT_DFF pass (perform DFF optimizations).

8.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.8.9. Finished fast OPT passes. (There is nothing left to do.)

8.9. Executing WREDUCE pass (reducing word size of cells).

8.10. Executing PEEPOPT pass (run peephole optimizers).

8.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module incomp_if2:
  created 0 $alu and 0 $macc cells.

8.13. Executing SHARE pass (SAT-based resource sharing).

8.14. Executing OPT pass (performing simple optimizations).

8.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if2..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

8.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if2.
Performed a total of 0 changes.

8.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.14.6. Executing OPT_DFF pass (perform DFF optimizations).

8.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.14.9. Finished fast OPT passes. (There is nothing left to do.)

8.15. Executing MEMORY pass.

8.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

8.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

8.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

8.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

8.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

8.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

8.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

8.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

8.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.17. Executing OPT pass (performing simple optimizations).

8.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.17.3. Executing OPT_DFF pass (perform DFF optimizations).

8.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.17.5. Finished fast OPT passes.

8.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

8.19. Executing OPT pass (performing simple optimizations).

8.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_if2..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

8.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_if2.
Performed a total of 0 changes.

8.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.19.6. Executing OPT_SHARE pass.

8.19.7. Executing OPT_DFF pass (perform DFF optimizations).

8.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.19.10. Finished fast OPT passes. (There is nothing left to do.)

8.20. Executing TECHMAP pass (map to technology primitives).

8.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

8.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $not.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $dlatch.
No more expansions possible.
<suppressed ~82 debug messages>

8.21. Executing OPT pass (performing simple optimizations).

8.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.21.3. Executing OPT_DFF pass (perform DFF optimizations).

8.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..

8.21.5. Finished fast OPT passes.

8.22. Executing ABC pass (technology mapping using ABC).

8.22.1. Extracting gate netlist of module `\incomp_if2' to `<abc-temp-dir>/input.blif'..

8.22.1.1. Executed ABC.
Extracted 4 gates and 8 wires to a netlist network with 4 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-wkIzbH/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

8.22.1.2. Re-integrating ABC results.
ABC RESULTS:               MUX cells:        1
ABC RESULTS:               NOR cells:        1
ABC RESULTS:        internal signals:        2
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

8.23. Executing OPT pass (performing simple optimizations).

8.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_if2.

8.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_if2'.
Removed a total of 0 cells.

8.23.3. Executing OPT_DFF pass (perform DFF optimizations).

8.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_if2..
Removed 0 unused cells and 8 unused wires.
<suppressed ~1 debug messages>

8.23.5. Finished fast OPT passes.

8.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `incomp_if2'. Setting top module to incomp_if2.

8.24.1. Analyzing design hierarchy..
Top module:  \incomp_if2

8.24.2. Analyzing design hierarchy..
Top module:  \incomp_if2
Removed 0 unused modules.

8.25. Printing statistics.

=== incomp_if2 ===

        +----------Local Count, excluding submodules.
        | 
        7 wires
        7 wire bits
        5 public wires
        5 public wire bits
        5 ports
        5 port bits
        3 cells
        1   $_DLATCH_N_
        1   $_MUX_
        1   $_NOR_

8.26. Executing CHECK pass (checking for obvious problems).
Checking module incomp_if2...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

9. Executing ABC pass (technology mapping using ABC).

9.1. Extracting gate netlist of module `\incomp_if2' to `<abc-temp-dir>/input.blif'..

9.1.1. Executed ABC.
Extracted 2 gates and 6 wires to a netlist network with 4 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

9.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__mux2_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nor2_1 cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr incomp_if2_noattr_generated_netlist.v

10. Executing Verilog backend.

10.1. Executing BMUXMAP pass.

10.2. Executing DEMUXMAP pass.
Dumping module `\incomp_if2'.

yosys> show

11. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module incomp_if2 to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v

12. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v' to AST representation.
Generating RTLIL representation for module `\incomp_case'.
Successfully finished Verilog frontend.

yosys> synth -top incomp_case

13. Executing SYNTH pass.

13.1. Executing HIERARCHY pass (managing design hierarchy).

13.1.1. Analyzing design hierarchy..
Top module:  \incomp_case

13.1.2. Analyzing design hierarchy..
Top module:  \incomp_case
Removing unused module `\incomp_if2'.
Removed 1 unused modules.

13.2. Executing PROC pass (convert processes to netlists).

13.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

13.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v:3$208 in module incomp_case.
Removed a total of 0 dead cases.

13.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 1 assignment to connection.

13.2.4. Executing PROC_INIT pass (extract init attributes).

13.2.5. Executing PROC_ARST pass (detect async resets in processes).

13.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

13.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\incomp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v:3$208'.
     1/1: $1\y[0:0]

13.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
Latch inferred for signal `\incomp_case.\y' from process `\incomp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v:3$208': $auto$proc_dlatch.cc:432:proc_dlatch$229

13.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

13.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

13.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\incomp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v:3$208'.
Removing empty process `incomp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/incomp_case.v:3$208'.
Cleaned up 1 empty switch.

13.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.
<suppressed ~6 debug messages>

13.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..
Removed 1 unused cells and 7 unused wires.
<suppressed ~2 debug messages>

13.5. Executing CHECK pass (checking for obvious problems).
Checking module incomp_case...
Found and reported 0 problems.

13.6. Executing OPT pass (performing simple optimizations).

13.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

13.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_case.
    New ctrl vector for $pmux cell $procmux$210: $procmux$211_CMP
  Optimizing cells in module \incomp_case.
Performed a total of 1 changes.

13.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.6.6. Executing OPT_DFF pass (perform DFF optimizations).

13.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.6.9. Rerunning OPT passes. (Maybe there is more to do..)

13.6.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

13.6.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_case.
Performed a total of 0 changes.

13.6.12. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.6.13. Executing OPT_DFF pass (perform DFF optimizations).

13.6.14. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.6.15. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.6.16. Finished fast OPT passes. (There is nothing left to do.)

13.7. Executing FSM pass (extract and optimize FSM).

13.7.1. Executing FSM_DETECT pass (finding FSMs in design).

13.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

13.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

13.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

13.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

13.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

13.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

13.8. Executing OPT pass (performing simple optimizations).

13.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

13.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_case.
Performed a total of 0 changes.

13.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.8.6. Executing OPT_DFF pass (perform DFF optimizations).

13.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.8.9. Finished fast OPT passes. (There is nothing left to do.)

13.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 2) from port B of cell incomp_case.$procmux$211_CMP0 ($eq).

13.10. Executing PEEPOPT pass (run peephole optimizers).

13.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module incomp_case:
  created 0 $alu and 0 $macc cells.

13.13. Executing SHARE pass (SAT-based resource sharing).

13.14. Executing OPT pass (performing simple optimizations).

13.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

13.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_case.
Performed a total of 0 changes.

13.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.14.6. Executing OPT_DFF pass (perform DFF optimizations).

13.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.14.9. Finished fast OPT passes. (There is nothing left to do.)

13.15. Executing MEMORY pass.

13.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

13.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

13.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

13.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

13.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

13.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

13.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

13.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

13.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.17. Executing OPT pass (performing simple optimizations).

13.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.17.3. Executing OPT_DFF pass (perform DFF optimizations).

13.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.17.5. Finished fast OPT passes.

13.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

13.19. Executing OPT pass (performing simple optimizations).

13.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \incomp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

13.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \incomp_case.
Performed a total of 0 changes.

13.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.19.6. Executing OPT_SHARE pass.

13.19.7. Executing OPT_DFF pass (perform DFF optimizations).

13.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..

13.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.19.10. Finished fast OPT passes. (There is nothing left to do.)

13.20. Executing TECHMAP pass (map to technology primitives).

13.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

13.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $not.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $dlatch.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $logic_not.
No more expansions possible.
<suppressed ~84 debug messages>

13.21. Executing OPT pass (performing simple optimizations).

13.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.
<suppressed ~5 debug messages>

13.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.21.3. Executing OPT_DFF pass (perform DFF optimizations).

13.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..
Removed 2 unused cells and 6 unused wires.
<suppressed ~3 debug messages>

13.21.5. Finished fast OPT passes.

13.22. Executing ABC pass (technology mapping using ABC).

13.22.1. Extracting gate netlist of module `\incomp_case' to `<abc-temp-dir>/input.blif'..

13.22.1.1. Executed ABC.
Extracted 5 gates and 9 wires to a netlist network with 4 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-wTc5YQ/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

13.22.1.2. Re-integrating ABC results.
ABC RESULTS:            ANDNOT cells:        1
ABC RESULTS:               MUX cells:        1
ABC RESULTS:               NOR cells:        1
ABC RESULTS:             ORNOT cells:        1
ABC RESULTS:        internal signals:        3
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

13.23. Executing OPT pass (performing simple optimizations).

13.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module incomp_case.

13.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\incomp_case'.
Removed a total of 0 cells.

13.23.3. Executing OPT_DFF pass (perform DFF optimizations).

13.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \incomp_case..
Removed 0 unused cells and 9 unused wires.
<suppressed ~1 debug messages>

13.23.5. Finished fast OPT passes.

13.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `incomp_case'. Setting top module to incomp_case.

13.24.1. Analyzing design hierarchy..
Top module:  \incomp_case

13.24.2. Analyzing design hierarchy..
Top module:  \incomp_case
Removed 0 unused modules.

13.25. Printing statistics.

=== incomp_case ===

        +----------Local Count, excluding submodules.
        | 
        9 wires
       10 wire bits
        5 public wires
        6 public wire bits
        5 ports
        6 port bits
        5 cells
        1   $_ANDNOT_
        1   $_DLATCH_N_
        1   $_MUX_
        1   $_NOR_
        1   $_ORNOT_

13.26. Executing CHECK pass (checking for obvious problems).
Checking module incomp_case...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

14. Executing ABC pass (technology mapping using ABC).

14.1. Extracting gate netlist of module `\incomp_case' to `<abc-temp-dir>/input.blif'..

14.1.1. Executed ABC.
Extracted 4 gates and 8 wires to a netlist network with 4 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

14.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__buf_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__mux2_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nand2b_1 cells:        1
ABC RESULTS:        internal signals:        2
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr incomp_case_noattr_generated_netlist.v

15. Executing Verilog backend.

15.1. Executing BMUXMAP pass.

15.2. Executing DEMUXMAP pass.
Dumping module `\incomp_case'.

yosys> show

16. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module incomp_case to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v

17. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v' to AST representation.
/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:8: Warning: Yosys has only limited support for tri-state logic at the moment.
Generating RTLIL representation for module `\bad_case'.
Successfully finished Verilog frontend.

yosys> synth -top bad_case

18. Executing SYNTH pass.

18.1. Executing HIERARCHY pass (managing design hierarchy).

18.1.1. Analyzing design hierarchy..
Top module:  \bad_case

18.1.2. Analyzing design hierarchy..
Top module:  \bad_case
Removing unused module `\incomp_case'.
Removed 1 unused modules.

18.2. Executing PROC pass (convert processes to netlists).

18.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

18.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed 1 dead cases from process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336 in module bad_case.
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336 in module bad_case.
Removed a total of 1 dead cases.

18.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 1 assignment to connection.

18.2.4. Executing PROC_INIT pass (extract init attributes).

18.2.5. Executing PROC_ARST pass (detect async resets in processes).

18.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

18.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\bad_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336'.
     1/1: $1\y[0:0]

18.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\bad_case.\y' from process `\bad_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336'.

18.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

18.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

18.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\bad_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336'.
Removing empty process `bad_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/bad_case.v:2$336'.
Cleaned up 1 empty switch.

18.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.
<suppressed ~1 debug messages>

18.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..
Removed 0 unused cells and 3 unused wires.
<suppressed ~1 debug messages>

18.5. Executing CHECK pass (checking for obvious problems).
Checking module bad_case...
Found and reported 0 problems.

18.6. Executing OPT pass (performing simple optimizations).

18.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \bad_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~3 debug messages>

18.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \bad_case.
Performed a total of 0 changes.

18.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.6.6. Executing OPT_DFF pass (perform DFF optimizations).

18.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.6.9. Finished fast OPT passes. (There is nothing left to do.)

18.7. Executing FSM pass (extract and optimize FSM).

18.7.1. Executing FSM_DETECT pass (finding FSMs in design).

18.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

18.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

18.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

18.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

18.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

18.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

18.8. Executing OPT pass (performing simple optimizations).

18.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \bad_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~3 debug messages>

18.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \bad_case.
Performed a total of 0 changes.

18.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.8.6. Executing OPT_DFF pass (perform DFF optimizations).

18.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.8.9. Finished fast OPT passes. (There is nothing left to do.)

18.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 2) from port B of cell bad_case.$procmux$341_CMP0 ($eq).

18.10. Executing PEEPOPT pass (run peephole optimizers).

18.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module bad_case:
  created 0 $alu and 0 $macc cells.

18.13. Executing SHARE pass (SAT-based resource sharing).

18.14. Executing OPT pass (performing simple optimizations).

18.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \bad_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~3 debug messages>

18.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \bad_case.
Performed a total of 0 changes.

18.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.14.6. Executing OPT_DFF pass (perform DFF optimizations).

18.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.14.9. Finished fast OPT passes. (There is nothing left to do.)

18.15. Executing MEMORY pass.

18.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

18.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

18.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

18.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

18.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

18.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

18.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

18.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

18.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.17. Executing OPT pass (performing simple optimizations).

18.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.
<suppressed ~1 debug messages>

18.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.17.3. Executing OPT_DFF pass (perform DFF optimizations).

18.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..
Removed 1 unused cells and 2 unused wires.
<suppressed ~2 debug messages>

18.17.5. Finished fast OPT passes.

18.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

18.19. Executing OPT pass (performing simple optimizations).

18.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \bad_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

18.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \bad_case.
Performed a total of 0 changes.

18.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.19.6. Executing OPT_SHARE pass.

18.19.7. Executing OPT_DFF pass (perform DFF optimizations).

18.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..

18.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.19.10. Finished fast OPT passes. (There is nothing left to do.)

18.20. Executing TECHMAP pass (map to technology primitives).

18.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

18.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $logic_not.
Using extmapper simplemap for cells of type $eq.
Using template $paramod$d629d85c8826a74239b9178d1930215a43b0ceb0\_90_pmux for cells of type $pmux.
Using extmapper simplemap for cells of type $reduce_or.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $mux.
No more expansions possible.
<suppressed ~100 debug messages>

18.21. Executing OPT pass (performing simple optimizations).

18.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.
<suppressed ~4 debug messages>

18.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.21.3. Executing OPT_DFF pass (perform DFF optimizations).

18.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..
Removed 0 unused cells and 18 unused wires.
<suppressed ~1 debug messages>

18.21.5. Finished fast OPT passes.

18.22. Executing ABC pass (technology mapping using ABC).

18.22.1. Extracting gate netlist of module `\bad_case' to `<abc-temp-dir>/input.blif'..

18.22.1.1. Executed ABC.
Extracted 16 gates and 22 wires to a netlist network with 6 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-l78Ebw/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

18.22.1.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:            ANDNOT cells:        3
ABC RESULTS:               MUX cells:        1
ABC RESULTS:                OR cells:        3
ABC RESULTS:             ORNOT cells:        2
ABC RESULTS:        internal signals:       15
ABC RESULTS:           input signals:        6
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

18.23. Executing OPT pass (performing simple optimizations).

18.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module bad_case.

18.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\bad_case'.
Removed a total of 0 cells.

18.23.3. Executing OPT_DFF pass (perform DFF optimizations).

18.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \bad_case..
Removed 0 unused cells and 18 unused wires.
<suppressed ~1 debug messages>

18.23.5. Finished fast OPT passes.

18.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `bad_case'. Setting top module to bad_case.

18.24.1. Analyzing design hierarchy..
Top module:  \bad_case

18.24.2. Analyzing design hierarchy..
Top module:  \bad_case
Removed 0 unused modules.

18.25. Printing statistics.

=== bad_case ===

        +----------Local Count, excluding submodules.
        | 
       15 wires
       16 wire bits
        6 public wires
        7 public wire bits
        6 ports
        7 port bits
       10 cells
        3   $_ANDNOT_
        1   $_AND_
        1   $_MUX_
        2   $_ORNOT_
        3   $_OR_

18.26. Executing CHECK pass (checking for obvious problems).
Checking module bad_case...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

19. Executing ABC pass (technology mapping using ABC).

19.1. Extracting gate netlist of module `\bad_case' to `<abc-temp-dir>/input.blif'..

19.1.1. Executed ABC.
Extracted 10 gates and 16 wires to a netlist network with 6 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

19.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__mux4_2 cells:        1
ABC RESULTS:        internal signals:        9
ABC RESULTS:           input signals:        6
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr bad_case_noattr_generated_netlist.v

20. Executing Verilog backend.

20.1. Executing BMUXMAP pass.

20.2. Executing DEMUXMAP pass.
Dumping module `\bad_case'.

yosys> show

21. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module bad_case to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v

22. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v' to AST representation.
Generating RTLIL representation for module `\comp_case'.
Successfully finished Verilog frontend.

yosys> synth -top comp_case

23. Executing SYNTH pass.

23.1. Executing HIERARCHY pass (managing design hierarchy).

23.1.1. Analyzing design hierarchy..
Top module:  \comp_case

23.1.2. Analyzing design hierarchy..
Top module:  \comp_case
Removing unused module `\bad_case'.
Removed 1 unused modules.

23.2. Executing PROC pass (convert processes to netlists).

23.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

23.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v:4$478 in module comp_case.
Removed a total of 0 dead cases.

23.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 1 assignment to connection.

23.2.4. Executing PROC_INIT pass (extract init attributes).

23.2.5. Executing PROC_ARST pass (detect async resets in processes).

23.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

23.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\comp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v:4$478'.
     1/1: $1\y[0:0]

23.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\comp_case.\y' from process `\comp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v:4$478'.

23.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

23.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

23.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\comp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v:4$478'.
Removing empty process `comp_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/comp_case.v:4$478'.
Cleaned up 1 empty switch.

23.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.
<suppressed ~1 debug messages>

23.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..
Removed 0 unused cells and 3 unused wires.
<suppressed ~1 debug messages>

23.5. Executing CHECK pass (checking for obvious problems).
Checking module comp_case...
Found and reported 0 problems.

23.6. Executing OPT pass (performing simple optimizations).

23.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \comp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

23.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \comp_case.
Performed a total of 0 changes.

23.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.6.6. Executing OPT_DFF pass (perform DFF optimizations).

23.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.6.9. Finished fast OPT passes. (There is nothing left to do.)

23.7. Executing FSM pass (extract and optimize FSM).

23.7.1. Executing FSM_DETECT pass (finding FSMs in design).

23.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

23.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

23.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

23.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

23.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

23.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

23.8. Executing OPT pass (performing simple optimizations).

23.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \comp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

23.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \comp_case.
Performed a total of 0 changes.

23.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.8.6. Executing OPT_DFF pass (perform DFF optimizations).

23.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.8.9. Finished fast OPT passes. (There is nothing left to do.)

23.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 2) from port B of cell comp_case.$procmux$481_CMP0 ($eq).

23.10. Executing PEEPOPT pass (run peephole optimizers).

23.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module comp_case:
  created 0 $alu and 0 $macc cells.

23.13. Executing SHARE pass (SAT-based resource sharing).

23.14. Executing OPT pass (performing simple optimizations).

23.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \comp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

23.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \comp_case.
Performed a total of 0 changes.

23.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.14.6. Executing OPT_DFF pass (perform DFF optimizations).

23.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.14.9. Finished fast OPT passes. (There is nothing left to do.)

23.15. Executing MEMORY pass.

23.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

23.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

23.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

23.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

23.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

23.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

23.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

23.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

23.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.17. Executing OPT pass (performing simple optimizations).

23.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.17.3. Executing OPT_DFF pass (perform DFF optimizations).

23.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.17.5. Finished fast OPT passes.

23.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

23.19. Executing OPT pass (performing simple optimizations).

23.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \comp_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

23.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \comp_case.
Performed a total of 0 changes.

23.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.19.6. Executing OPT_SHARE pass.

23.19.7. Executing OPT_DFF pass (perform DFF optimizations).

23.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..

23.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.19.10. Finished fast OPT passes. (There is nothing left to do.)

23.20. Executing TECHMAP pass (map to technology primitives).

23.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

23.20.2. Continuing TECHMAP pass.
Using template $paramod$c5c783b17ab1d780abfad8cfe6563a0a7b47a3b0\_90_pmux for cells of type $pmux.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $logic_not.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $reduce_or.
Using extmapper simplemap for cells of type $mux.
No more expansions possible.
<suppressed ~98 debug messages>

23.21. Executing OPT pass (performing simple optimizations).

23.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.
<suppressed ~2 debug messages>

23.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.21.3. Executing OPT_DFF pass (perform DFF optimizations).

23.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..
Removed 0 unused cells and 14 unused wires.
<suppressed ~1 debug messages>

23.21.5. Finished fast OPT passes.

23.22. Executing ABC pass (technology mapping using ABC).

23.22.1. Extracting gate netlist of module `\comp_case' to `<abc-temp-dir>/input.blif'..

23.22.1.1. Executed ABC.
Extracted 10 gates and 15 wires to a netlist network with 5 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-F93lcm/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

23.22.1.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:            ANDNOT cells:        2
ABC RESULTS:               MUX cells:        1
ABC RESULTS:                OR cells:        2
ABC RESULTS:             ORNOT cells:        1
ABC RESULTS:        internal signals:        9
ABC RESULTS:           input signals:        5
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

23.23. Executing OPT pass (performing simple optimizations).

23.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module comp_case.

23.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\comp_case'.
Removed a total of 0 cells.

23.23.3. Executing OPT_DFF pass (perform DFF optimizations).

23.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \comp_case..
Removed 0 unused cells and 13 unused wires.
<suppressed ~1 debug messages>

23.23.5. Finished fast OPT passes.

23.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `comp_case'. Setting top module to comp_case.

23.24.1. Analyzing design hierarchy..
Top module:  \comp_case

23.24.2. Analyzing design hierarchy..
Top module:  \comp_case
Removed 0 unused modules.

23.25. Printing statistics.

=== comp_case ===

        +----------Local Count, excluding submodules.
        | 
       11 wires
       12 wire bits
        5 public wires
        6 public wire bits
        5 ports
        6 port bits
        7 cells
        2   $_ANDNOT_
        1   $_AND_
        1   $_MUX_
        1   $_ORNOT_
        2   $_OR_

23.26. Executing CHECK pass (checking for obvious problems).
Checking module comp_case...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

24. Executing ABC pass (technology mapping using ABC).

24.1. Extracting gate netlist of module `\comp_case' to `<abc-temp-dir>/input.blif'..

24.1.1. Executed ABC.
Extracted 7 gates and 12 wires to a netlist network with 5 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

24.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__mux2i_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nand2_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__o21ai_0 cells:        1
ABC RESULTS:        internal signals:        6
ABC RESULTS:           input signals:        5
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr comp_case_noattr_generated_netlist.v

25. Executing Verilog backend.

25.1. Executing BMUXMAP pass.

25.2. Executing DEMUXMAP pass.
Dumping module `\comp_case'.

yosys> show

26. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module comp_case to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v

27. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v' to AST representation.
Generating RTLIL representation for module `\demux_case'.
Successfully finished Verilog frontend.

yosys> synth -top demux_case

28. Executing SYNTH pass.

28.1. Executing HIERARCHY pass (managing design hierarchy).

28.1.1. Analyzing design hierarchy..
Top module:  \demux_case

28.1.2. Analyzing design hierarchy..
Top module:  \demux_case
Removing unused module `\comp_case'.
Removed 1 unused modules.

28.2. Executing PROC pass (convert processes to netlists).

28.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

28.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed 1 dead cases from process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599 in module demux_case.
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599 in module demux_case.
Removed a total of 1 dead cases.

28.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 1 assignment to connection.

28.2.4. Executing PROC_INIT pass (extract init attributes).

28.2.5. Executing PROC_ARST pass (detect async resets in processes).

28.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

28.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\demux_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599'.
     1/8: $1\y_int[7:0] [6]
     2/8: $1\y_int[7:0] [5]
     3/8: $1\y_int[7:0] [3]
     4/8: $1\y_int[7:0] [1]
     5/8: $1\y_int[7:0] [7]
     6/8: $1\y_int[7:0] [2]
     7/8: $1\y_int[7:0] [4]
     8/8: $1\y_int[7:0] [0]

28.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\demux_case.\y_int' from process `\demux_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599'.

28.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

28.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

28.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\demux_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599'.
Removing empty process `demux_case.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_case.v:5$599'.
Cleaned up 1 empty switch.

28.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.
<suppressed ~8 debug messages>

28.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..
Removed 0 unused cells and 11 unused wires.
<suppressed ~2 debug messages>

28.5. Executing CHECK pass (checking for obvious problems).
Checking module demux_case...
Found and reported 0 problems.

28.6. Executing OPT pass (performing simple optimizations).

28.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
<suppressed ~168 debug messages>
Removed a total of 56 cells.

28.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

28.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_case.
    New ctrl vector for $pmux cell $procmux$618: { $procmux$605_CMP $auto$opt_reduce.cc:137:opt_pmux$673 }
    New ctrl vector for $pmux cell $procmux$645: { $procmux$606_CMP $auto$opt_reduce.cc:137:opt_pmux$675 }
    New ctrl vector for $pmux cell $procmux$609: { $procmux$603_CMP $auto$opt_reduce.cc:137:opt_pmux$677 }
    New ctrl vector for $pmux cell $procmux$600: { $procmux$602_CMP $auto$opt_reduce.cc:137:opt_pmux$679 }
    New ctrl vector for $pmux cell $procmux$663: { $procmux$608_CMP $auto$opt_reduce.cc:137:opt_pmux$681 }
    New ctrl vector for $pmux cell $procmux$636: { $auto$opt_reduce.cc:137:opt_pmux$683 $procmux$601_CMP }
    New ctrl vector for $pmux cell $procmux$654: { $procmux$604_CMP $auto$opt_reduce.cc:137:opt_pmux$685 }
    New ctrl vector for $pmux cell $procmux$627: { $procmux$607_CMP $auto$opt_reduce.cc:137:opt_pmux$687 }
  Optimizing cells in module \demux_case.
Performed a total of 8 changes.

28.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.6.6. Executing OPT_DFF pass (perform DFF optimizations).

28.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..
Removed 0 unused cells and 56 unused wires.
<suppressed ~1 debug messages>

28.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.6.9. Rerunning OPT passes. (Maybe there is more to do..)

28.6.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

28.6.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_case.
Performed a total of 0 changes.

28.6.12. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.6.13. Executing OPT_DFF pass (perform DFF optimizations).

28.6.14. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.6.15. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.6.16. Finished fast OPT passes. (There is nothing left to do.)

28.7. Executing FSM pass (extract and optimize FSM).

28.7.1. Executing FSM_DETECT pass (finding FSMs in design).

28.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

28.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

28.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

28.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

28.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

28.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

28.8. Executing OPT pass (performing simple optimizations).

28.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

28.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_case.
Performed a total of 0 changes.

28.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.8.6. Executing OPT_DFF pass (perform DFF optimizations).

28.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.8.9. Finished fast OPT passes. (There is nothing left to do.)

28.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 2 bits (of 3) from port B of cell demux_case.$procmux$607_CMP0 ($eq).
Removed top 1 bits (of 3) from port B of cell demux_case.$procmux$606_CMP0 ($eq).
Removed top 1 bits (of 3) from port B of cell demux_case.$procmux$605_CMP0 ($eq).

28.10. Executing PEEPOPT pass (run peephole optimizers).

28.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module demux_case:
  created 0 $alu and 0 $macc cells.

28.13. Executing SHARE pass (SAT-based resource sharing).

28.14. Executing OPT pass (performing simple optimizations).

28.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

28.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_case.
Performed a total of 0 changes.

28.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.14.6. Executing OPT_DFF pass (perform DFF optimizations).

28.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.14.9. Finished fast OPT passes. (There is nothing left to do.)

28.15. Executing MEMORY pass.

28.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

28.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

28.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

28.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

28.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

28.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

28.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

28.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

28.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.17. Executing OPT pass (performing simple optimizations).

28.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.
<suppressed ~9 debug messages>

28.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.17.3. Executing OPT_DFF pass (perform DFF optimizations).

28.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..
Removed 1 unused cells and 1 unused wires.
<suppressed ~2 debug messages>

28.17.5. Finished fast OPT passes.

28.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

28.19. Executing OPT pass (performing simple optimizations).

28.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_case..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~14 debug messages>

28.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_case.
Performed a total of 0 changes.

28.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.19.6. Executing OPT_SHARE pass.

28.19.7. Executing OPT_DFF pass (perform DFF optimizations).

28.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..

28.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.

28.19.10. Finished fast OPT passes. (There is nothing left to do.)

28.20. Executing TECHMAP pass (map to technology primitives).

28.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

28.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $logic_not.
Using extmapper simplemap for cells of type $reduce_or.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $and.
No more expansions possible.
<suppressed ~100 debug messages>

28.21. Executing OPT pass (performing simple optimizations).

28.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.
<suppressed ~21 debug messages>

28.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
<suppressed ~96 debug messages>
Removed a total of 32 cells.

28.21.3. Executing OPT_DFF pass (perform DFF optimizations).

28.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..
Removed 0 unused cells and 38 unused wires.
<suppressed ~1 debug messages>

28.21.5. Finished fast OPT passes.

28.22. Executing ABC pass (technology mapping using ABC).

28.22.1. Extracting gate netlist of module `\demux_case' to `<abc-temp-dir>/input.blif'..

28.22.1.1. Executed ABC.
Extracted 54 gates and 59 wires to a netlist network with 4 inputs and 8 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-zS4pOs/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

28.22.1.2. Re-integrating ABC results.
ABC RESULTS:            ANDNOT cells:       17
ABC RESULTS:               MUX cells:        2
ABC RESULTS:              NAND cells:        1
ABC RESULTS:               NOT cells:        2
ABC RESULTS:                OR cells:       18
ABC RESULTS:             ORNOT cells:        2
ABC RESULTS:        internal signals:       47
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        8
Removing temp directory.
Removing global temp directory.

28.23. Executing OPT pass (performing simple optimizations).

28.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_case.
<suppressed ~1 debug messages>

28.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_case'.
Removed a total of 0 cells.

28.23.3. Executing OPT_DFF pass (perform DFF optimizations).

28.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_case..
Removed 0 unused cells and 52 unused wires.
<suppressed ~1 debug messages>

28.23.5. Finished fast OPT passes.

28.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `demux_case'. Setting top module to demux_case.

28.24.1. Analyzing design hierarchy..
Top module:  \demux_case

28.24.2. Analyzing design hierarchy..
Top module:  \demux_case
Removed 0 unused modules.

28.25. Printing statistics.

=== demux_case ===

        +----------Local Count, excluding submodules.
        | 
       45 wires
       54 wire bits
       11 public wires
       20 public wire bits
       10 ports
       12 port bits
       42 cells
       17   $_ANDNOT_
        2   $_MUX_
        1   $_NAND_
        2   $_NOT_
        2   $_ORNOT_
       18   $_OR_

28.26. Executing CHECK pass (checking for obvious problems).
Checking module demux_case...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

29. Executing ABC pass (technology mapping using ABC).

29.1. Extracting gate netlist of module `\demux_case' to `<abc-temp-dir>/input.blif'..

29.1.1. Executed ABC.
Extracted 42 gates and 46 wires to a netlist network with 4 inputs and 8 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

29.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__and4_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__and4b_1 cells:        3
ABC RESULTS:   sky130_fd_sc_hd__nor4b_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nor4bb_1 cells:        3
ABC RESULTS:        internal signals:       34
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        8
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr demux_case_noattr_generated_netlist.v

30. Executing Verilog backend.

30.1. Executing BMUXMAP pass.

30.2. Executing DEMUXMAP pass.
Dumping module `\demux_case'.

yosys> show

31. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module demux_case to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v

32. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v' to AST representation.
Generating RTLIL representation for module `\partial_case_assign'.
Successfully finished Verilog frontend.

yosys> synth -top partial_case_assign

33. Executing SYNTH pass.

33.1. Executing HIERARCHY pass (managing design hierarchy).

33.1.1. Analyzing design hierarchy..
Top module:  \partial_case_assign

33.1.2. Analyzing design hierarchy..
Top module:  \partial_case_assign
Removing unused module `\demux_case'.
Removed 1 unused modules.

33.2. Executing PROC pass (convert processes to netlists).

33.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

33.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 1 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008 in module partial_case_assign.
Removed a total of 0 dead cases.

33.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 2 assignments to connections.

33.2.4. Executing PROC_INIT pass (extract init attributes).

33.2.5. Executing PROC_ARST pass (detect async resets in processes).

33.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

33.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\partial_case_assign.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008'.
     1/2: $1\x[0:0]
     2/2: $1\y[0:0]

33.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\partial_case_assign.\y' from process `\partial_case_assign.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008'.
Latch inferred for signal `\partial_case_assign.\x' from process `\partial_case_assign.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008': $auto$proc_dlatch.cc:432:proc_dlatch$1025

33.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

33.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

33.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\partial_case_assign.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008'.
Removing empty process `partial_case_assign.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/partial_case_assign.v:2$1008'.
Cleaned up 1 empty switch.

33.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.
<suppressed ~6 debug messages>

33.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..
Removed 1 unused cells and 9 unused wires.
<suppressed ~2 debug messages>

33.5. Executing CHECK pass (checking for obvious problems).
Checking module partial_case_assign...
Found and reported 0 problems.

33.6. Executing OPT pass (performing simple optimizations).

33.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
<suppressed ~6 debug messages>
Removed a total of 2 cells.

33.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \partial_case_assign..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

33.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \partial_case_assign.
Performed a total of 0 changes.

33.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.6.6. Executing OPT_DFF pass (perform DFF optimizations).

33.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..
Removed 0 unused cells and 2 unused wires.
<suppressed ~1 debug messages>

33.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.6.9. Rerunning OPT passes. (Maybe there is more to do..)

33.6.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \partial_case_assign..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

33.6.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \partial_case_assign.
Performed a total of 0 changes.

33.6.12. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.6.13. Executing OPT_DFF pass (perform DFF optimizations).

33.6.14. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.6.15. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.6.16. Finished fast OPT passes. (There is nothing left to do.)

33.7. Executing FSM pass (extract and optimize FSM).

33.7.1. Executing FSM_DETECT pass (finding FSMs in design).

33.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

33.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

33.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

33.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

33.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

33.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

33.8. Executing OPT pass (performing simple optimizations).

33.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \partial_case_assign..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

33.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \partial_case_assign.
Performed a total of 0 changes.

33.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.8.6. Executing OPT_DFF pass (perform DFF optimizations).

33.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.8.9. Finished fast OPT passes. (There is nothing left to do.)

33.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 2) from port B of cell partial_case_assign.$procmux$1011_CMP0 ($eq).

33.10. Executing PEEPOPT pass (run peephole optimizers).

33.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module partial_case_assign:
  created 0 $alu and 0 $macc cells.

33.13. Executing SHARE pass (SAT-based resource sharing).

33.14. Executing OPT pass (performing simple optimizations).

33.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \partial_case_assign..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

33.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \partial_case_assign.
Performed a total of 0 changes.

33.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.14.6. Executing OPT_DFF pass (perform DFF optimizations).

33.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.14.9. Finished fast OPT passes. (There is nothing left to do.)

33.15. Executing MEMORY pass.

33.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

33.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

33.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

33.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

33.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

33.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

33.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

33.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

33.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.17. Executing OPT pass (performing simple optimizations).

33.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.17.3. Executing OPT_DFF pass (perform DFF optimizations).

33.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.17.5. Finished fast OPT passes.

33.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

33.19. Executing OPT pass (performing simple optimizations).

33.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \partial_case_assign..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

33.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \partial_case_assign.
Performed a total of 0 changes.

33.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.19.6. Executing OPT_SHARE pass.

33.19.7. Executing OPT_DFF pass (perform DFF optimizations).

33.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..

33.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.19.10. Finished fast OPT passes. (There is nothing left to do.)

33.20. Executing TECHMAP pass (map to technology primitives).

33.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

33.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $logic_not.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $dlatch.
Using template $paramod$c5c783b17ab1d780abfad8cfe6563a0a7b47a3b0\_90_pmux for cells of type $pmux.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $reduce_or.
No more expansions possible.
<suppressed ~100 debug messages>

33.21. Executing OPT pass (performing simple optimizations).

33.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.
<suppressed ~4 debug messages>

33.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.21.3. Executing OPT_DFF pass (perform DFF optimizations).

33.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..
Removed 0 unused cells and 14 unused wires.
<suppressed ~1 debug messages>

33.21.5. Finished fast OPT passes.

33.22. Executing ABC pass (technology mapping using ABC).

33.22.1. Extracting gate netlist of module `\partial_case_assign' to `<abc-temp-dir>/input.blif'..

33.22.1.1. Executed ABC.
Extracted 11 gates and 16 wires to a netlist network with 5 inputs and 3 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-ZAcJGx/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

33.22.1.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:            ANDNOT cells:        2
ABC RESULTS:               MUX cells:        2
ABC RESULTS:               NOR cells:        1
ABC RESULTS:                OR cells:        1
ABC RESULTS:             ORNOT cells:        1
ABC RESULTS:        internal signals:        8
ABC RESULTS:           input signals:        5
ABC RESULTS:          output signals:        3
Removing temp directory.
Removing global temp directory.

33.23. Executing OPT pass (performing simple optimizations).

33.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module partial_case_assign.

33.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\partial_case_assign'.
Removed a total of 0 cells.

33.23.3. Executing OPT_DFF pass (perform DFF optimizations).

33.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \partial_case_assign..
Removed 0 unused cells and 14 unused wires.
<suppressed ~1 debug messages>

33.23.5. Finished fast OPT passes.

33.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `partial_case_assign'. Setting top module to partial_case_assign.

33.24.1. Analyzing design hierarchy..
Top module:  \partial_case_assign

33.24.2. Analyzing design hierarchy..
Top module:  \partial_case_assign
Removed 0 unused modules.

33.25. Printing statistics.

=== partial_case_assign ===

        +----------Local Count, excluding submodules.
        | 
       13 wires
       14 wire bits
        6 public wires
        7 public wire bits
        6 ports
        7 port bits
        9 cells
        2   $_ANDNOT_
        1   $_AND_
        1   $_DLATCH_P_
        2   $_MUX_
        1   $_NOR_
        1   $_ORNOT_
        1   $_OR_

33.26. Executing CHECK pass (checking for obvious problems).
Checking module partial_case_assign...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

34. Executing ABC pass (technology mapping using ABC).

34.1. Extracting gate netlist of module `\partial_case_assign' to `<abc-temp-dir>/input.blif'..

34.1.1. Executed ABC.
Extracted 8 gates and 13 wires to a netlist network with 5 inputs and 3 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.09 sec
ABC: Memory =   19.85 MB. Time =     0.09 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

34.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__a221o_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__and3b_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__mux2_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nand2b_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nor2_1 cells:        1
ABC RESULTS:        internal signals:        5
ABC RESULTS:           input signals:        5
ABC RESULTS:          output signals:        3
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr partial_case_assign_noattr_generated_netlist.v

35. Executing Verilog backend.

35.1. Executing BMUXMAP pass.

35.2. Executing DEMUXMAP pass.
Dumping module `\partial_case_assign'.

yosys> show

36. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module partial_case_assign to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v

37. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v' to AST representation.
Generating RTLIL representation for module `\mux_generate'.
Successfully finished Verilog frontend.

yosys> synth -top mux_generate

38. Executing SYNTH pass.

38.1. Executing HIERARCHY pass (managing design hierarchy).

38.1.1. Analyzing design hierarchy..
Top module:  \mux_generate

38.1.2. Analyzing design hierarchy..
Top module:  \mux_generate
Removing unused module `\partial_case_assign'.
Removed 1 unused modules.

38.2. Executing PROC pass (convert processes to netlists).

38.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

38.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 4 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148 in module mux_generate.
Removed a total of 0 dead cases.

38.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 2 assignments to connections.

38.2.4. Executing PROC_INIT pass (extract init attributes).

38.2.5. Executing PROC_ARST pass (detect async resets in processes).

38.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~4 debug messages>

38.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\mux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148'.
     1/4: $4\y[0:0]
     2/4: $3\y[0:0]
     3/4: $2\y[0:0]
     4/4: $1\y[0:0]

38.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\mux_generate.\k' from process `\mux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148'.
Latch inferred for signal `\mux_generate.\y' from process `\mux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148': $auto$proc_dlatch.cc:432:proc_dlatch$1199

38.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

38.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

38.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 4 empty switches in `\mux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148'.
Removing empty process `mux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:5$1148'.
Cleaned up 4 empty switches.

38.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.
<suppressed ~12 debug messages>

38.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..
Removed 1 unused cells and 21 unused wires.
<suppressed ~2 debug messages>

38.5. Executing CHECK pass (checking for obvious problems).
Checking module mux_generate...
Found and reported 0 problems.

38.6. Executing OPT pass (performing simple optimizations).

38.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \mux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

38.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \mux_generate.
Performed a total of 0 changes.

38.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.6.6. Executing OPT_DFF pass (perform DFF optimizations).

38.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.6.9. Finished fast OPT passes. (There is nothing left to do.)

38.7. Executing FSM pass (extract and optimize FSM).

38.7.1. Executing FSM_DETECT pass (finding FSMs in design).

38.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

38.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

38.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

38.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

38.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

38.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

38.8. Executing OPT pass (performing simple optimizations).

38.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \mux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

38.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \mux_generate.
Performed a total of 0 changes.

38.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.8.6. Executing OPT_DFF pass (perform DFF optimizations).

38.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.8.9. Finished fast OPT passes. (There is nothing left to do.)

38.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 2) from port A of cell mux_generate.$eq$/home/ank/Desktop/SoC_Shwetank/verilog_files/mux_generate.v:8$1150 ($eq).

38.10. Executing PEEPOPT pass (run peephole optimizers).

38.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module mux_generate:
  created 0 $alu and 0 $macc cells.

38.13. Executing SHARE pass (SAT-based resource sharing).

38.14. Executing OPT pass (performing simple optimizations).

38.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \mux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

38.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \mux_generate.
Performed a total of 0 changes.

38.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.14.6. Executing OPT_DFF pass (perform DFF optimizations).

38.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.14.9. Finished fast OPT passes. (There is nothing left to do.)

38.15. Executing MEMORY pass.

38.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

38.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

38.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

38.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

38.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

38.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

38.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

38.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

38.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.17. Executing OPT pass (performing simple optimizations).

38.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.17.3. Executing OPT_DFF pass (perform DFF optimizations).

38.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.17.5. Finished fast OPT passes.

38.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

38.19. Executing OPT pass (performing simple optimizations).

38.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \mux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~4 debug messages>

38.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \mux_generate.
Performed a total of 0 changes.

38.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
Removed a total of 0 cells.

38.19.6. Executing OPT_SHARE pass.

38.19.7. Executing OPT_DFF pass (perform DFF optimizations).

38.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..

38.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.19.10. Finished fast OPT passes. (There is nothing left to do.)

38.20. Executing TECHMAP pass (map to technology primitives).

38.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

38.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $not.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $logic_not.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $dlatch.
No more expansions possible.
<suppressed ~92 debug messages>

38.21. Executing OPT pass (performing simple optimizations).

38.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.
<suppressed ~13 debug messages>

38.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
<suppressed ~6 debug messages>
Removed a total of 2 cells.

38.21.3. Executing OPT_DFF pass (perform DFF optimizations).

38.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..
Removed 4 unused cells and 16 unused wires.
<suppressed ~5 debug messages>

38.21.5. Finished fast OPT passes.

38.22. Executing ABC pass (technology mapping using ABC).

38.22.1. Extracting gate netlist of module `\mux_generate' to `<abc-temp-dir>/input.blif'..

38.22.1.1. Executed ABC.
Extracted 12 gates and 18 wires to a netlist network with 6 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-zysuN6/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

38.22.1.2. Re-integrating ABC results.
ABC RESULTS:            ANDNOT cells:        3
ABC RESULTS:               MUX cells:        3
ABC RESULTS:              NAND cells:        2
ABC RESULTS:        internal signals:       10
ABC RESULTS:           input signals:        6
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

38.23. Executing OPT pass (performing simple optimizations).

38.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module mux_generate.

38.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\mux_generate'.
<suppressed ~3 debug messages>
Removed a total of 1 cells.

38.23.3. Executing OPT_DFF pass (perform DFF optimizations).

38.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \mux_generate..
Removed 0 unused cells and 19 unused wires.
<suppressed ~1 debug messages>

38.23.5. Finished fast OPT passes.

38.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `mux_generate'. Setting top module to mux_generate.

38.24.1. Analyzing design hierarchy..
Top module:  \mux_generate

38.24.2. Analyzing design hierarchy..
Top module:  \mux_generate
Removed 0 unused modules.

38.25. Printing statistics.

=== mux_generate ===

        +----------Local Count, excluding submodules.
        | 
       15 wires
       50 wire bits
        8 public wires
       43 public wire bits
        6 ports
        7 port bits
        8 cells
        3   $_ANDNOT_
        1   $_DLATCH_N_
        3   $_MUX_
        1   $_NAND_

38.26. Executing CHECK pass (checking for obvious problems).
Checking module mux_generate...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

39. Executing ABC pass (technology mapping using ABC).

39.1. Extracting gate netlist of module `\mux_generate' to `<abc-temp-dir>/input.blif'..

39.1.1. Executed ABC.
Extracted 7 gates and 13 wires to a netlist network with 6 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

39.1.2. Re-integrating ABC results.
ABC RESULTS:          _const0_ cells:        1
ABC RESULTS:   sky130_fd_sc_hd__mux4_2 cells:        1
ABC RESULTS:        internal signals:        5
ABC RESULTS:           input signals:        6
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr mux_generate_noattr_generated_netlist.v

40. Executing Verilog backend.

40.1. Executing BMUXMAP pass.

40.2. Executing DEMUXMAP pass.
Dumping module `\mux_generate'.

yosys> show

41. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module mux_generate to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v

42. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v' to AST representation.
Generating RTLIL representation for module `\demux_generate'.
Successfully finished Verilog frontend.

yosys> synth -top demux_generate

43. Executing SYNTH pass.

43.1. Executing HIERARCHY pass (managing design hierarchy).

43.1.1. Analyzing design hierarchy..
Top module:  \demux_generate

43.1.2. Analyzing design hierarchy..
Top module:  \demux_generate
Removing unused module `\mux_generate'.
Removed 1 unused modules.

43.2. Executing PROC pass (convert processes to netlists).

43.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

43.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 8 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342 in module demux_generate.
Removed a total of 0 dead cases.

43.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 9 assignments to connections.

43.2.4. Executing PROC_INIT pass (extract init attributes).

43.2.5. Executing PROC_ARST pass (detect async resets in processes).

43.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~8 debug messages>

43.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\demux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342'.
     1/8: $8\y_int[7:7]
     2/8: $7\y_int[6:6]
     3/8: $6\y_int[5:5]
     4/8: $5\y_int[4:4]
     5/8: $4\y_int[3:3]
     6/8: $3\y_int[2:2]
     7/8: $2\y_int[1:1]
     8/8: $1\y_int[0:0]

43.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
No latch inferred for signal `\demux_generate.\k' from process `\demux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342'.
No latch inferred for signal `\demux_generate.\y_int' from process `\demux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342'.

43.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

43.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

43.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 8 empty switches in `\demux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342'.
Removing empty process `demux_generate.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:6$1342'.
Cleaned up 8 empty switches.

43.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.
<suppressed ~1 debug messages>

43.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..
Removed 0 unused cells and 26 unused wires.
<suppressed ~1 debug messages>

43.5. Executing CHECK pass (checking for obvious problems).
Checking module demux_generate...
Found and reported 0 problems.

43.6. Executing OPT pass (performing simple optimizations).

43.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

43.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_generate.
Performed a total of 0 changes.

43.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.6.6. Executing OPT_DFF pass (perform DFF optimizations).

43.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.6.9. Finished fast OPT passes. (There is nothing left to do.)

43.7. Executing FSM pass (extract and optimize FSM).

43.7.1. Executing FSM_DETECT pass (finding FSMs in design).

43.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

43.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

43.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

43.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

43.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

43.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

43.8. Executing OPT pass (performing simple optimizations).

43.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

43.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_generate.
Performed a total of 0 changes.

43.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.8.6. Executing OPT_DFF pass (perform DFF optimizations).

43.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.8.9. Finished fast OPT passes. (There is nothing left to do.)

43.9. Executing WREDUCE pass (reducing word size of cells).
Removed top 1 bits (of 3) from port A of cell demux_generate.$eq$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:10$1346 ($eq).
Removed top 1 bits (of 3) from port A of cell demux_generate.$eq$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:10$1345 ($eq).
Removed top 2 bits (of 3) from port A of cell demux_generate.$eq$/home/ank/Desktop/SoC_Shwetank/verilog_files/demux_generate.v:10$1344 ($eq).

43.10. Executing PEEPOPT pass (run peephole optimizers).

43.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module demux_generate:
  created 0 $alu and 0 $macc cells.

43.13. Executing SHARE pass (SAT-based resource sharing).

43.14. Executing OPT pass (performing simple optimizations).

43.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_generate..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~16 debug messages>

43.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_generate.
Performed a total of 0 changes.

43.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.14.6. Executing OPT_DFF pass (perform DFF optimizations).

43.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.14.9. Finished fast OPT passes. (There is nothing left to do.)

43.15. Executing MEMORY pass.

43.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

43.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

43.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

43.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

43.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

43.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

43.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

43.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

43.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.17. Executing OPT pass (performing simple optimizations).

43.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.
<suppressed ~8 debug messages>

43.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.17.3. Executing OPT_DFF pass (perform DFF optimizations).

43.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.17.5. Finished fast OPT passes.

43.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

43.19. Executing OPT pass (performing simple optimizations).

43.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \demux_generate..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

43.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \demux_generate.
Performed a total of 0 changes.

43.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.19.6. Executing OPT_SHARE pass.

43.19.7. Executing OPT_DFF pass (perform DFF optimizations).

43.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..

43.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.19.10. Finished fast OPT passes. (There is nothing left to do.)

43.20. Executing TECHMAP pass (map to technology primitives).

43.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

43.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $eq.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $logic_not.
No more expansions possible.
<suppressed ~93 debug messages>

43.21. Executing OPT pass (performing simple optimizations).

43.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.
<suppressed ~21 debug messages>

43.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
<suppressed ~39 debug messages>
Removed a total of 13 cells.

43.21.3. Executing OPT_DFF pass (perform DFF optimizations).

43.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..
Removed 0 unused cells and 27 unused wires.
<suppressed ~1 debug messages>

43.21.5. Finished fast OPT passes.

43.22. Executing ABC pass (technology mapping using ABC).

43.22.1. Extracting gate netlist of module `\demux_generate' to `<abc-temp-dir>/input.blif'..

43.22.1.1. Executed ABC.
Extracted 31 gates and 35 wires to a netlist network with 4 inputs and 8 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-gbPoni/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

43.22.1.2. Re-integrating ABC results.
ABC RESULTS:            ANDNOT cells:        8
ABC RESULTS:              NAND cells:        1
ABC RESULTS:               NOT cells:        1
ABC RESULTS:                OR cells:        9
ABC RESULTS:             ORNOT cells:        2
ABC RESULTS:        internal signals:       23
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        8
Removing temp directory.
Removing global temp directory.

43.23. Executing OPT pass (performing simple optimizations).

43.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module demux_generate.

43.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\demux_generate'.
Removed a total of 0 cells.

43.23.3. Executing OPT_DFF pass (perform DFF optimizations).

43.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \demux_generate..
Removed 0 unused cells and 35 unused wires.
<suppressed ~1 debug messages>

43.23.5. Finished fast OPT passes.

43.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `demux_generate'. Setting top module to demux_generate.

43.24.1. Analyzing design hierarchy..
Top module:  \demux_generate

43.24.2. Analyzing design hierarchy..
Top module:  \demux_generate
Removed 0 unused modules.

43.25. Printing statistics.

=== demux_generate ===

        +----------Local Count, excluding submodules.
        | 
       25 wires
       65 wire bits
       12 public wires
       52 public wire bits
       10 ports
       12 port bits
       21 cells
        8   $_ANDNOT_
        1   $_NAND_
        1   $_NOT_
        2   $_ORNOT_
        9   $_OR_

43.26. Executing CHECK pass (checking for obvious problems).
Checking module demux_generate...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

44. Executing ABC pass (technology mapping using ABC).

44.1. Extracting gate netlist of module `\demux_generate' to `<abc-temp-dir>/input.blif'..

44.1.1. Executed ABC.
Extracted 21 gates and 25 wires to a netlist network with 4 inputs and 8 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

44.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__and4_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__and4b_1 cells:        3
ABC RESULTS:   sky130_fd_sc_hd__nor4b_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__nor4bb_1 cells:        3
ABC RESULTS:        internal signals:       13
ABC RESULTS:           input signals:        4
ABC RESULTS:          output signals:        8
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr demux_generate_noattr_generated_netlist.v

45. Executing Verilog backend.

45.1. Executing BMUXMAP pass.

45.2. Executing DEMUXMAP pass.
Dumping module `\demux_generate'.

yosys> show

46. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module demux_generate to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v /home/ank/Desktop/SoC_Shwetank/verilog_files/rca.v

47. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v' to AST representation.
Generating RTLIL representation for module `\fa'.
Successfully finished Verilog frontend.

48. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/rca.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/rca.v' to AST representation.
Generating RTLIL representation for module `\rca'.
Successfully finished Verilog frontend.

yosys> synth -top rca

49. Executing SYNTH pass.

49.1. Executing HIERARCHY pass (managing design hierarchy).

49.1.1. Analyzing design hierarchy..
Top module:  \rca
Used module:     \fa

49.1.2. Analyzing design hierarchy..
Top module:  \rca
Used module:     \fa
Removing unused module `\demux_generate'.
Removed 1 unused modules.

49.2. Executing PROC pass (convert processes to netlists).

49.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

49.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed a total of 0 dead cases.

49.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 0 assignments to connections.

49.2.4. Executing PROC_INIT pass (extract init attributes).

49.2.5. Executing PROC_ARST pass (detect async resets in processes).

49.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.

49.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).

49.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).

49.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

49.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

49.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

49.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..
Removed 0 unused cells and 1 unused wires.
<suppressed ~1 debug messages>

49.5. Executing CHECK pass (checking for obvious problems).
Checking module fa...
Checking module rca...
Found and reported 0 problems.

49.6. Executing OPT pass (performing simple optimizations).

49.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \fa..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \rca..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

49.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \fa.
  Optimizing cells in module \rca.
Performed a total of 0 changes.

49.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.6.6. Executing OPT_DFF pass (perform DFF optimizations).

49.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.6.9. Finished fast OPT passes. (There is nothing left to do.)

49.7. Executing FSM pass (extract and optimize FSM).

49.7.1. Executing FSM_DETECT pass (finding FSMs in design).

49.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

49.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

49.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

49.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

49.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

49.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

49.8. Executing OPT pass (performing simple optimizations).

49.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \fa..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \rca..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

49.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \fa.
  Optimizing cells in module \rca.
Performed a total of 0 changes.

49.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.8.6. Executing OPT_DFF pass (perform DFF optimizations).

49.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.8.9. Finished fast OPT passes. (There is nothing left to do.)

49.9. Executing WREDUCE pass (reducing word size of cells).

49.10. Executing PEEPOPT pass (run peephole optimizers).

49.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module fa:
  creating $macc model for $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1611 ($add).
  creating $macc model for $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1612 ($add).
  merging $macc model for $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1611 into $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1612.
  creating $alu model for $macc $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1612.
  creating $alu cell for $add$/home/ank/Desktop/SoC_Shwetank/verilog_files/fa.v:2$1612: $auto$alumacc.cc:495:replace_alu$1613
  created 1 $alu and 0 $macc cells.
Extracting $alu and $macc cells in module rca:
  created 0 $alu and 0 $macc cells.

49.13. Executing SHARE pass (SAT-based resource sharing).

49.14. Executing OPT pass (performing simple optimizations).

49.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \fa..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \rca..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

49.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \fa.
  Optimizing cells in module \rca.
Performed a total of 0 changes.

49.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.14.6. Executing OPT_DFF pass (perform DFF optimizations).

49.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..
Removed 1 unused cells and 1 unused wires.
<suppressed ~2 debug messages>

49.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.14.9. Rerunning OPT passes. (Maybe there is more to do..)

49.14.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \fa..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \rca..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

49.14.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \fa.
  Optimizing cells in module \rca.
Performed a total of 0 changes.

49.14.12. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.14.13. Executing OPT_DFF pass (perform DFF optimizations).

49.14.14. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.14.15. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.14.16. Finished fast OPT passes. (There is nothing left to do.)

49.15. Executing MEMORY pass.

49.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

49.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

49.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

49.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

49.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

49.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

49.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

49.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

49.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.17. Executing OPT pass (performing simple optimizations).

49.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.17.3. Executing OPT_DFF pass (perform DFF optimizations).

49.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.17.5. Finished fast OPT passes.

49.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

49.19. Executing OPT pass (performing simple optimizations).

49.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \fa..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \rca..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

49.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \fa.
  Optimizing cells in module \rca.
Performed a total of 0 changes.

49.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.19.6. Executing OPT_SHARE pass.

49.19.7. Executing OPT_DFF pass (perform DFF optimizations).

49.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..

49.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.19.10. Finished fast OPT passes. (There is nothing left to do.)

49.20. Executing TECHMAP pass (map to technology primitives).

49.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

49.20.2. Continuing TECHMAP pass.
Using template $paramod$1d1e68f77481583066c6d429218f48ea9d5739b3\_90_alu for cells of type $alu.
Using template $paramod\_90_lcu_brent_kung\WIDTH=32'00000000000000000000000000000010 for cells of type $lcu.
Using extmapper simplemap for cells of type $pos.
Using extmapper simplemap for cells of type $and.
Using extmapper simplemap for cells of type $xor.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $not.
Using extmapper simplemap for cells of type $or.
No more expansions possible.
<suppressed ~216 debug messages>

49.21. Executing OPT pass (performing simple optimizations).

49.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
<suppressed ~9 debug messages>
Optimizing module rca.

49.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.21.3. Executing OPT_DFF pass (perform DFF optimizations).

49.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..
Removed 1 unused cells and 26 unused wires.
<suppressed ~2 debug messages>

49.21.5. Finished fast OPT passes.

49.22. Executing ABC pass (technology mapping using ABC).

49.22.1. Extracting gate netlist of module `\fa' to `<abc-temp-dir>/input.blif'..

49.22.1.1. Executed ABC.
Extracted 5 gates and 8 wires to a netlist network with 3 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-CFnDfz/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

49.22.1.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:            ANDNOT cells:        1
ABC RESULTS:                OR cells:        1
ABC RESULTS:              XNOR cells:        2
ABC RESULTS:        internal signals:        3
ABC RESULTS:           input signals:        3
ABC RESULTS:          output signals:        2
Removing temp directory.

49.22.2. Extracting gate netlist of module `\rca' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

49.22.2.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.
Removing global temp directory.

49.23. Executing OPT pass (performing simple optimizations).

49.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module fa.
Optimizing module rca.

49.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\fa'.
Finding identical cells in module `\rca'.
Removed a total of 0 cells.

49.23.3. Executing OPT_DFF pass (perform DFF optimizations).

49.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \fa..
Finding unused cells or wires in module \rca..
Removed 0 unused cells and 8 unused wires.
<suppressed ~1 debug messages>

49.23.5. Finished fast OPT passes.

49.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `rca'. Setting top module to rca.

49.24.1. Analyzing design hierarchy..
Top module:  \rca
Used module:     \fa

49.24.2. Analyzing design hierarchy..
Top module:  \rca
Used module:     \fa
Removed 0 unused modules.

49.25. Printing statistics.

=== fa ===

        +----------Local Count, excluding submodules.
        | 
        8 wires
        8 wire bits
        5 public wires
        5 public wire bits
        5 ports
        5 port bits
        5 cells
        1   $_ANDNOT_
        1   $_AND_
        1   $_OR_
        2   $_XNOR_

=== rca ===

        +----------Local Count, excluding submodules.
        | 
        5 wires
       41 wire bits
        5 public wires
       41 public wire bits
        3 ports
       25 port bits
        8 submodules
        8   fa

=== design hierarchy ===

        +----------Count including submodules.
        | 
       40 rca
        5 fa

        +----------Count including submodules.
        | 
       69 wires
      105 wire bits
       45 public wires
       81 public wire bits
       43 ports
       65 port bits
        - memories
        - memory bits
        - processes
       40 cells
        8   $_ANDNOT_
        8   $_AND_
        8   $_OR_
       16   $_XNOR_
        8 submodules
        8   fa

49.26. Executing CHECK pass (checking for obvious problems).
Checking module fa...
Checking module rca...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

50. Executing ABC pass (technology mapping using ABC).

50.1. Extracting gate netlist of module `\fa' to `<abc-temp-dir>/input.blif'..

50.1.1. Executed ABC.
Extracted 5 gates and 8 wires to a netlist network with 3 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

50.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__maj3_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__xor3_1 cells:        1
ABC RESULTS:        internal signals:        3
ABC RESULTS:           input signals:        3
ABC RESULTS:          output signals:        2
Removing temp directory.

50.2. Extracting gate netlist of module `\rca' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

50.2.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr rca_noattr_generated_netlist.v

51. Executing Verilog backend.

51.1. Executing BMUXMAP pass.

51.2. Executing DEMUXMAP pass.
Dumping module `\fa'.
Dumping module `\rca'.

yosys> show

52. Generating Graphviz representation of design.
ERROR: For formats different than 'ps' or 'dot' only one module must be selected.

yosys> show fa

53. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module fa to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> show rca

54. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module rca to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

