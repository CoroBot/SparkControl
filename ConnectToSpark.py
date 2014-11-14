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
        QtGui.QInputDialog.__init__(self)
        self.IPaddressLabel= QtGui.QLabel('Spark IP Address')
        self.IPaddressInput= QtGui.QLineEdit(self)
        self.connectButton = QtGui.QPushButton('Connect')
        self.cancelButton = QtGui.QPushButton('Cancel')
        
        InputdialogLayout = QtGui.QHBoxLayout()
        InputdialogLayout.addWidget(self.IPaddressLabel)
        InputdialogLayout.addWidget(self.IPaddressInput)
        
        DialogButtonLayout = QtGui.QHBoxLayout()
        DialogButtonLayout.addWidget(self.connectButton)
        DialogButtonLayout.addWidget(self.cancelButton)
        
        mainDialogLayout = QtGui.QVBoxLayout
        mainDialogLayout.addWidget(InputdialogLayout)
        mainDialogLayout.addWidget(DialogButtonLayout)
        
        self.setWindowTitle('Connect To CoroBot Spark')
        self.setLayout(mainDialogLayout)
        
        