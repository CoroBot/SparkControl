'''
CoroBot Camera Portal
Developer: CoroWare
Date: 20, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>
Python File for Managing and Creating Camera Portal

Copyright (c) 2015

This software is provided 'as-is', without any express or implied warranty. In
no event will the authors be held liable for any damages arising from the use
of this software. 

Permission is granted to anyone to use this software for any purpose, including
commercial application, and to alter it and redistribute it freely, subject to
the following restrictions:
    
    1) The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software in a
    product, acknowledgements to CoroWare Robotics Solutions must be made.

    2) Alteration of source versions must be plainly and clearly marked as
    such, and must not be misrepresented as being the original software.

    3) This notice may not be removed or altered from any source distribution.

'''


import cv2
from PySide import QtCore, QtGui
import numpy
import sys

class VideoDisplayPort(QtGui.QWidget):

    def __init__(self,parent, colorMode = 'RGB'):
        QtGui.QWidget.__init__(self)
#         self.video_size = QSize(320, 240)
        self.setup_ui()
        self.setup_camera()
        self.colorMode = colorMode
    def setup_ui(self):
        """Initialize widgets.
        """
        self.videoDisplay = QtGui.QLabel()
#         self.image_label.setFixedSize(self.video_size)
 
 
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.addWidget(self.videoDisplay, 0,0)
 
        self.setLayout(self.main_layout)
 
    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)
 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)
 
    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        if self.colorMode == 'RGB':
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        elif self.colorMode=='BW':
            frame = cv2.cvtColor(frame, cv2.THRESH_BINARY_INV)
        elif self.colorMode=='TOL_Zero':
            frame = cv2.cvtColor(frame, cv2.THRESH_TOZERO)     
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.videoDisplay.setPixmap(QtGui.QPixmap.fromImage(image))
