'''
CoroBot Spark Sensor Display Units Radio Buttons
Developer: CoroWare
Date: 20, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui

class UnitRadioWidget(QtGui.QWidget):
    def __init__(self, parent, option1 = "in", option2 = "cm"):
        QtGui.QWidget.__init__(self)
        self.option1=option1
        self.option2=option2
        
        self.option1box=QtGui.QRadioButton(self.option1)
        self.option2box=QtGui.QRadioButton(self.option2)
        '''Inches are default Unit'''
        self.option1box.setChecked(True)
        #self.option2box.setChecked(True)
        
        self.grid=QtGui.QGridLayout()
        self.grid.addWidget(self.option1box,0,0)
        self.grid.addWidget(self.option2box,0,1)
        self.setLayout(self.grid)