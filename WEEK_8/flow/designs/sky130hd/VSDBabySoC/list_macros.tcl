read_liberty ./platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_lef ./designs/sky130hd/VSDBabySoC/lef/avsddac.lef
read_lef ./designs/sky130hd/VSDBabySoC/lef/avsdpll.lef
read_db ./results/sky130hd/VSDBabySoC/base/2_3_floorplan_tapcell.odb

puts "=== Macro instances and pins ==="
foreach m [get_cells -filter "is_macro==1"] {
  puts "MACRO_INSTANCE: $m"
  foreach p [get_pins -of_objects $m] {
    # print pin name and layer(s)
    set pname [get_property $p name]
    set layers ""
    if {[catch {set layers [get_property $p layers]}]} { set layers "[no layers]" }
    puts "  PIN: $pname  layers: $layers"
  }
}
