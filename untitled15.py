# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:17:47 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilepos()
mc.setSing(x,y,z,63,0,'[lol]')