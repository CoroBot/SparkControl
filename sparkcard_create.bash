# This bash file takes a standard installation of Raspbian and installs the 
# required software for the CoroBot Spark. 

# This scrip file is to be run directly on the Raspberry Pi. 

# Deverloper: CoroWare Robotics Solutions
# Author: Cameron Owens <cowens@coroawre.com>

# Version 0.01
# Date August 24, 2015
echo "Warning, script runs as user"
sudo -s

echo "Running standard software updates and firmawre update"

sudo apt-get update && sudo apt-get upgrade -y
sudo rpi-update -y

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
echo "Exiting Downloads Folder"
cd ~/

echo "Installing ZMQ... The one true message queue."
cd ~/Downloads/
wget http://download.zeromq.org/zeromq-4.1.3.tar.gz
tar -zxvf zeromq-4.1.3.tar.gz
cd zeromq-4.1.3/
./configure
make
sudo make install
sudo ldconfig
echo "Exiting Downloads Folder"
cd ~/

echo "Installing Python and Python related dependencies"
sudo apt-get install python3 python-pyside python3-pyside python3-all-dev -y
cd ~/Downloads/
wget https://bootstrap.pypa.io/get-pip.py 
sudo python3 get-pip.py
sudo pip3 install numpy virtualenv virtualenvwrapper pyzmq -y
echo "Exiting Downloads Folder"
cd ~/

echo "Installing OpenCV dependencies" 
sudo apt-get cmake install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran -y

echo "Downloading OpenCV"
cd ~/Downloads
wget -O opencv-2.4.10.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip/download
unzip opencv-2.4.10.zip
mv opencv-2.4.10 ~/
cd ~/opencv-2.4.10
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON ..
make
sudo make install
sudo ldconfig

echo "Installing ROS Tools"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu rariing main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update && sudo apt-get upgrade
sudo pip install rosdistro -y
sudo pip install wstool -y

exit

