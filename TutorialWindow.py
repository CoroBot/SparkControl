'''
CoroBot Tutorial Window
This is a general web interface window for the in software tutorials.
Developer: CoroWare Robotics Solutions 
Date: 26, March 2015
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui, QtWebKit
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebSettings

class TutorialWindow(QtGui.QDialog):
    def __init__(self, parent,Title='Tutorial_Name', TutorialBlob='Text Here',TutorialVideo='Insert URL Here'):
        QtGui.QDialog.__init__(self)
        self.WindowLabel = Title
        videoView=QtWebKit.QWebView()
        Settings = videoView.settings()
        Settings.setAttribute(QWebSettings.PluginsEnabled,True)
        videoURL = TutorialVideo
        videoView.load(QUrl(videoURL))
        videoView.show()
        
        layout=QtGui.QGridLayout()
        layout.addWidget(videoView,0,0)
#        layout.addWidget(textBlobWindow,1,0)
        self.setWindowTitle(self.WindowLabel)
        self.setLayout(layout)
