# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:30:18 2020

@author: appedu
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create() 
mc.postToChat(87)
while y,z=True:
    x,mc.player.getTilePos()
    mc.postToChat("You are located on X:"+str(x)
                                    +",Y:"+str(y)
                                    +"<Z:"+str(z))