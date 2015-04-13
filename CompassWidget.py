'''
CoroBot Compass Widget
This is a general pointer widget that displays orientation
of a compass on a compass equiped robot. 
Developer: CoroWare
Date: 19, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

Copyright (c) 2015

'''
from PySide import QtCore, QtGui

class CompassWidget(QtGui.QWidget):
    '''
    Compass widget that is used for indicating orientation of the robot
    relative to the readings of the magnetometer of the IMU. Although the end
    purpose of this widget is intended for the use of indicating direction, it
    can be used for any other purpose the author sees fit.
    '''

    directionPointer = QtGui.QPolygon([
                                       QtCore.QPoint(7,8),
                                       QtCore.QPoint(-7,8),
                                       QtCore.QPoint(0,-40)])
    pointerColor = QtGui.QColor(255,0,0)
    
    def __init__(self,parent):
        '''Method that is called when the class is created.'''
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Compass')
        
    def paintEvent(self,event):
        '''Indicator Object'''

        side = min(self.width(), self.height())
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
