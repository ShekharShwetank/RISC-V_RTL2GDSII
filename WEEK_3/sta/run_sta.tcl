# -------------------------------------------------------------------------
# OpenSTA Tcl Script for VSDBabySoC Analysis (final, OpenSTA 2.7.0 compatible)
# -------------------------------------------------------------------------

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
puts "A done"

# B. Unconstrained endpoints
report_checks -unconstrained > reports/2_unconstrained.rpt
puts "B done"

# C. Full setup timing (max paths)
report_checks -path_delay max -format full_clock_expanded > reports/3_setup_report.rpt
puts "C done"

# D. Full hold timing (min paths)
report_checks -path_delay min -format full_clock_expanded > reports/4_hold_report.rpt
puts "D done"

# E. Worst slack summary
report_worst_slack -max > reports/5_worst_slack.rpt
puts "E done"

# F. Single worst (critical) path report
report_checks -path_delay max -format short -group_path_count 1 > reports/6_critical_path.rpt
puts "F done"

report_checks -path_delay max -format full_clock_expanded -group_path_count 1 > reports/6_critical_path_full.rpt
report_checks -path_delay max -format full -group_path_count 1 > reports/6_critical_path_full_short.rpt

puts "INFO: Reports written to ./reports/"
puts "INFO: STA script finished successfully."

# Proper termination (avoid Tcl positional argument bug)
exit

