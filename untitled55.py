# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:24:13 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-25,y-1,z-25,x+25,y-1,z+25,155)