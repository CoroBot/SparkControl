'''
CoroBot Camera Portal
Developer: CoroWare
Date: 20, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>


Python File for Managing and Creating Camera Portal
'''


from PySide import QtCore, QtGui
import sys
import zmq
import Image
import cStringIO as StringIO
import threading

robot_address = "http://@192.168.1.130:8000/"


class VideoDisplayPort(QtGui.QWidget):

    def __init__(self, parent, colorMode='RGB'):
        QtGui.QWidget.__init__(self)
#         self.video_size = QSize(320, 240)
        self.setup_ui()
        self.zmq_setup()
        self.setup_stream()
        self.display_video_stream()

    def setup_ui(self):
        """
        Initialize widgets.
        """
        self.videoDisplay = QtGui.QLabel()
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.addWidget(self.videoDisplay, 0, 0)
        self.setLayout(self.main_layout)

    def setup_stream(self):
        """
        Initialize video stream of jpeg images over zmq.
        """
        incoming_image = self.socket.recv_multipart()
        f = StringIO.StringIO(incoming_image[1])
        recieved_image =Image.open(f).convert('RGB')

    def display_video_stream(self):
        """
        Read frame from camera and repaint QLabel widget.
        """
        #_, frame = self.capture.read()
        image = QtGui.QImage.load(recieved_image)
        self.videoDisplay.setPixmap(QtGui.QPixmap.fromImage(image))


    def zmq_setup(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect(robot_address)
