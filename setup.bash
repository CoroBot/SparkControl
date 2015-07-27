# This is the first shell script to automate the installation proces of the
# Spark control application for Linux Targets.

echo "Checking for software updates."
sudo apt-get update && sudo apt-get upgrade -y

echo "Installing Qt and its dependencies"
sudo apt-get install
