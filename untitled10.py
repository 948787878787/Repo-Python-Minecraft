# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:43:41 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x-1,y-1,z+1,38)
    time.sleep(1)