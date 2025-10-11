#!/bin/bash

# Define the absolute base directory for the PVT reports
BASE_DIR="/home/ank/Desktop/SoC_Shwetank/WEEK_3/babysoc/reports/pvt"

# Define the array of corner names to iterate through
CORNERS=(
  "tt_025C_1v80"
  "tt_100C_1v80"
  "ff_100C_1v65"
  "ff_100C_1v95"
  "ff_n40C_1v56"
  "ff_n40C_1v65"
  "ff_n40C_1v76"
  "ff_n40C_1v95"
  "ss_100C_1v40"
  "ss_100C_1v60"
  "ss_n40C_1v28"
  "ss_n40C_1v35"
  "ss_n40C_1v40"
  "ss_n40C_1v44"
  "ss_n40C_1v60"
  "ss_n40C_1v76"
)

# Loop through each corner name
for corner in "${CORNERS[@]}"; do
    # Construct the full path to the summary file
    FILE_PATH="$BASE_DIR/$corner/4_hold_summary.rpt"

    # Print a header for each corner's output
    echo "=========================================================="
    echo "Hold Summary for Corner: $corner"
    echo "=========================================================="

    # Check if the file exists and print its contents, or report that it's missing
    if [ -f "$FILE_PATH" ]; then
        cat "$FILE_PATH"
    else
        echo "Report not found at: $FILE_PATH"
    fi

    # Add a blank line for readability
    echo
done

