(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc$ cat STA/run_sta.tcl
# OpenSTA Tcl Script for VSDBabySoC Analysis (restored, safe)
# -----------------------------------------------------------------------------
# Ensure output directory exists
if {![file exists "reports"]} {
    file mkdir reports
}

puts "INFO: Loading libraries..."
read_liberty VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty VSDBabySoC/src/lib/avsddac.lib
read_liberty VSDBabySoC/src/lib/avsdpll.lib

puts "INFO: Reading synthesized netlist..."
read_verilog VSDBabySoC/reports/vsdbabysoc_netlist.v

puts "INFO: Linking design..."
link_design vsdbabysoc

puts "INFO: Reading SDC constraints..."
read_sdc STA/final.sdc

puts "INFO: Generating timing reports..."

# A. Clock listing
report_clock_properties > reports/1_clocks.rpt

# B. Unconstrained endpoints (help find missing clocks/IO constraints)
report_checks -unconstrained > reports/2_unconstrained.rpt

# C. Full setup timing (max paths)
report_checks -path_delay max -format full_clock_expanded > reports/3_setup_report.rpt

# D. Full hold timing (min paths)
report_checks -path_delay min -format full_clock_expanded > reports/4_hold_report.rpt

# E. Worst slack summary
report_worst_slack -max > reports/5_worst_slack.rpt

# F. Single worst path (fast): limit to 1 path using report_checks
#     This is much faster than an unrestricted find_timing_paths.
report_checks -path_delay max -format short -group_path_count 1 > reports/6_critical_path.rpt

puts "INFO: Reports written to ./reports/"
puts "INFO: STA script finished."
exit
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc$ sta -no_splash STA/run_sta.tcl | tee STA/sta_run.log
INFO: Loading libraries...
Warning: VSDBabySoC/src/lib/sky130_fd_sc_hd__tt_025C_1v80.lib line 23, default_fanout_load is 0.0.
INFO: Reading synthesized netlist...
INFO: Linking design...
INFO: Reading SDC constraints...
INFO: Generating timing reports...
INFO: Reports written to ./reports/
INFO: STA script finished.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc$ ls -l reports
total 24
-rw-rw-r-- 1 ank ank  155 Oct  9 02:41 1_clocks.rpt
-rw-rw-r-- 1 ank ank 1140 Oct  9 02:41 2_unconstrained.rpt
-rw-rw-r-- 1 ank ank 1140 Oct  9 02:41 3_setup_report.rpt
-rw-rw-r-- 1 ank ank 1001 Oct  9 02:41 4_hold_report.rpt
-rw-rw-r-- 1 ank ank   21 Oct  9 02:41 5_worst_slack.rpt
-rw-rw-r-- 1 ank ank  192 Oct  9 02:41 6_critical_path.rpt
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc$ 

