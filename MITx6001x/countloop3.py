# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:02:12 2016

@author: mgarcial
"""

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))