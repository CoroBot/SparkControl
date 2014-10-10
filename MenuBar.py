'''
CoroBot Menu Bar Widget
This is a general menu bar widget. 
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide.QtGui import QApplication, QMainWindow, QStatusBar, QTextEdit, \
        QAction, QIcon, QKeySequence, QMessageBox, QAction, QDesktopWidget, QMenuBar, QLayout
#Is there a way to list dependencies for a python application like in ROS?

class MainMenuBar(QMenuBar):
    def SetupComponents(self):
        '''Method that creates components attributes of the application'''
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
        self.RPLidarMenu.addAction(self.configureRPLidar)
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
        self.configureRPLidar = QAction('&Configure Sensor', self)
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
     
#This section of Code is having issues with the               
    def CreateMenus(self):
        '''Method that creates Menus in Menu Bar'''
        self.fileMenu = self.addMenu("&File")
        self.editMenu = self.addMenu("&Edit")
        self.sensorsMenu = self.addMenu("&Sensors")
        self.ultrasonicMenu = self.sensorsMenu.addMenu('Ultrasonic')
        self.infraredMenu =self.sensorsMenu.addMenu('Infrared')
        self.cameraMenu = self.sensorsMenu.addMenu('Camera')
        self.additionalSensorsMenu = self.sensorsMenu.addMenu('Additional Sensor Config')
        self.windowMenu = self.addMenu("&Window")
        self.sourceMenu = self.addMenu("&Source")
        self.toolsMenu = self.addMenu('&Tools')
        self.tutorialsMenu = self.addMenu('Tutorials')
        self.helpMenu = self.addMenu("&Help")
#         

        