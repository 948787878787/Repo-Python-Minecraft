# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:35:54 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
name=input('Your Name?')
message=input("message??")
mc.postToChat("["+name+"]"message)