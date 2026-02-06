# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:08:34 2016

@author: mgarcial
"""
import math
import decimal
import random

#define a function to calculate circumference
def calcCircum(radius):
    return math.pi * 2 * radius

#create data class
class Circle:
    #add a method to class
    pass

# Empty List
circles = []

#for loop of range
for i in range(0,10):
    c = Circle() #set data type
    c.radius = random.uniform(1,9) #call random module set member value
    c.circumference = calcCircum(c.radius) #calc with function 
    circles.append(c) #append to list circles

for c in circles:
    print("Radius",c.radius, "Circumference",c.circumference) #print circumference
    