'''
CoroBot Spark IP Address Input
This is a general menu bar widget. 
Developer: CoroWare
Date: 13, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui


class connectToSparkDialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self)
        self.IPaddressLabel= QtGui.QLabel('Spark IP Address')
        self.IPaddressInput= QtGui.QLineEdit(self)
        self.connectButton = QtGui.QPushButton('Connect')
        self.cancelButton = QtGui.QPushButton('Cancel')
        
        self.InputRow = QtGui.QHBoxLayout()
        self.InputRow.addWidget(self.IPaddressLabel)
        self.InputRow.addWidget(self.IPaddressInput)
        
        self.buttonRow = QtGui.QHBoxLayout()
        self.buttonRow.addWidget(self.cancelButton)
        self.buttonRow.addWidget(self.connectButton)
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addLayout(self.InputRow)
        self.mainLayout.addLayout(self.buttonRow)
        
        self.setWindowTitle('Connect To Spark')
        self.setLayout(self.mainLayout)