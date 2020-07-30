# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:31:08 2020

@author: appedu
"""
a=[1,89,56,9,42,37,6]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print(a)            