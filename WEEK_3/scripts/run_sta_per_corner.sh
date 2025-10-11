# run_sta_per_corner.sh
set -euo pipefail

# --- Edit these to match your repo layout ---
TOP=vsdbabysoc
NETLIST="VSDBabySoC/reports/vsdbabysoc_netlist.v"
SDC="STA/final.sdc"

# Optional macro liberty files (if present)
EXTRA_LIBS="VSDBabySoC/src/lib/avsddac.lib VSDBabySoC/src/lib/avsdpll.lib"

# Where to write per-corner reports
OUTROOT="reports/pvt"

# Sky130 liberty root (you’ve already confirmed these exist)
PDKROOT="$HOME/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib"

# Choose the exact subset you want to run (expand later if you wish)
# This array maps corner names to their corresponding .lib file paths.
# Note: The *_ccsnoise.lib files are for noise analysis and are not included as timing corners.

declare -A CORNERS=(
  # Typical-Typical Corners
  [tt_025C_1v80]="$PDKROOT/sky130_fd_sc_hd__tt_025C_1v80.lib"
  [tt_100C_1v80]="$PDKROOT/sky130_fd_sc_hd__tt_100C_1v80.lib"

  # Fast-Fast Corners
  [ff_100C_1v65]="$PDKROOT/sky130_fd_sc_hd__ff_100C_1v65.lib"
  [ff_100C_1v95]="$PDKROOT/sky130_fd_sc_hd__ff_100C_1v95.lib"
  [ff_n40C_1v56]="$PDKROOT/sky130_fd_sc_hd__ff_n40C_1v56.lib"
  [ff_n40C_1v65]="$PDKROOT/sky130_fd_sc_hd__ff_n40C_1v65.lib"
  [ff_n40C_1v76]="$PDKROOT/sky130_fd_sc_hd__ff_n40C_1v76.lib"
  [ff_n40C_1v95]="$PDKROOT/sky130_fd_sc_hd__ff_n40C_1v95.lib"

  # Slow-Slow Corners
  [ss_100C_1v40]="$PDKROOT/sky130_fd_sc_hd__ss_100C_1v40.lib"
  [ss_100C_1v60]="$PDKROOT/sky130_fd_sc_hd__ss_100C_1v60.lib"
  [ss_n40C_1v28]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v28.lib"
  [ss_n40C_1v35]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v35.lib"
  [ss_n40C_1v40]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v40.lib"
  [ss_n40C_1v44]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v44.lib"
  [ss_n40C_1v60]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v60.lib"
  [ss_n40C_1v76]="$PDKROOT/sky130_fd_sc_hd__ss_n40C_1v76.lib"
)

# Prevent “hangs”: kill a corner run if it exceeds this many seconds
: "${STA_TIMEOUT:=600}"

mkdir -p "$OUTROOT"

for cname in "${!CORNERS[@]}"; do
  lib="${CORNERS[$cname]}"
  outdir="$OUTROOT/$cname"
  mkdir -p "$outdir"

  echo "=== Running corner: $cname"
  echo "    Lib: $lib"

  # Export env vars used by the TCL
  CORNER_NAME="$cname" \
  CORNER_LIB="$lib" \
  TOP_CELL="$TOP" \
  NETLIST="$NETLIST" \
  SDC_FILE="$SDC" \
  OUT_DIR="$outdir" \
  EXTRA_LIBS="$EXTRA_LIBS" \
  timeout "$STA_TIMEOUT" sta -no_splash STA/sta_per_corner.tcl

  echo "Completed $cname -> $outdir"
done

echo "All corners processed. Reports are under $OUTROOT/"

