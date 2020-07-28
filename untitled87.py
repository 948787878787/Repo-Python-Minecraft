# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:04:24 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
X,Y,Z=mc.player.getTilePos()
mc.player.setPos(X+0.5,Y,Z+0.5)
mc.setBlock(X,Y-1,Z,11)