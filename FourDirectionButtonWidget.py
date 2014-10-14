'''
CoroBot Spark Four Direction Button Widget
This is a generic widget for creating directional buttons
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide.QtGui import QPushButton, QWidget, QGridLayout, QSlider, QLabel, QSpinBox
        
class DirectionalButtons(QWidget):
    def __init__(self, parent, North="Up", East="Right", South="Down", West="Left",BoxLabel='Power'):
        QWidget.__init__(self)
        self.North = North
        self.East= East
        self.South = South
        self.West = West
        self.boxLabel = BoxLabel
        buttonLayout = QGridLayout(self)
        northButton = QPushButton(self.North, self)
#        northbutton.click(actionscript)
        
        eastButton = QPushButton(self.East, self)

        southButton = QPushButton(self.South, self)
        
        westButton = QPushButton(self.West, self)
        
        speedSlider = QSlider()
        speedSlider.setTickPosition(QSlider.TicksRight)
        speedSlider.setTickInterval(10)
        speedSlider.TicksRight
        sliderPosition = QSpinBox()
        sliderPosition.setRange(0,101)
        sliderLabel = QLabel(self.boxLabel)
        speedSlider.valueChanged.connect(sliderPosition.setValue)
        sliderPosition.valueChanged.connect(speedSlider.setValue)
        
        
        ##Needs work to fix the layout issues......
        buttonLayout.addWidget(northButton, 1, 1)
        buttonLayout.addWidget(eastButton, 2, 2)
        buttonLayout.addWidget(westButton, 2, 0)
        buttonLayout.addWidget(southButton, 3, 1)
        buttonLayout.addWidget(sliderPosition,1, 3)
        buttonLayout.addWidget(sliderLabel, 0, 3)
        buttonLayout.addWidget(speedSlider, 2, 3, 3,3)
        
        self.setLayout(buttonLayout)
