# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:58:25 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
X,Y,Z=mc.player.getTilePos
mc.setBlock(x,y,z,198)