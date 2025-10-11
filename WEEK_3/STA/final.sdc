# Final, robust SDC for VSDBabySoC

# 1. Define the primary clock on the output of the black-box PLL.
create_clock -name "core_clk" -period 11.0 [get_pins {pll/CLK}]

# 2. Get collections of all I/O ports.
set all_in [all_inputs]
set all_out [all_outputs]

# 3. Define a collection of all non-data ports (clocks, resets, controls).
set non_data_ports [get_ports {REF VCO_IN ENb_CP ENb_VCO reset}]

# 4. Apply I/O delays: first apply to ALL inputs, then clear the non-data ports
set input_delay_val [expr {0.3 * 11.0}]
set output_delay_val [expr {0.3 * 11.0}]

# Apply to every input (safer than trying to build set difference)
set_input_delay $input_delay_val -clock [get_clocks {core_clk}] $all_in
# Override the non-data ports to effectively exclude them
set_input_delay 0.0 -clock [get_clocks {core_clk}] $non_data_ports

# Outputs: all outputs are data ports in this design
set_output_delay $output_delay_val -clock [get_clocks {core_clk}] $all_out

