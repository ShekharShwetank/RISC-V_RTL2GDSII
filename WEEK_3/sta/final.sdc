# ==================================================
# final.sdc — Clean OpenSTA-compatible version
# for VSDBabySoC timing analysis
# ==================================================

# 1. Define the main clock
set clk_targets [get_pins pll/CLK]
if {[llength $clk_targets] == 0} {
    set clk_targets [get_ports core_clk]
    if {[llength $clk_targets] == 0} {
        set clk_targets [get_pins */CLK]
    }
}
create_clock -name core_clk -period 11.0 $clk_targets

# 2. Collect ports
set all_in  [all_inputs]
set all_out [all_outputs]
set non_data_ports [get_ports {REF VCO_IN ENb_CP ENb_VCO reset}]

# 3. Exclude asynchronous control signals (e.g. reset)
set_false_path -from [get_ports reset]

# 4. Define data input ports (exclude non-data ones)
# OpenSTA doesn't support remove_from_collection, so use filter logic
set data_in {}
foreach port $all_in {
    if {[lsearch $non_data_ports $port] == -1} {
        lappend data_in $port
    }
}

# 5. Apply input/output delays
set input_delay_val  [expr {0.3 * 11.0}]
set output_delay_val [expr {0.3 * 11.0}]
set_input_delay  $input_delay_val -clock [get_clocks core_clk] $data_in
set_output_delay $output_delay_val -clock [get_clocks core_clk] $all_out

# 6. Clock uncertainties and transition
set_clock_uncertainty -setup 0.10 [get_clocks core_clk]
set_clock_uncertainty -hold  0.05 [get_clocks core_clk]
set_clock_transition 0.05 [get_clocks core_clk]

# 7. Output loads
set_load 0.02 [all_outputs]

