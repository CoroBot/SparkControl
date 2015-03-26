'''
CoroBot iPython terminal widget
Developer: CoroWare Robotics Solutions Group
Date 22 March, 2015
Version 0.01

Author: Cameron Owens <cowens@coroware.com>

'''
import sys
from PySide import QtCore, QtGui
#from IPython.qt.console.ipython_widget import IPythonWidget
from IPython.qt.inprocess import QtInProcessKernelManager
from IPython.qt.console.rich_ipython_widget import RichIPythonWidget
class iPythonTerminalWidget(QtGui.QWidget):

    #Initialize/Constructor Method
    def __init__(self,partent):
        kernel_manager=QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel=kernel_manager.kernel
        kernel.gui ='qt'

        kernel_client=kernel_manager.client()
        kernel_client.start_channels()

        QtGui.QWidget.__init__(self)
        displayname=QtGui.QLabel('iPython Terminal Widget')
        mainlayout=QtGui.QGridLayout(self)
#        console=IPythonWidget(self)
        console=RichIPythonWidget(self)
        console.kernel_manager=kernel_manager
        console.kernel_client=kernel_client
        console.exit_requested.connect(self.stop)

        mainlayout.addWidget(console,0,0)
    def stop():
        kernel_client.stop_channels()
        kernel_manager.shutdown_kernel()
        sys.exit()

