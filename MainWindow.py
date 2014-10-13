'''
CoroBot Spark Main User Window
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QTextEdit, \
        QAction, QIcon, QKeySequence, QMessageBox, QAction, QDesktopWidget, QPushButton, \
        QGridLayout, QDockWidget
from MenuBar import MainMenuBar  
from FourDirectionButtonWidget import DirectionalButtons   
#Import required modules


class MainUserWindow(QMainWindow):
    ''' Main User Window Class, to be the "home" for all widgets'''
    
    #Constructor Function
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Spark Control: Python")
        self.setGeometry(300,300,1080,500) #(x position of center, y position of center, width and height of window)
        self.setMinimumHeight(500)
        self.setMinimumWidth(600)
        
    def setIcon(self):
        '''Self Explainatory: Sets the icon for the application'''
        SparkIcon = QIcon('icon.png') #Make Sure to store icon.png file in same folder as MainUserWindow Script
        self.setWindowIcon(SparkIcon)
        
    def CenterMethod(self):
        '''Method that centers the application on the computer's main display'''
        #Downside of PySide is there is no self.center method of the widget
        #For discussion of this please visit the SparkForum/PySideDevelopment
        qRect=self.frameGeometry()
        centerPoint =QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    
    def CreateStatusBar(self):
        '''Method that creates the status bar. This UI object is used to display general
        information at the bottom of the UI window'''
        self.mainStatusBar = QStatusBar()
        self.mainStatusBar.showMessage("Welcome to Spark Control", 3000)
        self.setStatusBar(self.mainStatusBar)

    def CreateDockWindows(self):
        dock = QDockWidget('Motion Control', self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        
        self.driveButtons = DirectionalButtons(self,'Forward', 'Right', 'Reverse', 'Left')
        dock.setWidget(self.driveButtons)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,dock)
        
        dock =QDockWidget('Camera Control', self)
        self.cameraButtons=DirectionalButtons(self, 'Up', 'Right', 'Down', 'Right')
        dock.setWidget(self.cameraButtons)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea,dock)
if __name__ == '__main__':
    '''It is best practice to use this type of wrapper to in the event that someone else
    uses your code and has this as an import'''
            # Exception Handling
    try:
        SparkControl = QApplication(sys.argv)
        mainWindow = MainUserWindow()
        mainWindow.CreateDockWindows()
        mainWindow.setIcon()
        mainWindow.CreateStatusBar()
        SparkMenu = MainMenuBar()
        SparkMenu.SetupComponents()
        mainWindow.setMenuBar(SparkMenu)
        mainWindow.CenterMethod()
        mainWindow.show()
        SparkControl.exec_()
        sys.exit(0)
        
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print (sys.exc_info()[1])