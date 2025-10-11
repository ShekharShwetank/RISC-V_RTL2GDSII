set -euo pipefail

# Edit the __CORNERS__ array below to match liberty files you have locally.
# Format: "label|/path/to/libfile"

CORNERS=(
  "tt_025C_1v80|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib"
  "tt_100C_1v80|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_100C_1v80.lib"
  "ff_100C_1v65|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ff_100C_1v65.lib"
  "ff_100C_1v95|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ff_100C_1v95.lib"
  "ff_n40C_1v56|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ff_n40C_1v56.lib"
  "ff_n40C_1v76|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ff_n40C_1v76.lib"
  "ss_100C_1v40|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ss_100C_1v40.lib"
  "ss_n40C_1v28|/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__ss_n40C_1v28.lib"
)


# Path to your synthesized netlist and SDC (as used earlier)
NETLIST="VSDBabySoC/reports/vsdbabysoc_netlist.v"
SDC="STA/final.sdc"
TOPCELL="vsdbabysoc"   # adjust if your top cell differs

OUTDIR="reports/pvt"
mkdir -p "${OUTDIR}"

# Template function: create a temporary STA script for a corner
make_sta_for_corner() {
  local label="$1"
  local libpath="$2"
  local outscript="$3"

cat > "${outscript}" <<'TCL'
# Auto-generated STA script
read_liberty __LIBPATH__
read_liberty VSDBabySoC/src/lib/avsddac.lib
read_liberty VSDBabySoC/src/lib/avsdpll.lib
read_verilog __NETLIST__
link_design __TOP__
read_sdc __SDC__

# produce standard reports
report_clock_properties > __OUT__/__LABEL__._1_clocks.rpt
report_checks -unconstrained > __OUT__/__LABEL__._2_unconstrained.rpt
report_checks -path_delay max -format full_clock_expanded > __OUT__/__LABEL__._6_critical_path_full.rpt
report_checks -path_delay max -format full -group_path_count 1 > __OUT__/__LABEL__._6_critical_path_short.rpt
report_worst_slack -max > __OUT__/__LABEL__._5_worst_slack_max.rpt
report_worst_slack -min > __OUT__/__LABEL__._5_worst_slack_min.rpt
set wns_val [get_wns]
set tns_val [get_tns]
puts "WNS = \$wns_val" > ${OUTDIR}/${label}._wns.rpt
puts "TNS = \$tns_val" > ${OUTDIR}/${label}._tns.rpt
# also produce setup/hold full reports
report_checks -path_delay max -format full_clock_expanded > __OUT__/__LABEL__._3_setup_full.rpt
report_checks -path_delay min -format full_clock_expanded > __OUT__/__LABEL__._4_hold_full.rpt

exit
TCL

  # replace placeholders
  sed -i "s|__LIBPATH__|${libpath}|g" "${outscript}"
  sed -i "s|__NETLIST__|${NETLIST}|g" "${outscript}"
  sed -i "s|__TOP__|${TOPCELL}|g" "${outscript}"
  sed -i "s|__SDC__|${SDC}|g" "${outscript}"
  sed -i "s|__OUT__|${OUTDIR}|g" "${outscript}"
  sed -i "s|__LABEL__|${label}|g" "${outscript}"
}

# loop corners
for entry in "${CORNERS[@]}"; do
  label="${entry%%|*}"
  libpath="${entry#*|}"
  echo "=== Running corner: $label  (lib: $libpath)"
  if [ ! -f "$libpath" ]; then
    echo "WARNING: liberty file not found: $libpath  — skipping $label"
    continue
  fi
  script="/tmp/sta_run_${label}.tcl"
  make_sta_for_corner "$label" "$libpath" "$script"

  # run sta and capture log
  sta -no_splash "$script" > "${OUTDIR}/${label}_sta.log" 2>&1 || {
    echo "STA failed for corner $label — see ${OUTDIR}/${label}_sta.log"
    # continue with next corner (do not exit)
    continue
  }

  echo "Completed corner $label. Reports written under ${OUTDIR}/"
done

echo "All corners processed. Reports in ${OUTDIR}/"

