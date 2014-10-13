from PySide.QtCore import *
from PySide.QtGui  import *

import sys

class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.form_widget = FormWidget(self,'Forward','Reverse') 
        self.setCentralWidget(self.form_widget) 


class FormWidget(QWidget):
    def __init__(self, parent, TopButton='up', BottomButton='down'):
        self.TopButton=TopButton
        self.BottomButton=BottomButton 
        super(FormWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton(self.TopButton)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton(self.BottomButton)
        self.layout.addWidget(self.button2)

app = QApplication([])
foo = MyMainWindow()
foo.show()
sys.exit(app.exec_())