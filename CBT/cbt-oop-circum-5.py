# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:08:34 2016

@author: mgarcial
"""
import math
import decimal
import random


#create data class
class Circle:
    #add a method to class
    #define a function to calculate circumference
    def calcCircum(self):
        return math.pi * 2 * self.radius
        
    def calcDiam(self):
        return self.radius * 2
        
    def calcArea(self):
        return math.pi * (self.radius ** 2)
        
# Empty List
circles = []
#for loop of range
for i in range(0,10):
    c = Circle() #set data type
    c.radius = random.uniform(1.1,9.5) #call random module set member value
    circles.append(c) #append to list circles

for c in circles:
    print("Circumference",c.calcCircum()) #print circumference
    print("Diameter",c.calcDiam())
    print("Radius",c.radius)
    print("Area",c.calcArea())    