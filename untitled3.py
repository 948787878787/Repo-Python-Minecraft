# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:01:46 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=254,y=69,z=220
mc.player.setTilepos(x,y,z)
