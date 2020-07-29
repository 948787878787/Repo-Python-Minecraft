# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:56:07 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
mc.spawnEntity(x,y,z,63)