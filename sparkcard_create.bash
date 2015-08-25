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
sudo apt-get install -y make autonconf automake libtool git autotools build-essential cmake pkg-config

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
cd ~/

echo "Installing Python and Python related dependencies"
sudo apt-get install python3 python-pyside python3-pyside
wget https://bootstrap.pypa.io/get-pip.py ~/Downloads/
sudo python3 ~/Downloads/get-pip.py
sudo pip3 install numpy virtualenv virtualenvwrapper
sudo pip3 install pyzmq
sudo apt-get install python3-all-dev

echo "Installing OpenCV dependencies" 
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran

echo "Downloading OpenCV"
cd ~/Downloads
wget -O opencv-2.4.10.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip/download
unzip opencv-2.4.10.zip
mv opencv-2.4.10 ~/
cd opencv-2.4.10
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON ..
make
sudo make install
sudo ldconfig



