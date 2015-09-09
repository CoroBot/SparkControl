# This is the first shell script to automate the installation proces of the
# Spark control application for Linux Targets.

echo "Checking for software updates."
sudo apt-get clean
sudo apt-get update && sudo apt-get upgrade -y

echo "Installing GIT...If it's not already installed, shame on you."
sudo apt-get install git -y

echo "Installing Required dependencies"
sudo apt-get clean
sudo apt-get install build-essential libgl1-mesa-dev cmake libqt4-dev libphonon-dev python2.7-dev python3.4-dev libxml2-dev libxslt1-dev qtmobility-dev

echo "Creating CoroBot Applications Directories"
mkdir -p ~/CoroBot/SparkControl
mkdir -p ~/CoroBot/Temp_Downloads

echo "Installing Pip"
cd ~/CoroBot/Temp_Downloads
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

echo "Installing Pyside"
sudo apt-get clean
sudo apt-get install python3-pyside -y

echo "Installing Python Tools"
sudo pip3 install numpy cython

echo "Getting and install OpenCV"
cd ~/
echo "Getting OpenCV Dependencies"
sudo apt-get install build-essential cmake git pkg-config libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev libatlas-base-dev gfortran -y 

sudo apt-get install python3.4-dev -y
echo "Cloning OpenCV from Source"
git clone https://github.com/Itseez/opencv.git --depth 2
git clone https://github.com/Itseez/opencv_contrib.git --depth 2
mkdir ~/opencv/build 
cd ~/opencv/build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
make -j4
sudo make install
sudo ldconfig

echo "Getting Python Dependencies"
sudo apt-get clean
sudo apt-get install python-numpy python3-scipy python3-matplotlib ipython3 ipython3-notebook python3-pandas python3-sympy python3-nose python3-zmq -y

echo "Installing Libsodium and other ZMQ Dependencies"
cd ~/CoroBot/Temp_Downloads
wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
tar -xvzf LATEST.tar.gz
cd libsodium*
./configure
make && make check
sudo make install 
sudo ldconfig
cd ..
 
echo "Installing ZMQ and PYZMQ"
cd ~/CoroBot/Temp_Downloads
wget http://download.zeromq.org/zeromq-4.1.3.tar.gz
tar -xvzf zeromq-4.1.3.tar.gz
cd zeromq-4.1.3/
./configure
make
sudo make install
sudo ldconfig
cd ..

