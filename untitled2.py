# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:59:21 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(10):
     r=random.randrange(1,7)
     #z+
     if r==1:
      mc.setBlocks(x,y,z,x,y,z-4,1)
      z=z+4
     #z-
     elif r==2:
      mc.setBlocks(x,y,z,x,y,z-4,1)
      z=z-4
     #x+
     elif r==3:
      mc.setBlocks(x,y,z,x+4,y,z,1)
      x=x-4
     #x+
     elif r==4:
      mc.setBlocks(x,y,z,x+4,y,z,1)
      x=x+4           
     #y+
     elif r==5:
      mc.setBlocks(x,y,z,x,y+4,z,1)
      y=y+4
       #y+
     else:
      mc.setBlocks(x,y,z,x,y-4,z,1)
      y=y-4
            
