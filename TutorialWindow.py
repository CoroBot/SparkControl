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

class TutorialWindow(QtGui.QDialog):
    def __init__(self, parent,Title='Tutorial_Name', TutorialBlob='Text Here',TutorialVideo='Insert URL Here'):
        QtGui.QDialog.__init__(self)
        self.WindowLabel = Title
        videoView=QtWebKit.QWebView()
        videoURL = TutorialVideo
        videoView.load(QUrl(videoURL))
        videoView.show()
        
        textBlob = QtGui.QMessageBox()
        textBlob.setText("hello world")

        videoFrameHolder = QtGui.QScrollArea
        videoFrameHolder.setWidget(videoView)
        textFrameHolder = QtGui.QScrollArea
        textFrameHolder.setWidget(textBlob)

        dialogLayout = QtGui.QVBoxLayout()
        dialogLayout.addWidget(videoFrameHolder)
        dialogLayout.addWidget(textFrameHolder)
        self.setLayout(dialogLayout)
