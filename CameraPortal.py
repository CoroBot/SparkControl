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
import zmq

robot_address = "http://@192.168.1.130:8000/"


class VideoDisplayPort(QtGui.QWidget):

    def __init__(self, parent, colorMode='RGB'):
        QtGui.QWidget.__init__(self)
#         self.video_size = QSize(320, 240)
        self.setup_ui()
        self.setup_camera()
        self.zmq_setup()
        self.colorMode = colorMode

    def setup_ui(self):
        """Initialize widgets.
        """
        self.videoDisplay = QtGui.QLabel()
#         self.image_label.setFixedSize(self.video_size)
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.addWidget(self.videoDisplay, 0, 0)
        self.setLayout(self.main_layout)

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(robot_address)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)

    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, frame = self.capture.read()
        image = QtGui.QImage(frame)
        self.videoDisplay.setPixmap(QtGui.QPixmap.fromImage(image))

    def zmq_setup(self):
        context = zmq.context()
        socket = context.socket(zmq.SUB)
        socket.connect(robot_address)
