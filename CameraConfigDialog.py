'''
Ultrasonic Configuration Dialog
This is a configuration dialog for the Ultrasonic snesors. 
Developer: CoroWare
Date: 12, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

Copyright (c)

This software is provided 'as-is', without any express or implied warranty. In
no event will the authors be held liable for any damages arising from the use
of this software. 

Permission is granted to anyone to use this software for any purpose, including
commercial application, and to alter it and redistribute it freely, subject to
the following restrictions:
    
    1) The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software in a
    product, acknowledgements to CoroWare Robotics Solutions must be made.

    2) Alter souce versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3) This notice may not be removed or altered from any source distribution. 

'''

from PySide import QtCore, QtGui

class CameraConfigDialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self)
        
    def configButtons():
        ColorModeComboBox = QtGui.QComboBox(self)
        ColorModeComboBox.addItem('RGB')
        ColorModeComboBox.addItem('Grayscale')
        ColorModeComboBox.add
    def setupUI():
        '''
        Method for establishing Layout UI
        '''
        
        self.ColorModeLabel = QtGui.QLabel("Color Mode")
        
        
        self.ColorModeComboBox = QtGui.QComboBox(self)
        self.ColorModeComboBox.addItem('RGB')
        self.ColorModeComboBox.addItem('Greyscale')
        self.ColorModeComboBox.addItem('Red Filter')
        self.ColorModeComboBox.addItem('Green Filter')
        self.ColorModeComboBox.addItem('Blue Filter')
        self.ColorModeComboBox.addItem('Custom Filter')

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
