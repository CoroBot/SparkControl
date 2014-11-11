'''
CoroBot Menu Bar Widget
This is a general menu bar widget. 
Developer: CoroWare
Date: 9, October 2014
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
from PySide import QtCore, QtGui, QtWebKit
#Is there a way to list dependencies for a Python application like in ROS?

class MainMenuBar(QtGui.QMenuBar):
    def SetupComponents(self):
        '''Method that creates components attributes of the application'''
        self.CreateMenus()

         
#######Creation of File Menu and its actions#############################################3
        self.newAction = QtGui.QAction(QtGui.QIcon('new.png'), '&New',
                                  self, shortcut=QtGui.QKeySequence.New,
                                  statusTip="Create a New File")
        self.fileMenu.addAction(self.newAction)
        

        self.openAction = QtGui.QAction(QtGui.QIcon('open.png'), '&Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.setStatusTip('Open New File')
        self.openAction.triggered.connect(self.openDialog)
        
        self.fileMenu.addAction(self.openAction)
        
        self.importAction = QtGui.QAction(QtGui.QIcon('import.png'), '&Import',
                                    self, shortcut=QtGui.QKeySequence.fromString('Ctrl+i'))
        self.fileMenu.addAction(self.importAction)
        
        self.exportAction = QtGui.QAction(QtGui.QIcon('export.png'), '&Export', self)
        self.fileMenu.addAction(self.exportAction)
        
        
        self.exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self, shortcut=QtGui.QKeySequence.Quit)
        self.fileMenu.addAction(self.exitAction)   
        self.connect(self.exitAction, QtCore.SIGNAL("triggered()"),QtGui.qApp, QtCore.SLOT("quit()"))
        
        
#####  Creation of Source Menu Actions        ########################################
        self.viewSource = QtGui.QAction('&View Source', self)
        self.sourceMenu.addAction(self.viewSource)
        
        self.visitGitHub = QtGui.QAction('&Visit GitHub', self) 
        self.sourceMenu.addAction(self.visitGitHub)

        self.viewAuthors = QtGui.QAction('&View Authors', self)  
        self.sourceMenu.addAction(self.viewAuthors)
         

#####  Creation of Help Menu & Actions   ############################################  
        self.welcomeHelp = QtGui.QAction('&Welcome', self)
        self.helpMenu.addAction(self.welcomeHelp)
         
        self.viewDocs =QtGui.QAction('&View Docs', self)
        self.helpMenu.addAction(self.viewDocs)
         
        self.viewForum = QtGui.QAction('View Forum', self)
        self.helpMenu.addAction(self.viewForum)
         
        self.askExperts = QtGui.QAction('&Ask the Experts', self)
        self.helpMenu.addAction(self.askExperts)
          
########Creation of Sensor Menus and Actions#############################################
        self.configureUltrasonic = QtGui.QAction('&Configure Ultrasonic Code', self)
        self.ultrasonicMenu.addAction(self.configureUltrasonic)
        self.setUltrasonicUnits = QtGui.QAction('& Set Units', self)
        self.ultrasonicMenu.addAction(self.setUltrasonicUnits)
        
        self.configureInfrared = QtGui.QAction('&Configure Infrarred Code', self)
        self.infraredMenu.addAction(self.configureInfrared)
        self.setInfraredUnits = QtGui.QAction('& Set Units', self)
        self.infraredMenu.addAction(self.setInfraredUnits)
         
        self.configureCamera = QtGui.QAction('&Configure Camera Code', self)
        self.cameraMenu.addAction(self.configureCamera)
        self.setColorMode = QtGui.QAction('&Set Color Mode', self)
        self.cameraMenu.addAction(self.setColorMode)
        self.setCameraResolution = QtGui.QAction('&Set Camera Resolution', self)
        self.cameraMenu.addAction(self.setCameraResolution)
         
        self.configureRPLidar = QtGui.QAction('Configure RPLidar Code', self)
        self.RPLidarMenu.addAction(self.configureRPLidar)
        self.setRPLidarSampleRate = QtGui.QAction('Set Sample Rate', self)
        self.RPLidarMenu.addAction(self.setRPLidarSampleRate)
         
        self.configureSensor = QtGui.QAction("&Configure New Sensor Code", self)
        self.additionalSensorsMenu.addAction(self.configureSensor)
 
 
# ######  Creation of Window Menu Menus and Actions   ################################
        self.fullScreen = QtGui.QAction('&Full Screen', self)
        self.windowMenu.addAction(self.fullScreen)
         
        self.showHUD = QtGui.QAction('&Show HUD', self)
        self.windowMenu.addAction(self.showHUD)
        
        self.frontLeftUltrasonicDisplay = QtGui.QAction('FLeft Ultrasonic Sensor Display', self)
        self.showSensorPanels.addAction(self.frontLeftUltrasonicDisplay)
        self.frontRightUltrasonicDisplay = QtGui.QAction('Front Right Ultrasonic Sensor Display', self)
        self.showSensorPanels.addAction(self.frontRightUltrasonicDisplay)
        self.frontInfraredDisplay = QtGui.QAction('Front Infrared Display', self)
        self.showSensorPanels.addAction(self.frontInfraredDisplay)
        self.rearUltrasonicDisplay = QtGui.QAction('Rear Ultrasonic Display', self)
        self.showSensorPanels.addAction(self.rearUltrasonicDisplay)
        
##### Creation of Tools Menu Options and  Actions



###### Creation of Tutorials Menu Options and Actions
        '''Getting Started Tuts Actions and Menu Options'''
        self.welcomeSparkControl = QtGui.QAction('Welcome to Spark Control', self, triggered = self.WelcomeAction())
        self.gettingStartedTutsMenu.addAction(self.welcomeSparkControl)
        
        self.firstPythonScript = QtGui.QAction('First Python Script', self)
        self.gettingStartedTutsMenu.addAction(self.firstPythonScript)
        
        '''Sensors Tuts Actions and Menu Options'''
        self.ultrasonicDemo = QtGui.QAction('Ultrasonic Tutorial', self)
        self.sensorsTutsMenu.addAction(self.ultrasonicDemo)
        
        self.PWMDemo = QtGui.QAction('PWM Tutorial', self)
        self.motorsTutsMenu.addAction(self.PWMDemo)
        self.PIDControlDemo = QtGui.QAction('PID Tutorial', self)
        self.motorsTutsMenu.addAction(self.PIDControlDemo)
        
        self.TurningDemo = QtGui.QAction('Turning Tutorial', self)
        self.motorsTutsMenu.addAction(self.TurningDemo)
        
        self.BackgroundSubtractionDemo = QtGui.QAction('Background Subtraction Tutorial', self)
        self.machineVisionTutsMenu.addAction(self.BackgroundSubtractionDemo)
        
        self.OpticalFlowDemo = QtGui.QAction('Optical Flow Tutorial', self)
        self.machineVisionTutsMenu.addAction(self.OpticalFlowDemo)
    
    def WelcomeAction(self):
        pass
##### Create Menu Actions
    def newAction(self):
        pass
    
    def openDialog(self, path=""):
        fileName, _ = QtGui.QFileDialog.getOpenFileName(self, "Open Text Files", "c:/", "Python Files(*.py)")
         
        contents = open(fileName, 'r')
         
        with contents:
            data = contents.read()
            self.textEdit.setText(data)
           
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
        self.showSensorPanels = self.windowMenu.addMenu('Sensor Panels')
        self.showDirectionPanels = self.windowMenu.addMenu('Motion Control Panels')
        self.sourceMenu = self.addMenu("&Source")
        self.toolsMenu = self.addMenu('&Tools')
        self.tutorialsMenu = self.addMenu('Tutorials')
        self.gettingStartedTutsMenu = self.tutorialsMenu.addMenu('Getting Started')
        self.sensorsTutsMenu = self.tutorialsMenu.addMenu('Sensors Tutorials')
        self.motorsTutsMenu = self.tutorialsMenu.addMenu('Motor Control Tutorials')
        self.machineVisionTutsMenu = self.tutorialsMenu.addMenu('Machine Vision Tutorials')
        self.settingsMenu = self.addMenu('Settings')
        self.helpMenu = self.addMenu("&Help")
       

        