#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------*
#    __________            ___.   .__           _________ __
#    \____    /____   _____\_ |__ |__| ____    /   _____//  |_  ___________  _____
#      /     //  _ \ /     \| __ \|  |/ __ \   \_____  \\   __\/  _ \_  __ \/     \
#     /     /(  <_> )  Y Y  \ \_\ \  \  ___/   /        \|  | (  <_> )  | \/  Y Y  \
#    /_______ \____/|__|_|  /___  /__|\___  > /_______  /|__|  \____/|__|  |__|_|  /
#            \/           \/    \/        \/          \/                         \/
#
# Name  : __init__.py
# Desc  : The init file for the gui module.
#
# Author: p.antoine
# Date  : 03/02/2024
#--------------------------------------------------------------------------------*
#                     Copyright (c) 2024 Peter Antoine
#                            All rights Reserved.
#                    Released Under the Artistic Licence
#--------------------------------------------------------------------------------*

import sys
from PyQt6 import QtWidgets
from .main_window import MainWindow


def startUI():
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()

# vim: ts=4 sw=4 noexpandtab nocin ai
