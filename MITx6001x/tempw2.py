# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:38:00 2016

@author: mgarcial
"""

# Explanation: Demonstrates function scope and global variable access:
# `h` prints the global `x`, increments its parameter `y`, and the script
# shows that calling `h(x)` does not modify the global `x` value.

def h(y):
    print(x)
    y = y + 1
x = 5
h(x)
print(x)