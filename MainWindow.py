'''
CoroBot Spark Main User Window
Developer: CoroWare
Date: 30, September 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

#Import required modules
import sys
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QTextEdit, \
        QAction, QIcon, QKeySequence, QMessageBox, QAction, QDesktopWidget

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
        '''Self Explainatory: Sets the icon'''
        SparkIcon = QIcon('icon.png') #Make Sure to store icon.png file in same folder as MainUserWindow Script
        self.setWindowIcon(SparkIcon)
        
    def CenterMethod(self):
        '''Method that centers the application on the computer's main display'''
        #Downside of PySide is there is no self.center method of the widget
        #For discusson of this please visit the SparkForum/PySideDevelopment
        qRect=self.frameGeometry()
        centerPoint =QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())
    
    def SetupComponents(self):
        '''Method that creates components attributes of the application'''
        self.MainStatusBar = QStatusBar() #Creates an attribute from a method. Cool stuff
        self.setStatusBar(self.MainStatusBar)
        self.MainStatusBar.showMessage("Welcome!")
        self.CreateMenus()
        self.FileMenuActions()
        self.EditMenuActions()
        self.sensorsMenuActions()
        self.WindowMenuActions()
        self.SourceMenuActions()
        self.HelpMenuActions()
        self.ToolsMenuActions()
        self.TutorialsMenuActions()
         
        #Creation of File Menu and its actions
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.importAction)
        self.fileMenu.addAction(self.exportAction)
        self.fileMenu.addAction(self.exitAction)
           
        #Creation of Source Menu Actions
        self.sourceMenu.addAction(self.viewSource)
        self.sourceMenu.addAction(self.visitGitHub)
        self.sourceMenu.addAction(self.viewAuthors)
           
        #Creation of Help Menu
        #self.helpMenu.addAction(self.welcomeHelp)
        #self.helpMenu.addAction(self.viewDocs)
        #self.helpMenu.addAction(self.viewForum)
        #self.helpMenu.addAction(self.askExperts)
         
        #Creation of Sensor Menus and Actions
        self.ultrasonicMenu.addAction(self.configureUltrasonic)
        self.infraredMenu.addAction(self.configureInfrared)
        self.cameraMenu.addAction(self.configureCamera)
        self.additionalSensorsMenu.addAction(self.configureSensor)
        
    def FileMenuActions(self):
        '''Methods that define actions available to file menu buttons'''
        self.newAction = QAction(QIcon('new.png'), '&New',
                                  self, shortcut=QKeySequence.New,
                                  statusTip="Create a New File",
                                  triggered=self.newFile)
        
        self.openAction = QAction(QIcon('open.png'), '&Open', self,
                                  shortcut = QKeySequence.Open)
        
        self.importAction = QAction(QIcon('import.png'), '&Import',
                                    self)
        
        self.exportAction = QAction(QIcon('export.png'), '&Export', self)
        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        
        
    def EditMenuActions(self):
        '''Methods that define actions available to edit menu buttons'''
        
    def sensorsMenuActions(self):
        '''Methods that define actions avialable to sensor menu buttons'''
        self.configureUltrasonic = QAction('&Configure Ultrasonics', self)
        self.configureInfrared = QAction('&Configure Infrared', self)
        self.configureCamera = QAction('&Configure Camera', self)
        self.configureSensor = QAction('&Configure Sensor', self)
        
    def WindowMenuActions(self):
        '''Methods that define actions available to window menu buttons'''
        
    def SourceMenuActions(self):
        '''Methods that define actions available to source menu buttons'''
        self.viewSource = QAction('&View Source', self)
        self.visitGitHub = QAction('&Visit GitHub', self)
        self.viewAuthors = QAction('&View Authors', self)
        #self.sourceMenu.addAction(self.viewAuthors)
    def HelpMenuActions(self):
        '''Methods that define Actions Available to Help Menu buttons'''
        
    def ToolsMenuActions(self):
        '''Methods that define actions available to Tools Menu Buttons'''
        
    def TutorialsMenuActions(self):
        '''Methods to call Tutorials Menu Actions'''
        
    def newFile(self):
        pass
     
              
    def CreateMenus(self):
        '''Method that creates Menus in Menu Bar'''
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.sensorsMenu = self.menuBar().addMenu("&Sensors")
        self.ultrasonicMenu = self.sensorsMenu.addMenu('Ultrasonic')
        self.infraredMenu =self.sensorsMenu.addMenu('Infrared')
        self.cameraMenu = self.sensorsMenu.addMenu('Camera')
        self.additionalSensorsMenu = self.sensorsMenu.addMenu('Additional Sensor Config')
        self.windowMenu = self.menuBar().addMenu("&Window")4
        self.sourceMenu = self.menuBar().addMenu("&Source")
        self.toolsMenu = self.menuBar().addMenu('&Tools')
        self.tutorialsMenu = self.menuBar().addMenu('Tutorials')
        self.helpMenu = self.menuBar().addMenu("&Help")
        

        
        
if __name__ == '__main__':
    '''It is best practice to use this type of wrapper to in the event that someone else
    uses your code and has this as an import'''
            # Exception Handling
    try:
        SparkControl = QApplication(sys.argv)
        mainWindow = MainUserWindow()
        mainWindow.SetupComponents()
        mainWindow.setIcon()
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