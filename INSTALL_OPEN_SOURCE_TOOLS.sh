#!/bin/bash

# Script to install all open-source tools for SoC design

set -e  # Exit on any error

echo "Starting installation of open-source tools..."

# Update package list
echo "Updating package list..."
sudo apt-get update

# Install dependencies for Yosys
echo "Installing dependencies for Yosys..."
sudo apt-get install -y build-essential clang bison flex \
    libreadline-dev gawk tcl-dev libffi-dev git \
    graphviz xdot pkg-config python3 libboost-system-dev \
    libboost-python-dev libboost-filesystem-dev zlib1g-dev

# Install make if not present
sudo apt-get install -y make

# Clone and build Yosys
echo "Cloning and building Yosys..."
git clone https://github.com/YosysHQ/yosys.git
cd yosys
make config-gcc
make
sudo make install
cd ..

# Install Iverilog
echo "Installing Iverilog..."
sudo apt-get install -y iverilog

# Install gtkwave
echo "Installing gtkwave..."
sudo apt-get install -y gtkwave

# Install dependencies for ngspice
echo "Installing dependencies for ngspice..."
sudo apt-get install -y libx11-dev tcl-dev tk-dev libcairo2-dev \
    mesa-common-dev libglu1-mesa-dev libncurses-dev

# Download and build ngspice (assuming ngspice-37.tar.gz is downloaded)
# Note: User needs to download ngspice-37.tar.gz from https://sourceforge.net/projects/ngspice/files/
# For automation, we'll assume it's in the current directory
echo "Please download ngspice-37.tar.gz from https://sourceforge.net/projects/ngspice/files/ and place it in the current directory."
echo "Then run: tar -zxvf ngspice-37.tar.gz && cd ngspice-37 && mkdir release && cd release && ../configure --with-x --with-readline=yes --disable-debug && make && sudo make install"

# Install dependencies for magic
echo "Installing dependencies for magic..."
sudo apt-get install -y m4 tcsh csh libx11-dev tcl-dev tk-dev \
    libcairo2-dev mesa-common-dev libglu1-mesa-dev libncurses-dev

# Clone and build magic
echo "Cloning and building magic..."
git clone https://github.com/RTimothyEdwards/magic
cd magic
./configure
make
sudo make install
cd ..

# Install dependencies for OpenLANE
echo "Installing dependencies for OpenLANE..."
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential python3 python3-venv python3-pip make git
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Install Docker
echo "Installing Docker..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Test Docker
sudo docker run hello-world

# Add user to docker group
sudo groupadd docker || true
sudo usermod -aG docker $USER

echo "Please reboot the system and run 'docker run hello-world' to verify Docker."

# Clone OpenLane
echo "Cloning OpenLane..."
cd $HOME
git clone https://github.com/The-OpenROAD-Project/OpenLane
cd OpenLane
make
make test

echo "Installation complete! Please reboot and run the verification script."
