read_liberty .../sky130_fd_sc_hd__tt_025C_1v80.lib
read_lef $(VSDBabySoC_DIR)/lef/avsddac.lef
read_lef $(VSDBabySoC_DIR)/lef/avsdpll.lef
read_db ./results/sky130hd/VSDBabySoC/base/2_3_floorplan_tapcell.odb
# list macros and their pins
foreach m [get_cells -filter "is_macro==1"] {
  puts "$m"
  foreach p [get_pins -of_objects $m] {
    puts "  [get_property $p name] layer=[get_property $p layer]"
  }
}
# check connectivity for nets named VDD, VPWR, etc
foreach net VDD VPWR VDD2 VDD3 VSS VGND {
  puts "===== net $net ====="
  if {[catch {psm::check_connectivity -net $net} res]} {
    puts "  check failed or not present"
  } else {
    puts "  $res"
  }
}

