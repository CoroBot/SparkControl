#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Soltuions
#
# Distributed under terms of the MIT license.

"""
This widget is a widget created to be used within the tab'd dialog window for
the Camera Configuration for CoroBot's using the Spark Control platform

Date: 11, June 2015
Version 0.01
Author Cameron Owens <cowens@coroware.com>
"""

from PySide import QtCore, QtGui
import math

class colorPicker(QtGui.QWidget)
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.redRadioButton=QtGui.QRadioButton('R')
        self.redValue=QtGui.QLineEdit()
        self.greenRadioButton=QtGui.QRadioButton('G')
        self.greenValue=QtGui.QLineEdit()
        self.blueRadioButton=QtGui.QRadioButton('B')

        self.hueRadioButton=QtGui.QRadioButton('H')
        self.hueValue=QtGui.QLineEdit()
        self.saturationRadioButton=QtGui.QRadioButton('S')
        self.saturationValue=QtGui.QLineEdit()
        self.valueRadioButton=QtGui.QRadioButton('V')
        self.valueValue=QtGui.QLineEdit()


