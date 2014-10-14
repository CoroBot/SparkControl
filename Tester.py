import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()

    def initUI(self):

        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setDigitCount(8)          # change the number of digits displayed
        self.setGeometry(30, 30, 800, 600)
        self.setWindowTitle('Time')

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lcd)
        self.setLayout(vbox)

        self.show()

    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.lcd.display(text)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()