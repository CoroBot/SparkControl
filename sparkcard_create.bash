# This bash file takes a standard installation of Raspbian and installs the 
# required software for the CoroBot Spark. 

# This script file is to be run directly on the Raspberry Pi. 
#
# This bash script is distributed under terms of the MIT License

# Deverloper: CoroWare Robotics Solutions
# Author: Cameron Owens <cowens@coroawre.com>

# Version 0.01
# Date August 24, 2015

#Adding Colorized notifications
ESC_SEQ='\x1b['
COL_RESET=$ESC_SEQ"39;49;00m"
COL_RED=$ESC_SEQ"31;01m"
COL_CYAN=$ESC_SEQ"36;01m"
COL_GREEN=$ESC_SEQ"32;01m"
COL_WHITE=$ESC_SEQ"37;01m"

VER="0.01"

echo -n -e "
Welcome to the CoroBot Spark Raspberry Pi Setup Utility version $VER by CoroWare Robotics Solutions. 

In order to continue with the installation process, please review the following license agreement and consult your nearby magic eightball, tea leaves, and local palm readers if you should continue

$COL_WHITE
Please press 'Enter' to continue..."

    read dummy
    more <<EOF

=============================================
Spark Card Create Setup Information
=============================================

EOF

echo -e $COL_RED"
Are you ready to install? (This process can take up to 3 hours) [yes|no]>>>"
read ans
    if [[($ans != "yes") && ($ans != "YES") && ($ans != "Yes") && ($ans != "y") && ($ans != "Y") ]]
    then 
	    echo "Aborting the installation process...."
	    exit 2
    fi

    echo -n -e "
    $COL_GREEN
Starting the Spark Card build process...."

echo $COL_WHITE "Entering SuperUser Mode."
$COL_GREEN
sudo -s
 
echo $COL_WHITE "Running standard software updates and firmawre update"
$COL_GREEN
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

