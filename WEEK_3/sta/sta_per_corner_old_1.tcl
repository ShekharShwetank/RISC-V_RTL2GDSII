# sta_per_corner.tcl — fixed for OpenSTA 2.7.0 (no positional args in report_units)

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

if {![file isdirectory $::env(OUT_DIR)]} {
  exec mkdir -p $::env(OUT_DIR)
}

puts "=== Corner: $::env(CORNER_NAME)"
puts "    Lib   : $::env(CORNER_LIB)"

safe_read_lib $::env(CORNER_LIB)
if {[info exists ::env(EXTRA_LIBS)] && $::env(EXTRA_LIBS) ne ""} {
  foreach L $::env(EXTRA_LIBS) { safe_read_lib $L }
}

if {[catch {read_verilog $::env(NETLIST)} err]} {
  puts "ERROR: read_verilog failed: $err"
}
if {[catch {link_design $::env(TOP_CELL)} err]} {
  puts "ERROR: link_design failed: $err"
}

if {[file exists $::env(SDC_FILE)]} {
  if {[catch {read_sdc $::env(SDC_FILE)} err]} {
    puts "WARNING: read_sdc failed: $err"
  }
} else {
  puts "WARNING: SDC not found: $::env(SDC_FILE)"
}

# === FIXED: safely write report_units ===
set units_file [file join $::env(OUT_DIR) units.rpt]
with_output_to_variable units_output { report_units }
set fp [open $units_file w]
puts $fp $units_output
close $fp

# === Timing reports ===
report_checks -path_delay max -format summary > [file join $::env(OUT_DIR) 3_setup_summary.rpt]
report_checks -path_delay min -format summary > [file join $::env(OUT_DIR) 4_hold_summary.rpt]

report_wns -max > [file join $::env(OUT_DIR) wns_setup.rpt]
report_tns -max > [file join $::env(OUT_DIR) tns_setup.rpt]
report_wns -min > [file join $::env(OUT_DIR) wns_hold.rpt]
report_tns -min > [file join $::env(OUT_DIR) tns_hold.rpt]

# === Safe critical-path reporting for OpenSTA 2.7.0 (Parallax build) ===
# Uses report_worst_slack to find worst endpoints.

# --- Worst setup (max) path ---
set setup_rpt [file join $::env(OUT_DIR) 6_critical_path_full_max.rpt]
set setup_worst [report_worst_slack -max]
if {$setup_worst ne ""} {
    # Extract endpoint pin from the report text (it's printed as "Endpoint: <pin>")
    set endpoint_pin ""
    foreach line [split $setup_worst "\n"] {
        if {[regexp {Endpoint:\s+(\S+)} $line -> ep]} {
            set endpoint_pin $ep
            break
        }
    }
    if {$endpoint_pin ne ""} {
        puts "INFO: Setup endpoint pin detected: $endpoint_pin"
        report_path -max $endpoint_pin > $setup_rpt
    } else {
        puts "WARNING: Could not extract setup endpoint pin for $::env(CORNER_NAME)"
    }
} else {
    puts "WARNING: No setup (max) path found for $::env(CORNER_NAME)"
}

# --- Worst hold (min) path ---
set hold_rpt [file join $::env(OUT_DIR) 6_critical_path_full_min.rpt]
set hold_worst [report_worst_slack -min]
if {$hold_worst ne ""} {
    set endpoint_pin ""
    foreach line [split $hold_worst "\n"] {
        if {[regexp {Endpoint:\s+(\S+)} $line -> ep]} {
            set endpoint_pin $ep
            break
        }
    }
    if {$endpoint_pin ne ""} {
        puts "INFO: Hold endpoint pin detected: $endpoint_pin"
        report_path -min $endpoint_pin > $hold_rpt
    } else {
        puts "WARNING: Could not extract hold endpoint pin for $::env(CORNER_NAME)"
    }
} else {
    puts "WARNING: No hold (min) path found for $::env(CORNER_NAME)"
}

puts "INFO: Corner $::env(CORNER_NAME) finished. Reports in $::env(OUT_DIR)"
exit



