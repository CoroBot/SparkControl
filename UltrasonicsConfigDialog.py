'''
Ultrasonic Configuration Dialog
This is a configuration dialog for the Ultrasonic snesors. 
Developer: CoroWare
Date: 12, November 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui

class UltrasonicConfigDialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self)
        buttonLayout = QtGui.QGridLayout(self)
        sensorPinNumber = QtGui.QSpinBox()
        self.sensorPriority_1_Label = QtGui.QLabel('Priority 1')
        self.sensorPriority_2_Label = QtGui.QLabel('Priority 2')
        self.sensorPriority_3_Label = QtGui.QLabel('Priority 3')
        
        self.sensorPriority_1_ComboBox = QtGui.QComboBox(self)
        self.sensorPriority_1_ComboBox.addItem('Front Left')
        self.sensorPriority_1_ComboBox.addItem('Front Right')
        self.sensorPriority_1_ComboBox.addItem('Rear')
        
        self.sensorPriority_2_ComboBox = QtGui.QComboBox(self)
        self.sensorPriority_2_ComboBox.addItem('Front Left')
        self.sensorPriority_2_ComboBox.addItem('Front Right')
        self.sensorPriority_2_ComboBox.addItem('Rear')
        
        self.SaveButton = QtGui.QPushButton("Save")
        
###### Widget Layout Configuration
        gridLayout = QtGui.QGridLayout(self)
        gridLayout.addWidget(self.sensorPriority_1_Label, 0,0)
        gridLayout.addWidget(self.sensorPriority_2_Label, 1,0)
        gridLayout.addWidget(self.sensorPriority_1_ComboBox,0,1)
        gridLayout.addWidget(self.sensorPriority_2_ComboBox, 1,1)
        
        

        self.setWindowTitle('Ultrasonic Config')
        
        
        self.setLayout(gridLayout)