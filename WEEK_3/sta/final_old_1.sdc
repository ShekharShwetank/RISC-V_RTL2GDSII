# final.sdc for VSDBabySoC (clean version)

set clk_targets [get_pins pll/CLK]
if {[llength $clk_targets] == 0} {
  # Fallback: try a top-level port named core_clk, else any pin named */CLK
  set clk_targets [get_ports core_clk]
  if {[llength $clk_targets] == 0} {
    set clk_targets [get_pins */CLK]
  }
}
create_clock -name core_clk -period 11.0 $clk_targets

# 1. Define the core clock (on PLL output or port)
# create_clock -name core_clk -period 11.0 [get_ports {core_clk}]
# Alternative (if PLL pin is visible):
# create_clock -name core_clk -period 11.0 [get_pins pll/CLK]

# 2. Collect ports
set all_in  [all_inputs]
set all_out [all_outputs]
set non_data_ports [get_ports {REF VCO_IN ENb_CP ENb_VCO reset}]

# 3. Exclude asynchronous controls
set_false_path -from [get_ports reset]

# 4. Apply input/output delays
set input_delay_val  [expr {0.3 * 11.0}]
set output_delay_val [expr {0.3 * 11.0}]
# set data_in  [remove_from_collection $all_in $non_data_ports]

set_input_delay  $input_delay_val -clock [get_clocks core_clk] $data_in
set_output_delay $output_delay_val -clock [get_clocks core_clk] $all_out

# 5. Clock uncertainties and transition
set_clock_uncertainty -setup 0.10 [get_clocks core_clk]
set_clock_uncertainty -hold  0.05 [get_clocks core_clk]
set_clock_transition 0.05 [get_clocks core_clk]

# 6. Output loads
set_load 0.02 [all_outputs]

