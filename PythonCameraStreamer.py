#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.
# Author: Cameron Owens
# Developer: CoroWare Robotics Solutions
# Date: August 27, 2015


"""
This Module is for streaming the Raspberry Pi Camera Feed over a network using
ZMQ. This Module is to be run directly on the Raspberry Pi.
"""

#Standard Import of the required modules

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import zmq
import cStringIO as StringIO
import numpy

camera = PiCamera() #This creats a camera object
camera.resolution = (640, 480) # (2592, 1994) 15fps (1920, 1080) 30fps
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Starting up the Camera
time .sleep(0.1)

def main():
    contex = zmq.Context()
    command = ctx.socket(zmq.DEALER)
    command.identity = b"u_watercher"
    command.connect("INSERT IP ADDRESS OF BOT HERE:PORT")

    bcast = context.socket(zmq.SUB)
    bcast.connect(
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port = True);
""" An invinite loop that captures frames as long as there is a next frame to
capture
"""
image = frame.arary # Take the array and put it into a frame object

rawCapture.truncate(0)

