# This is the first shell script to automate the installation proces of the
# Spark control application for Linux Targets.

echo "Checking for software updates."
sudo apt-get update && sudo apt-get upgrade -y

echo "Installing GIT...If it's not already installed, shame on you."
sudo apt-get install git

echo "Installing Required dependencies"
sudo apt-get install build-essential libgl1-mesa-dev cmake libqt4-dev libphonon-dev python2.7-dev python3-dev libxml2-dev libxslt1-dev qtmobility-dev

echo "Creating CoroBot Applications Directories"
mkdir -p ~/CoroBot/SparkControl
mkdir -p ~/CoroBot/Temp_Downloads

echo "Installing Pip"
cd ~/CoroBot/Temp_Downloads
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

echo "Installing Pyside"
cd ~/CoroBot/Temp_Downloads
wget https://pypi.python.org/packages/source/P/PySide/PySide-1.2.2.tar.gz
tar -xvzf PySide-1.2.2.tar.gz
cd PySide-1.2.2
python3 setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4

echo "Getting and instally OpenCV"
cd ~/CoroBot
version="$(wget -q -O - http://sourceforge.net/projects/opencvlibrary/files/opencv-unix | egrep -m1 -o '\"[0-9](\.[0-9]+)+' | cut -c2-)"
echo "Installing OpenCV" $version
mkdir OpenCV
cd OpenCV
echo "Removing any pre-installed ffmpeg and x264"
sudo apt-get -qq remove ffmpeg x264 libx264-dev
echo "Installing Dependenices"
sudo apt-get -qq install libopencv-dev build-essential checkinstall cmake pkg-config yasm libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils ffmpeg cmake qt5-default checkinstall
echo "Downloading OpenCV" $version
wget -O OpenCV-$version.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/$version/opencv-"$version".zip/download
echo "Installing OpenCV" $version
unzip OpenCV-$version.zip
cd opencv-$version
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
make -j2
sudo checkinstall
sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
echo "OpenCV" $version "ready to be used"
cd ~/CoroBot/Temp_Downloads

echo "Getting Python Dependencies"
sudo apt-get install python-numpy python3-scipy python3-matplotlib ipython3 ipython3-notebook python3-pandas python3-sympy python3-nose python3-zmq -y

echo "Installing Libsodium and other ZMQ Dependencies"
cd ~/CoroBot/Temp_Downloads
wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
tar -xvzf LATEST.tar.gz
cd libsodium*
./configure
make && make check
sudo make install 
cd ..
 
echo "Installing ZMQ and PYZMQ"
cd ~/CoroBot/Temp_Downloads
wget http://download.zeromq.org/zeromq-4.1.3.tar.gz
tar -xvzf zeromq-4.1.3.tar.gz
cd zeromq-4.1.3/
./configure
make
sudo amek install
ldconfig
cd ..

