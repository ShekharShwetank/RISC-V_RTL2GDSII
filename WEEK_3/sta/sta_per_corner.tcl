# sta_per_corner.tcl — OpenSTA 2.7.0 compatible, no unsupported properties.

proc safe_read_lib {libpath} {
  if {[file exists $libpath]} {
    if {[catch {read_liberty $libpath} err]} {
      puts "WARNING: read_liberty failed for $libpath : $err"
    } else {
      puts "INFO: Loaded liberty $libpath"
    }
  } else {
    puts "WARNING: Liberty not found: $libpath"
  }
}

# Ensure OUT_DIR exists
if {![file isdirectory $::env(OUT_DIR)]} {
  exec mkdir -p $::env(OUT_DIR)
}

puts "=== Corner: $::env(CORNER_NAME)"
puts "    Lib   : $::env(CORNER_LIB)"

# Load libraries
safe_read_lib $::env(CORNER_LIB)
if {[info exists ::env(EXTRA_LIBS)] && $::env(EXTRA_LIBS) ne ""} {
  foreach L $::env(EXTRA_LIBS) {
    safe_read_lib $L
  }
}

# Read netlist & link
if {[catch {read_verilog $::env(NETLIST)} err]} {
  puts "ERROR: read_verilog failed: $err"
}
if {[catch {link_design $::env(TOP_CELL)} err]} {
  puts "ERROR: link_design failed: $err"
}

# Read SDC (robust clock binding for pll/CLK vs port fallback)
if {[file exists $::env(SDC_FILE)]} {
  if {[catch {read_sdc $::env(SDC_FILE)} err]} {
    puts "WARNING: read_sdc failed: $err"
  }
} else {
  puts "WARNING: SDC not found: $::env(SDC_FILE)"
}

# Write units (help lists: report_units ; no positional args)
with_output_to_variable units_output { report_units }
set units_file [file join $::env(OUT_DIR) units.rpt]
set fp [open $units_file w]; puts $fp $units_output; close $fp

# ------------------------------------------------------------
# Timing summaries (setup/hold)
# ------------------------------------------------------------
report_checks -path_delay max -format summary > [file join $::env(OUT_DIR) 3_setup_summary.rpt]
report_checks -path_delay min -format summary > [file join $::env(OUT_DIR) 4_hold_summary.rpt]

# Worst paths (write one full path each; avoid report_path pin args)
report_checks -path_delay max -format full  -group_path_count 1 -sort_by_slack > [file join $::env(OUT_DIR) 6_critical_path_full_max.rpt]
report_checks -path_delay min -format full  -group_path_count 1 -sort_by_slack > [file join $::env(OUT_DIR) 6_critical_path_full_min.rpt]

# WNS/TNS for setup (max) and hold (min) — commands from your help
report_wns -max > [file join $::env(OUT_DIR) wns_setup.rpt]
report_tns -max > [file join $::env(OUT_DIR) tns_setup.rpt]
report_wns -min > [file join $::env(OUT_DIR) wns_hold.rpt]
report_tns -min > [file join $::env(OUT_DIR) tns_hold.rpt]

puts "INFO: Corner $::env(CORNER_NAME) finished. Reports in $::env(OUT_DIR)"
exit

