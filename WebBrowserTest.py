from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

app = QApplication([])

view = QWebView()

url = "https://www.youtube.com/embed/vnfJ1fo14AQ"

view.setWindowTitle(url)
view.load(QUrl(url))
view.show()

app.exec_()
