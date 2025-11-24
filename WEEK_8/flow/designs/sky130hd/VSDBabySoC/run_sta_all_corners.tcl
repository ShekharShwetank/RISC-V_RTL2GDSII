# /mnt/data/run_sta_all_corners.tcl
# Run: openroad -no_gui -exit /mnt/data/run_sta_all_corners.tcl

set root "/home/shwetank/OpenROAD-flow-scripts/flow"
set resdir "$root/results/sky130hd/VSDBabySoC/base"
set outdir "$root/reports/sta_across_pvt"
file mkdir $outdir

# list every corner lib you asked to include (absolute paths)
set corner_libs {
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_100C_1v80.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_100C_1v40.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_100C_1v60.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v28.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v35.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v40.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v44.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v60_ccsnoise.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v60.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v76.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v56.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v65.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v76.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v95_ccsnoise.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_100C_1v65.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_100C_1v95.lib"
}

# macro libs (absolute)
set macro_libs {
  "/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib"
  "/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib"
}

# Stages: map name -> "odb sdc"
array set stages {
  postsynth   "$resdir/1_1_yosys_canonicalize.rtlil $resdir/1_synth.sdc"
  postplace   "$resdir/3_place.odb $resdir/3_place.sdc"
  postcts     "$resdir/4_cts.odb $resdir/4_cts.sdc"
  postroute   "$resdir/5_route.odb $resdir/5_route.sdc"
}

proc run_stage {stage adb sdc outprefix} {
  puts "   Reading DB: $adb"
  if {![file exists $adb]} {
    puts "   SKIP (odb missing): $adb"
    return
  }
  read_db $adb
  if {[file exists $sdc]} {
    puts "   Reading SDC: $sdc"
    read_sdc $sdc
  } else {
    puts "   WARNING: SDC not found: $sdc"
  }
  # report setup (top 200 paths)
  set rpt_setup "${outprefix}_setup.rpt"
  report_timing -type setup -max_paths 200 -from_ports -to_ports -sort_by_slack -outfile $rpt_setup
  # report hold
  set rpt_hold "${outprefix}_hold.rpt"
  report_timing -type hold -max_paths 200 -from_ports -to_ports -sort_by_slack -outfile $rpt_hold
  # small summary extraction (WNS/TNS)
  set sumf "${outprefix}_summary.txt"
  catch { exec sh -c "grep -E 'WNS|TNS|Total negative slack|Worst slack' $rpt_setup > $sumf" } ret
  remove_db
}

# Main loop: load each corner lib and run stages
foreach lib $corner_libs {
  if {![file exists $lib]} {
    puts "WARN: corner lib not found: $lib  (skipping)"
    continue
  }
  puts "=== corner: $lib ==="
  read_liberty $lib
  # load macro libs
  foreach m $macro_libs {
    if {[file exists $m]} { read_liberty $m } else { puts "WARN: macro lib missing: $m" }
  }
  # for each stage, read db & sdc and generate reports
  foreach k [array names stages] {
    set pair [split $stages($k) " "]
    set odb [lindex $pair 0]
    set sdc [lindex $pair 1]
    set cornerbase [file tail $lib]
    regsub {\.lib$} $cornerbase "" cornerbase
    set outprefix "$outdir/${k}_${cornerbase}"
    puts " Running stage $k -> $outprefix"
    run_stage $k $odb $sdc $outprefix
  }
  # clear libs before next corner
  reset_timing_libs
}
puts "Finished. check: $outdir"
exit 0
