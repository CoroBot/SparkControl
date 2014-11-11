'''
CoroBot Camera Portal
Developer: CoroWare
Date: 20, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>


Python File for Managing and Creating Camera Portal
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
            frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
        
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.videoDisplay.setPixmap(QtGui.QPixmap.fromImage(image))
    
    def display_gray_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
        
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.videoDisplay.setPixmap(QtGui.QPixmap.fromImage(image)) 