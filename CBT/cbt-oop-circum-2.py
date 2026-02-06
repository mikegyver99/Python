# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:08:34 2016

@author: mgarcial
"""
import math
import decimal

# define function
def calcCircum(radius):
    return math.pi * 2 * radius
#create a class
class Circle():
    #define class
    pass
#create variable and set type
circle1 = Circle()
circle2 = Circle()
#create a member with property
circle1.radius = 9
circle2.radius = 3

print(calcCircum(circle1.radius))
print(calcCircum(circle2.radius))
