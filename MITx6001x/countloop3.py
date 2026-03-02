# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:02:12 2016

@author: mgarcial
"""

# Explanation: Demonstrates a while-loop manipulating counters to compute
# a value (numberOfApples) over iterations; contains an apparent bug
# (numberOfLoops is decremented, leading to an infinite loop).

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))