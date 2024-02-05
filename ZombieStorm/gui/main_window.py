#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------*
#	 __________			   ___.   .__			_________ __
#	 \____	  /____   _____\_ |__ |__| ____    /   _____//	|_	___________  _____
#	   /	 //  _ \ /	   \| __ \|  |/ __ \   \_____  \\	__\/  _ \_	__ \/	  \
#	  /		/(	<_> )  Y Y	\ \_\ \  \	___/   /		\|	| (  <_> )	| \/  Y Y  \
#	 /_______ \____/|__|_|	/___  /__|\___	> /_______	/|__|  \____/|__|  |__|_|  /
#			 \/			  \/	\/		  \/		  \/						 \/
#
# Name	: main_window.py
# Desc	:
#
# Author: p.antoine
# Date	: 03/02/2024
#--------------------------------------------------------------------------------*
#					  Copyright (c) 2024 Peter Antoine
#							 All rights Reserved.
#					 Released Under the Artistic Licence
#--------------------------------------------------------------------------------*

import time, threading
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from .character_sprite import CharacterSprite


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.new_char = CharacterSprite('main_guy')

		self.label = QtWidgets.QLabel()
		canvas = QtGui.QPixmap(400, 300)
		canvas.fill(Qt.GlobalColor.black)
		self.label.setPixmap(canvas)
		self.setCentralWidget(self.label)
		self.draw_something()

	def resizeEvent(self, event):
		print("Window has been resized")
		QtWidgets.QMainWindow.resizeEvent(self, event)

	def draw_something(self):
		canvas = self.label.pixmap()
		painter = QtGui.QPainter(canvas)

		self.new_char.drawCharacter(painter, 10, 10)
		self.new_char.incrementWalkCycle()

		painter.end()
		self.label.setPixmap(canvas)

		threading.Timer(1, self.draw_something).start()


# vim: ts=4 sw=4 noexpandtab nocin ai
