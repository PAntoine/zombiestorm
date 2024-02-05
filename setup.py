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
# Name  : setup.py
# Desc  : The setup iand installation file.
#
# Author: p.antoine
# Date  : 04/02/2024
#--------------------------------------------------------------------------------*
#                     Copyright (c) 2024 Peter Antoine
#                            All rights Reserved.
#                    Released Under the Artistic Licence
#--------------------------------------------------------------------------------*

from version import __version__, __author__, __email__, __url__
from setuptools import setup, find_packages


setup(name='ZombieStorm',
      version=__version__,
      description='Zombie Storm the Awesome Game Designed by Alex Antoine.',
      author=__author__,
      author_email=__email__,
      url=__url__,
      entry_points={'console_scripts': 'zombiestorm=ZombieStorm:startUI'},
      package_data={'': ['version.py', 'assets/players/*.png']},
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      install_requires=['PyQt6']
     )

# vim: ts=4 sw=4 noexpandtab nocin ai
