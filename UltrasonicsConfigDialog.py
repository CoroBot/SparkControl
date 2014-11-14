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
        self.sensorPriority_1_Label = QtGui.QLabel("Priority 1")
        self.sensorPriority_2_Label = QtGui.QLabel('Priority 2')
        self.sensorPriority_3_Label = QtGui.QLabel('Priority 3')
        
        self.unitsLabel = QtGui.QLabel('Units')
        self.unitsComboBox = QtGui.QComboBox(self)
        self.unitsComboBox.addItem('cm')
        self.unitsComboBox.addItem('in')
        
        self.sensorPriority_1_ComboBox = QtGui.QComboBox(self)
        self.sensorPriority_1_ComboBox.addItem('Front Left')
        self.sensorPriority_1_ComboBox.addItem('Front Right')
        self.sensorPriority_1_ComboBox.addItem('Rear')
        
        self.sensor_1_safeDist = QtGui.QLineEdit()
         
        self.sensorPriority_2_ComboBox = QtGui.QComboBox(self)
        self.sensorPriority_2_ComboBox.addItem('Front Left')
        self.sensorPriority_2_ComboBox.addItem('Front Right')
        self.sensorPriority_2_ComboBox.addItem('Rear')
        
        self.sensor_2_safeDist = QtGui.QLineEdit()
        
        self.sensorPriority_3_ComboBox = QtGui.QComboBox(self)
        self.sensorPriority_3_ComboBox.addItem('Front Left')
        self.sensorPriority_3_ComboBox.addItem('Front Right')
        self.sensorPriority_3_ComboBox.addItem('Rear')
         
        self.sensor_3_safeDist = QtGui.QLineEdit()
         
        self.SaveButton = QtGui.QPushButton("Save")
         
         
###### Widget Layout Configuration
        self.sensorPriority_1_Label.setBuddy(self.sensorPriority_1_ComboBox)
        
        self.row_1 = QtGui.QHBoxLayout()
        self.row_1.addWidget(self.sensorPriority_1_Label)
        self.row_1.addWidget(self.sensorPriority_1_ComboBox)
        self.row_1.addWidget(self.sensor_1_safeDist)
        
        self.sensorPriority_2_Label.setBuddy(self.sensorPriority_2_ComboBox)
        self.row_2 = QtGui.QHBoxLayout()
        self.row_2.addWidget(self.sensorPriority_2_Label)
        self.row_2.addWidget(self.sensorPriority_2_ComboBox)
        self.row_2.addWidget(self.sensor_2_safeDist)
        
        self.sensorPriority_3_Label.setBuddy(self.sensorPriority_3_ComboBox)
        self.row_3 = QtGui.QHBoxLayout()
        self.row_3.addWidget(self.sensorPriority_3_Label)
        self.row_3.addWidget(self.sensorPriority_3_ComboBox)
        self.row_3.addWidget(self.sensor_3_safeDist)
        
        self.row_4 = QtGui.QHBoxLayout()
        self.row_4.addWidget(self.unitsLabel)
        self.row_4.addWidget(self.unitsComboBox)
        
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addLayout(self.row_1)
        self.mainLayout.addLayout(self.row_2)
        self.mainLayout.addLayout(self.row_3)
        self.mainLayout.addLayout(self.row_4)
        
        self.setWindowTitle('Ultrasonic Config')
        
        
        self.setLayout(self.mainLayout)