# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:13:28 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(10):
    mc.setBlocks(x+i,y-i,z+i,x-i,y-i,z-i,x+i,35)