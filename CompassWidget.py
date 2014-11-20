'''
CoroBot Compass Widget
This is a general pointer widget that displays orientation
of a compass on a compass equiped robot. 
Developer: CoroWare
Date: 19, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide import QtCore, QtGui

class CompassWidget(QtGui.QWidget):
    directionPointer = QtGui.QPolygon([
                                       QtCore.QPoint(7,8),
                                       QtCore.QPoint(-7,8),
                                       QtCore.QPoint(0,-40)])
    pointerColor = QtGui.QColor(255,0,0)
    
    def __init__(self,parent):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle('Compass')
        
    def paintEvent(self,event):
        side = min(self.width(), self.height())
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)