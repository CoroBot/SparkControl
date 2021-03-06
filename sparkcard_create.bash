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

    echo -e $COL_GREEN "Starting the Spark Card build process...."

#echo -e  $COL_WHITE "Entering SuperUser Mode."
 
echo -e $COL_WHITE "Running standard software updates and firmawre update"
$COL_GREEN
sudo apt-get update && sudo apt-get upgrade -y
sudo rpi-update -y

echo "Installing basic required tools"
sudo apt-get install make autotools-dev autoconf automake libtool git build-essential cmake pkg-config -y

echo "Creating a 'Downloads' directory"
cd ~/
mkdir Downloads

echo "Installing Hotspot Support Softwares"
sudo apt-get install hostapd udhcpd
sudo cp /etc/udhcpd.conf /etc/udhcpd_bak.conf
{
	echo "start 192.168.42.2"
	echo "end 192.168.42.20"
	echo "interface wlan0"
	echo "remaining yes"
	echo "opt dns 8.8.8.8.4.2.2.2"
	echo "opt subnet 255.255.255.0"
	echo "opt router 192.168.42.1"
	echo "opt lease 864000"
} > /etc/udhcpd.conf
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
sudo apt-get install python3 python-pyside python3-pyside python3-all-dev python3-zmq python-zmq libzmq-dev python-dev python3-dev libusb-1.0-0-dev libudev-dev python3-picamera python3-dev -y
cd ~/Downloads/
wget https://bootstrap.pypa.io/get-pip.py 
sudo python3 get-pip.py
sudo pip3 install numpy virtualenv virtualenvwrapper pyzmq cython
sudo pip3 install hidapi
echo "Exiting Downloads Folder"
cd ~/

echo "Installing OpenCV dependencies" 
sudo apt-get install cmake  libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libatlas-base-dev gfortran -y

echo "Downloading OpenCV"
cd ~/
git clone https://github.com/Itseez/opencv.git --depth 2
cd opencv
git checkout 3.0.0
cd ~/
git clone https://github.com/Itseez/opencv_contrib.git --depth 2
cd opencv_contrib
git checkout 3.0.0
cd ~/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

echo "Verifying OpenCV is in Python3 Path"
ls -l /usr/local/lib/python3.2/site-packages
sleep 5


echo "Installing ROS Tools"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu rariing main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update && sudo apt-get upgrade -y
cd /Downloads
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz
tar -zxvf setuptools*
sudo python setup.py install
sudo apt-get install python-stdeb
sudo pip install rosdep rosinstall-generator wstool
sudo pip install -U rospkg
sudo apt-get install python-rosdep python-rosinstall-generator build-essential

mkdir ~/ros_catkin_ws && cd ~/ros_catkin_ws
rosinstall_generator ros_comm --rosdistro hydro --deps --wet-only > hydro-ros_comm-wet.rosinstall
wstool init -j8 src hydro-ros_comm-wet.rosinstall
sudo rosdep init
rosdep update
rosdep install  --from-paths src --ignore-src --rosdistro hydro -y --os=debian:wheezy
cd src
wstool rm roslisp
rm -rf roslisp
cd ..
rosdep install --from-paths src --ignore-src --rosdistro hydro -y --os=debian:wheezy
./src/catkin/bin/catkin_make_isolated --install
echo "source ~/ros_catkin_ws/install_isolated/setup.bash" >> .bashrc
source .bashrc



echo "Installing additional applications"
sudo apt-get install emacs vim nmap screen

echo "Installing Hardware Tools for Using GPIO on the Raspberry Pi"
sudo apt-get install python-smbus python3-smbus i2c-tools
exit

