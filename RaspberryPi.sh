#This is the shell script that will start the Raspberry Pi to stream video
#You will need to make sure that this is set up to run each time the 
#Raspberry Pi boots

raspivid -t 999999 -w 1080 -h 720 -fps 25 -hf -b 2000000 -o - | \
gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 \
! gdppay ! tcpserversink host=serverIp port=5000
