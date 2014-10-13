'''
CoroBot Spark Four Direction Button Widget
This is a generic widget for creating directional buttons
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide.QtGui import QPushButton, QWidget, QGridLayout
        
class DirectionalButtons(QWidget):
    def __init__(self, parent, North="Up", East="Right", South="Down", West="Left"):
        QWidget.__init__(self)
        self.North = North
        self.East= East
        self.South = South
        self.West = West
        
        buttonLayout = QGridLayout(self)
        northButton = QPushButton(self.North, self)
#        northbutton.click(actionscript)
        
        eastButton = QPushButton(self.East, self)

        southButton = QPushButton(self.South, self)
        
        westButton = QPushButton(self.West, self)
        
        buttonLayout.addWidget(northButton, 0, 1)
        buttonLayout.addWidget(eastButton, 1, 2)
        buttonLayout.addWidget(westButton, 1, 0)
        buttonLayout.addWidget(southButton, 2, 1)
        
        self.setLayout(buttonLayout)
