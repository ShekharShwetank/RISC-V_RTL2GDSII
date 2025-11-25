#!/bin/bash

################################################################################
# Multi-Corner Multi-Stage Static Timing Analysis Script for VSDBabySoC
# OpenROAD Flow - Week 8 Task Implementation
################################################################################

OPENROAD_BIN=~/OpenROAD-flow-scripts/tools/OpenROAD/build/bin/openroad
ROOT="$PWD"
DES="$ROOT/results/sky130hd/VSDBabySoC/base"
MACRO1="$ROOT/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib"
MACRO2="$ROOT/designs/sky130hd/VSDBabySoC/lib/avsddac.lib"
OUTDIR="$ROOT/reports/sta_across_pvt"
LOGDIR="$ROOT/logs/sta_corners"

mkdir -p "$OUTDIR" "$LOGDIR"

# Define all PVT corners with their corresponding library files
declare -A CORNERS=(
    ["tt_025C_1v80"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
    ["tt_100C_1v80"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_100C_1v80.lib"
    ["ff_100C_1v65"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_100C_1v65.lib"
    ["ff_100C_1v95"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_100C_1v95.lib"
    ["ff_n40C_1v56"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v56.lib"
    ["ff_n40C_1v65"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v65.lib"
    ["ff_n40C_1v76"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v76.lib"
    ["ff_n40C_1v95"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ff_n40C_1v95.lib"
    ["ss_100C_1v40"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_100C_1v40.lib"
    ["ss_100C_1v60"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_100C_1v60.lib"
    ["ss_n40C_1v28"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v28.lib"
    ["ss_n40C_1v35"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v35.lib"
    ["ss_n40C_1v40"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v40.lib"
    ["ss_n40C_1v44"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v44.lib"
    ["ss_n40C_1v60"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v60.lib"
    ["ss_n40C_1v76"]="$ROOT/platforms/sky130hd/lib/sky130_fd_sc_hd__ss_n40C_1v76.lib"
)

# Function to run STA for a specific corner and stage
run_sta_corner() {
    local corner_name=$1
    local corner_lib=$2
    local stage=$3
    local stage_file=$4
    local sdc_file=$5
    local spef_file=$6
    
    echo "=================================================="
    echo "Running STA Analysis"
    echo "Corner: $corner_name"
    echo "Stage: $stage"
    echo "=================================================="
    
    $OPENROAD_BIN -no_init -no_splash <<TCL 2>&1 | tee "$LOGDIR/${stage}_${corner_name}.log"

# Clear any previous database
catch {remove_db}

# Read liberty files
read_liberty "$corner_lib"
if { [file exists "$MACRO1"] } { read_liberty "$MACRO1" }
if { [file exists "$MACRO2"] } { read_liberty "$MACRO2" }

# Read design based on stage
if { "$stage" == "postsynth" } {
    # For post-synthesis, we need to load LEF files first
    set platform_dir "$ROOT/platforms/sky130hd"
    
    # Read technology LEF
    if { [file exists "\$platform_dir/lef/sky130_fd_sc_hd.tlef"] } {
        read_lef "\$platform_dir/lef/sky130_fd_sc_hd.tlef"
    }
    
    # Read standard cell LEF
    if { [file exists "\$platform_dir/lef/sky130_fd_sc_hd_merged.lef"] } {
        read_lef "\$platform_dir/lef/sky130_fd_sc_hd_merged.lef"
    } elseif { [file exists "\$platform_dir/lef/sky130_fd_sc_hd.lef"] } {
        read_lef "\$platform_dir/lef/sky130_fd_sc_hd.lef"
    }
    
    # Read macro LEFs if they exist
    set macro_lef_dir "$ROOT/designs/sky130hd/VSDBabySoC/lef"
    if { [file exists "\$macro_lef_dir/avsdpll.lef"] } {
        read_lef "\$macro_lef_dir/avsdpll.lef"
    }
    if { [file exists "\$macro_lef_dir/avsddac.lef"] } {
        read_lef "\$macro_lef_dir/avsddac.lef"
    }
    
    # Now read the Verilog netlist
    read_verilog "$stage_file"
    link_design vsdbabysoc
} else {
    read_db "$stage_file"
}

# Read timing constraints
read_sdc "$sdc_file"

# Read SPEF parasitics if available (post-route only)
if { "$spef_file" != "" && [file exists "$spef_file"] } {
    read_spef "$spef_file"
    puts "SPEF loaded: $spef_file"
}

# Generate detailed timing reports for setup analysis
report_checks -path_delay max -fields {input_pin slew capacitance} \
    -format full_clock_expanded -digits 4 -unconstrained \
    > "$OUTDIR/${stage}_${corner_name}_setup.rpt"

# Generate detailed timing reports for hold analysis
report_checks -path_delay min -fields {input_pin slew capacitance} \
    -format full_clock_expanded -digits 4 -unconstrained \
    > "$OUTDIR/${stage}_${corner_name}_hold.rpt"

# Report summary metrics - Setup (max delay)
set wns_max [sta::worst_slack_cmd "max"]
set tns_max [sta::total_negative_slack_cmd "max"]

# Report summary metrics - Hold (min delay)
set wns_min [sta::worst_slack_cmd "min"]
set tns_min [sta::total_negative_slack_cmd "min"]

# Write summary to files
set summary_file [open "$OUTDIR/${stage}_${corner_name}_summary.txt" w]
puts \$summary_file "Timing Analysis Summary"
puts \$summary_file "Corner: $corner_name"
puts \$summary_file "Stage: $stage"
puts \$summary_file "======================================"
puts \$summary_file "Setup Analysis (Max Delay):"
puts \$summary_file "  Worst Negative Slack (WNS): \$wns_max"
puts \$summary_file "  Total Negative Slack (TNS): \$tns_max"
puts \$summary_file "Hold Analysis (Min Delay):"
puts \$summary_file "  Worst Hold Slack (WHS): \$wns_min"
puts \$summary_file "  Total Hold Slack (THS): \$tns_min"
close \$summary_file

# Print to console
puts "======================================"
puts "Timing Summary for $corner_name - $stage"
puts "======================================"
puts "Setup: WNS = \$wns_max, TNS = \$tns_max"
puts "Hold:  WHS = \$wns_min, THS = \$tns_min"
puts "======================================"

exit
TCL
    
    if [ $? -eq 0 ]; then
        echo "Successfully completed STA for $corner_name at $stage stage"
    else
        echo "ERROR: STA failed for $corner_name at $stage stage"
    fi
    echo ""
}

# Main execution loop - iterate through all corners and stages
echo "Starting Multi-Corner Multi-Stage STA Analysis"
echo "Total corners to analyze: ${#CORNERS[@]}"
echo ""

for corner_name in "${!CORNERS[@]}"; do
    corner_lib="${CORNERS[$corner_name]}"
    
    # Verify corner library exists
    if [ ! -f "$corner_lib" ]; then
        echo "WARNING: Library file not found for corner $corner_name: $corner_lib"
        continue
    fi
    
    # Stage 1: Post-Synthesis Analysis
    if [ -f "$DES/1_synth.v" ] && [ -f "$DES/1_synth.sdc" ]; then
        run_sta_corner "$corner_name" "$corner_lib" "postsynth" \
            "$DES/1_synth.v" "$DES/1_synth.sdc" ""
    else
        echo "Skipping post-synthesis for $corner_name: files not found"
    fi
    
    # Stage 2: Post-Placement (Pre-CTS) Analysis
    if [ -f "$DES/3_place.odb" ] && [ -f "$DES/3_place.sdc" ]; then
        run_sta_corner "$corner_name" "$corner_lib" "postplace" \
            "$DES/3_place.odb" "$DES/3_place.sdc" ""
    else
        echo "Skipping post-placement for $corner_name: files not found"
    fi
    
    # Stage 3: Post-CTS Analysis
    if [ -f "$DES/4_cts.odb" ] && [ -f "$DES/4_cts.sdc" ]; then
        run_sta_corner "$corner_name" "$corner_lib" "postcts" \
            "$DES/4_cts.odb" "$DES/4_cts.sdc" ""
    else
        echo "Skipping post-CTS for $corner_name: files not found"
    fi
    
    # Stage 4: Post-Route Analysis with SPEF parasitics
    if [ -f "$DES/5_route.odb" ] && [ -f "$DES/5_route.sdc" ]; then
        run_sta_corner "$corner_name" "$corner_lib" "postroute" \
            "$DES/5_route.odb" "$DES/5_route.sdc" "$DES/6_final.spef"
    else
        echo "Skipping post-route for $corner_name: files not found"
    fi
done

echo ""
echo "=================================================="
echo "Multi-Corner STA Analysis Complete"
echo "=================================================="
echo "Reports directory: $OUTDIR"
echo "Logs directory: $LOGDIR"
echo ""
echo "Summary files generated for all corners:"
ls -lh "$OUTDIR"/*_summary.txt 2>/dev/null | wc -l
echo "files"

