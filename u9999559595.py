# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:25:52 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getPos()
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y.hut.pos.z
        blockID=mc.getBlock(x,y,z)
        print("你獵到ID:"+str(blockID)+"的方塊")