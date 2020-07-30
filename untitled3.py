# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:47:42 2020

@author: appedu
"""

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 50") 
    time.sleep(0.01)