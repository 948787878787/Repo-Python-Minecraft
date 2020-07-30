# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:25:51 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    for j in range(10):
        color=randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,color)
