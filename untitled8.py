# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:54:03 2020

@author: appedu
"""



from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
def Tree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
for i in range(10):
    Tree(x+i*5,y,z+0)
    Tree(x+i*5,y,z+5)
    Tree(x+i*5,y,z+10)
    Tree(x+i*5,y,z+15)
    Tree(x+i*5,y,z+20)