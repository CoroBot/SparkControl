'''
CoroBot Spark Four Direction Button Widget
This is a generic widget for creating directional buttons
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide.QtGui import QPushButton, QWidget
from PySide.QtGui import QGridLayout, QSlider, QLabel, QSpinBox
import zmq


class DirectionalButtons(QWidget):
    def __init__(self, parent, North="Up", East="Right",
                 South="Down", West="Left", BoxLabel='Power',
                 valueName='Position'):
        QWidget.__init__(self)
        self.North = North
        self.East = East
        self.South = South
        self.West = West
        self.boxLabel = BoxLabel
        self.createButtons()
        self.sliderStuff()
        self.setup_UI()
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        # self.socket.connect(robot_address)

    def setup_UI(self):
        self.buttonLayout = QGridLayout(self)
        self.buttonLayout.addWidget(self.northButton, 1, 1)
        self.buttonLayout.addWidget(self.eastButton, 2, 2)
        self.buttonLayout.addWidget(self.southButton, 3, 1)
        self.buttonLayout.addWidget(self.westButton, 2, 0)
        self.buttonLayout.addWidget(self.sliderPosition, 1, 3)
        self.buttonLayout.addWidget(self.speedSlider, 2, 3, 3, 3)
        self.buttonLayout.addWidget(self.sliderLabel, 0, 3)
        self.setLayout(self.buttonLayout)

    def createButtons(self):
        self.northButton = QPushButton(self.North)
        self.northButton.clicked.connect(self.upButtonsignal)
        self.southButton = QPushButton(self.South)
        self.southButton.clicked.connect(self.bottomButtonsignal)
        self.eastButton = QPushButton(self.East)
        self.eastButton.clicked.connect(self.rightButtonsignal)
        self.westButton = QPushButton(self.West)
        self.westButton.clicked.connect(self.leftButtonsignal)

    def sliderStuff(self):
        self.speedSlider = QSlider()
        self.speedSlider.setTickPosition(QSlider.TicksRight)
        self.speedSlider.setTickInterval(10)
        self.speedSlider.TicksRight
        self.sliderPosition = QSpinBox()
        self.sliderPosition.setRange(0, 100)
        self.speedSlider.valueChanged.connect(self.sliderPosition.setValue)
        self.sliderPosition.valueChanged.connect(self.speedSlider.setValue)
        self.speedSlider.valueChanged.connect(self.sliderChangeMethod)
        self.SliderValue = self.speedSlider.value()
        self.sliderLabel = QLabel(self.boxLabel)

    def upButtonsignal(self):
        print("Hello World")

    def leftButtonsignal(self):
        print('Left Dir Clicked')

    def bottomButtonsignal(self):
        print('Down button Clicked')

    def rightButtonsignal(self):
        print('Right Button Clicked')

    def sliderChangeMethod(self):
        self.sliderValue = self.speedSlider.value()
        print(self.boxLabel, self.sliderValue)
