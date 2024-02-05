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
# Name  : character_sprite.py
# Desc  : This class manages the character sprite.
#
# Author: p.antoine
# Date  : 04/02/2024
#--------------------------------------------------------------------------------*
#                     Copyright (c) 2024 Peter Antoine
#                            All rights Reserved.
#                    Released Under the Artistic Licence
#--------------------------------------------------------------------------------*

import os
from PyQt6.QtGui import QPixmap


class CharacterSprite(object):
	def __init__(self, character_name):
		root = os.path.abspath(os.path.dirname(__file__))

		filename = os.path.join(root, '..', 'assets', 'players', character_name + '.png')

		self.cycle = 0

		self.base_pixmap = QPixmap()
		if self.base_pixmap.load(filename, "PNG"):
			self.loaded = True

			print("---> ", self.base_pixmap.height())
			print("---> ", self.base_pixmap.width())
		else:
			print("Failed to load the filename:" + filename)

	def incrementWalkCycle(self):
		self.cycle = (self.cycle + 1) % 3

	def drawCharacter(self, painter, x, y):
		pix_offset = self.cycle * 17
		painter.drawPixmap(x, y, 32, 36, self.base_pixmap, 0, pix_offset, 16, 17)

# vim: ts=4 sw=4 noexpandtab nocin ai
