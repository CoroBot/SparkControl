#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Solutions <corobot.net>
#
# Distributed under terms of the MIT license.

"""
This is a small widget that displays iportant CPU metrics such as IP Addresses,
video frame rates, network signal strength, and etc. Basically this is a widget
that Cameron thought would be cool so he wrote it.... Deal with it!
"""
import socket
import zmq
from PySide import QtGui, QtCore
import os


class metrics(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUI()

    def setupUI(self):
        self.widget_layout = QtGui.QGridLayout(self)

    def list_of_bots(self):
        self.robot_list_label = QtGui.QLabel('Connected Robot')
        for i in range(0, 255):
            robo_host_name = socket.gethostname('Spark')
        self.available_robot_list = QtGui.QComboBox()
        self.available_robot_list.addItems(self.robot_list.keys())
#    def get_signal_strength(self):
