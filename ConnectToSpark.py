'''
CoroBot Spark IP Address Input
This is a general menu bar widget. 
Developer: CoroWare
Date: 13, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui


class connectToSparkDialog(QtGui.QInputDialog):
    def __init__(self,parent):
        QtGui.QInputDialog.__init__()
        self.IPaddressLabel= QtGui.QLabel('Spark IP Address')
        self.connectButton = QtGui.QPushButton('Connect')
        self.cancelButton = QtGui.QPushButton('Cancel')