'''
CoroBot Spark Main User Window
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore, QtGui

class DigitalDisplay(QtGui.QWidget):
    def __init__(self,parent, sensor_name='Sensor',Units='cm'):
        QtGui.QWidget.__init__(self)
        
        self.sensor_name = sensor_name
        self.displayname= QtGui.QLabel(self.sensor_name)
        
        self.sensordisplay = QtGui.QLCDNumber(self)
        self.sensordisplay.setDigitCount(4)
        
        displayLayout = QtGui.QGridLayout(self)
#          displayLayout.addWidget(self.displayname, 0, 0)
        displayLayout.addWidget(self.sensordisplay, 0,0)
         
        self.setLayout(displayLayout)