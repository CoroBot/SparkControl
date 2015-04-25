'''
Ultrasonic Configuration Dialog
This is a configuration dialog for the Ultrasonic snesors. 
Developer: CoroWare
Date: 12, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui

class CameraConfigDialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self)
        self.ColorModeLabel = QtGui.QLabel("Color Mode")
        
        
        self.ColorModeComboBox = QtGui.QComboBox(self)
        self.ColorModeComboBox.addItem('RGB')
        self.ColorModeComboBox.addItem('Greyscale')
        self.ColorModeComboBox.addItem('Red Filter')
        self.ColorModeComboBox.addItem('Green Filter')
        self.ColorModeComboBox.addItem('Blue Filter')
        
        self.SaveButton = QtGui.QPushButton("Save")
        self.cancelButton = QtGui.QPushButton('Cancel') 
         
###### Widget Layout Configuration
        self.ColorModeLabel.setBuddy(self.ColorModeComboBox)
        self.row_1 = QtGui.QHBoxLayout()
        self.row_1.addWidget(self.ColorModeLabel)
        self.row_1.addWidget(self.ColorModeComboBox)
        
        self.row_5 = QtGui.QHBoxLayout()
        self.row_5.addWidget(self.cancelButton)
        self.row_5.addWidget(self.SaveButton)
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addLayout(self.row_1)
#        self.mainLayout.addLayout(self.row_2)
#        self.mainLayout.addLayout(self.row_3)
#        self.mainLayout.addLayout(self.row_4)
        self.mainLayout.addLayout(self.row_5)
        
        self.setWindowTitle('Camera Config')
        
        
        self.setLayout(self.mainLayout)
