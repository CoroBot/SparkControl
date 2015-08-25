# This bash file takes a standard installation of Raspbian and installs the 
# required software for the CoroBot Spark. 

# This scrip file is to be run directly on the Raspberry Pi. 

# Deverloper: CoroWare Robotics Solutions
# Author: Cameron Owens

# Version 0.01
# Date August 24, 2015


echo "Running standard software updates and firmawre update"
sudo apt-get update && sudo apt-get upgrade -y
sudo rpi-update

echo "Installing basic required tools"
sudo apt-get install -y make autonconf automake libtool git autotools

echo "Creating a 'Downloads' directory"
cd ~/
mkdir Downloads

echo "Building libsodium from source prior to installing ZMQ"
cd ~/Downloads
wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
tar -zxvf LATEST.tar.gz
cd libsodium*
./configure 
make && sudo make check
sudo make install

echo "Installing ZMQ... The one true message queue."
wget http://download.zeromq.org/zeromq-4.1.3.tar.gz ~/Downloads/
tar -zxvf ~/Downloads/zeromq-4.1.3.tar.gz
cd ~/Downloads/zeromq-4.1.3*
./configure
make
sudo make install
sudo ldconfig

echo "Installing ZMQ"


echo "Installing Python and Python related dependencies"
sudo apt-get install python3 python-pyside python3-pyside
wget https://bootstrap.pypa.io/get-pip.py ~/Downloads/
sudo python3 ~/Downloads/get-pip.py
sudo pip3 install numpy virtualenv virtualenvwrapper
sudo pip3 install pyzmq
sudo apt-get install python3-all-dev
