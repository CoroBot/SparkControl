'''
CoroBot Digital Display for Sensor Data
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore, QtGui
import time


class DigitalDisplay(QtGui.QWidget):
    def __init__(self, parent, sensor_name='Sensor', Units='cm'):
        QtGui.QWidget.__init__(self)
        self.sensor_name = sensor_name
        self.setup_UI()

    def setup_UI(self):
        self.displayname = QtGui.QLabel(self.sensor_name)
        self.sensordisplay = QtGui.QLCDNumber(self)
        self.sensordisplay.setDigitCount(8)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)
        self.palette = self.palette()
        self.palette.setColor(self.palette.WindowText,
                              QtGui.QColor(255, 0, 0))
        self.setPalette(self.palette)
        self.displayLayout = QtGui.QGridLayout(self)
        self.displayLayout.addWidget(self.sensordisplay, 0, 0)
        self.setLayout(self.displayLayout)

    def update_display(self):
        current_time = time.strftime('%H:%M:%S')
        self.sensordisplay.display(current_time)
