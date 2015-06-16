'''
Ultrasonic Configuration Dialog
This is the Master configuration Dialog window for the Camera Settings.
This was originally spread across multiple dialogs and then was condensed
into a single tabed dialog window.
Developer: CoroWare
Date: 12, November 2014 (v0.01)
Date: 11, June 2015 (v0.20)
Version 0.20

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui

class CameraConfigDialog(QtGui.QDialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self,parent)
        tabFrameWork=QtGui.QTabWidget()
        tabFrameWork.addTab(colorMode(), 'Color Mode');
        tabFrameWork.addTab(cameraResolution(), 'Camera Resolution');
        tabFrameWork.addTab(ColorPicker(), 'Color Picker');
        self.tabLayout=QtGui.QVBoxLayout()
        self.tabLayout.addWidget(tabFrameWork)
        self.setLayout(self.tabLayout)
        self.setWindowTitle('Camera Configuration')

class colorMode(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
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
class cameraResolution(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.resolutionComboBox=QtGui.QComboBox(self)
        self.resolutionComboBox.addItem('1920x1080')
        self.resolutionComboBox.addItem('1280x720')
        self.resolutionComboBox.addItem('720x480')
        self.resolutionComboBox.addItem('640x480')
        self.resolutionComboBox.addItem('480x480')
class ColorPicker(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
