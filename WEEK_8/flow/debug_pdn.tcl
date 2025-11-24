read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/6_1_fill.odb

# detailed pin/net reporting for the macro instances
report_inst -netlist_instance dac -nets -detail
report_inst -netlist_instance pll -nets -detail

# summary for the VDD net
report_net VDD -nets

exit
