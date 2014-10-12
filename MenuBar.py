'''
CoroBot Menu Bar Widget
This is a general menu bar widget. 
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide.QtGui import  QIcon, QKeySequence, QAction, QMenuBar
#Is there a way to list dependencies for a Python application like in ROS?

class MainMenuBar(QMenuBar):
    def SetupComponents(self):
        '''Method that creates components attributes of the application'''
        self.CreateMenus()

         
#######Creation of File Menu and its actions#############################################
        self.newAction = QAction(QIcon('new.png'), '&New',
                                  self, shortcut=QKeySequence.New,
                                  statusTip="Create a New File")
        self.fileMenu.addAction(self.newAction)

        self.openAction = QAction(QIcon('open.png'), '&Open', self,
                                  shortcut = QKeySequence.Open)
        self.fileMenu.addAction(self.openAction)
        
        self.importAction = QAction(QIcon('import.png'), '&Import',
                                    self)
        self.fileMenu.addAction(self.importAction)
        
        self.exportAction = QAction(QIcon('export.png'), '&Export', self)
        self.fileMenu.addAction(self.exportAction)
        
        
        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.fileMenu.addAction(self.exitAction)   
        
        
        
#####  Creation of Source Menu Actions        ########################################
        self.viewSource = QAction('&View Source', self)
        self.sourceMenu.addAction(self.viewSource)
        
        self.visitGitHub = QAction('&Visit GitHub', self) 
        self.sourceMenu.addAction(self.visitGitHub)

        self.viewAuthors = QAction('&View Authors', self)  
        self.sourceMenu.addAction(self.viewAuthors)
         

#####  Creation of Help Menu & Actions   ############################################  
        self.welcomeHelp = QAction('&Welcome', self)
        self.helpMenu.addAction(self.welcomeHelp)
         
        self.viewDocs =QAction('&View Docs', self)
        self.helpMenu.addAction(self.viewDocs)
         
        self.viewForum = QAction('View Forum', self)
        self.helpMenu.addAction(self.viewForum)
         
        self.askExperts = QAction('&Ask the Experts', self)
        self.helpMenu.addAction(self.askExperts)
          
########Creation of Sensor Menus and Actions#############################################
        self.configureUltrasonic = QAction('&Configure Ultrasonic', self)
        self.ultrasonicMenu.addAction(self.configureUltrasonic)
         
        self.configureInfrared = QAction('&Configure Infrarred', self)
        self.infraredMenu.addAction(self.configureInfrared)
         
        self.configureCamera = QAction('&Configure Camera', self)
        self.cameraMenu.addAction(self.configureCamera)
         
        self.configureRPLidar = QAction('Configure RPLidar', self)
        self.RPLidarMenu.addAction(self.configureRPLidar)
         
        self.configureSensor = QAction('&Configure New Sensor', self)
        self.additionalSensorsMenu.addAction(self.configureSensor)
 
 
# ######  Creation of Window Menu Menus and Actions   ################################
        self.fullScreen = QAction('&Full Screen', self)
        self.windowMenu.addAction(self.fullScreen)
         
        self.showHUD = QAction('&Show HUD', self)
        self.windowMenu.addAction(self.showHUD)
          
##### Creation of Tools Menu Options and  Actions



###### Creation of Tutorials Menu Options and Actions
        '''Getting Started Tuts Actions and Menu Options'''
        self.welcomeSparkControl = QAction('Welcome to Spark Control', self)
        self.gettingStartedTutsMenu.addAction(self.welcomeSparkControl)
        
        self.firstPythonScript = QAction('First Python Script', self)
        self.gettingStartedTutsMenu.addAction(self.firstPythonScript)
        
        '''Sensors Tuts Actions and Menu Options'''
        self.ultrasonicDemo = QAction('Ultrasonic Demo', self)
        self.sensorsTutsMenu.addAction(self.ultrasonicDemo)

#This section of Code is having issues with the               
    def CreateMenus(self):
        '''Method that creates Menus in Menu Bar'''
        self.fileMenu = self.addMenu("&File")
        self.editMenu = self.addMenu("&Edit")
        self.sensorsMenu = self.addMenu("&Sensors")
        self.ultrasonicMenu = self.sensorsMenu.addMenu('Ultrasonic')
        self.infraredMenu =self.sensorsMenu.addMenu('Infrared')
        self.cameraMenu = self.sensorsMenu.addMenu('Camera')
        self.RPLidarMenu = self.sensorsMenu.addMenu('RPLidar')
        self.additionalSensorsMenu = self.sensorsMenu.addMenu('Additional Sensor Config')
        self.windowMenu = self.addMenu("&Window")
        self.sourceMenu = self.addMenu("&Source")
        self.toolsMenu = self.addMenu('&Tools')
        self.tutorialsMenu = self.addMenu('Tutorials')
        self.gettingStartedTutsMenu = self.tutorialsMenu.addMenu('Getting Started')
        self.sensorsTutsMenu = self.tutorialsMenu.addMenu('Learning Sensors')
        self.motorsTutsMenu = self.tutorialsMenu.addMenu('Learning Motor Control')
        self.machineVisionTutsMenu = self.tutorialsMenu.addMenu('Machine Vision')
        self.settingsMenu = self.addMenu('Settings')
        self.helpMenu = self.addMenu("&Help")
       

        