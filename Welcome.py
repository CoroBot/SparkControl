'''
CoroBot Spark Welcome Widget
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

import sys
from PySide.QtCore import Qt
from PySide.QtGui import QApplication, QLabel

class Welcome():
    def DisplayWelcome(self):
        WelcomeScreen = QApplication(sys.argv)
    
        appLabel=QLabel()
        appLabel.setText("Welcome To SparkControl: Python")
    
        appLabel.setAlignment(Qt.AlignCenter)
        appLabel.setWindowTitle("Spark Control Python")
        appLabel.setGeometry(300,300,250,175)
    
    #Draw the label
        appLabel.show()
        
