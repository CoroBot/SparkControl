'''
CoroBot Tutorial Window
This is a general web interface window for the in software tutorials.
Developer: CoroWare Robotics Solutions 
Date: 26, March 2015
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''

from PySide import QtCore, QtGui, QtWebKit

class TutorialWindow(QtGui.QDialog):
    def __init__(self, parent,Title='Tutorial_Name', TutorialBlob='Text Here',TutorialVideo='Insert URL Here'):
        QtGui.QDialog.__init__(self)
        self.WindowLabel = Title
        webWindow=QtWebKit.QWebView()
        webWindow.load(QtCore.QUrl("www.youtube.com"))
        textBlobWindow = QtGui.QTextDocument()
        layout=QtGui.QGridLayout()
        layout.addWidget(webWindow,0,0)
        layout.addWidget(textBlobWindow,1,0)
        webWindow.show()
        self.setWindowTitle(self.WindowLabel)
        self.setLayout(layout)
