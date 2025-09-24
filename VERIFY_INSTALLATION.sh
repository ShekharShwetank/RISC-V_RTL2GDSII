#!/bin/bash

# Script to verify installation of all open-source tools

echo "Starting verification of installed tools..."

# Function to check command success
check_command() {
    if $1; then
        echo "✓ $2 verification passed"
    else
        echo "✗ $2 verification failed"
    fi
}

# Verify Yosys
echo "Verifying Yosys..."
check_command "yosys --version" "Yosys"

# Verify Iverilog
echo "Verifying Iverilog..."
check_command "iverilog -V" "Iverilog"

# Verify gtkwave
echo "Verifying gtkwave..."
check_command "gtkwave --version" "gtkwave"

# Verify ngspice
echo "Verifying ngspice..."
check_command "ngspice -v" "ngspice"

# Verify magic
echo "Verifying magic..."
check_command "magic --version" "magic"

# Verify OpenLANE
echo "Verifying OpenLANE..."
cd $HOME/OpenLane
check_command "make pdk" "OpenLANE PDK setup"
check_command "make test" "OpenLANE test"

echo "Verification complete!"
