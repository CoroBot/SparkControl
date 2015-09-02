#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Soluitons <www.CoroBot.net>
#
# Distributed under terms of the MIT license.

"""
This module is for viewing the camera stream from the Raspberry Pi using
ZMQ and PiCamera. This module will be extended to include OpenCV tools.
"""

'''
Standard Python Library Imports
'''

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
