#This scrip is to be used for configuring a Raspberry Pi SD Card to be used in a
# for a CoroBot SPark. This script is to be run directly on a Raspberry Pi. An 
# additional tool will later be developed for doing this process from the ground up
# on a users desktop/laptop

#Author: CoroWare Robotics Solutions
#Developer: Cameron Owens <cowens@corowre.com>

echo "Getting System Updates"
sudo apt-get update && sudo apt-get upgrade -y
sudo rpi-update

echo "Getting system dependencies"
sudo apt-get install git build-essential cmake pkg-config libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev libv41-dev libatlas-base-dev gfortran

echo "Getting Python dependencies"
sudo apt-get intall python3 python3-pyside python3-zmq python3-numpy python3-all-dev

#Getting the Pip package manager
echo "Getting the PIP package manger"
mkdir -p ~/Downloads/Pip_Setup
cd ~/Downloads/Pip_Setup
wget https://bootstrap.pypa.io/get-pip.py ~/Downloads/Pip_Setup
sudo python get-pip.py
cd ~/

echo "Installing OpenCV"
wget -O opencv-2.4.10.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.10/opencv-2.4.10.zip/download

unkzip opencv-2.4.10.zip
cd opencv-2.4.10
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON  -D BUILD_EXAMPLES=ON ..

make
make install

echo "Installing ROS Related COMMS Stuff"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu raring main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update && sudo apt-get upgrade
sudo pip install rosdistro
sudo pip install wstool 
cd ~/Downloads
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz
tar xvf setuptools-1.1.6.tar.gz
cd setuptools-1.1.6
sudo python setup.py install
sudo apt-get install python-stdeb python3-stdeb

sudo pip install rosdep
sudo pip install rosinstall-generator
sudo pip install wstool

pip install -U rospkg
sudo apt-get install python-rosdep python-rosinnstall-generator build-essential
