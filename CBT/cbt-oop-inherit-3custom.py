# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:59:54 2016

@author: Michael Garcia garciamj@eou.edu
"""

import math

class Shape:
    def __init__(self):
        self.color = "Red"
        self.sides = 4
    def calcArea(self):
        return(0)

        
class Square(Shape):
    def __init__(self,w,h,c):
        Shape.__init__(self)
        self.width = w
        self.height = h
    def calcArea(self):
        return(self.width*self.height)
        
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.color = c
    def calcArea(self):
        return(math.pi * self.radius**2)
        
sq1 = Square(5,7,"Blue")
sq2 = Square(9,11,"Green")

circle1 = Circle(12,"Yellow")

print("Square Sizes:",sq1.width, "x", sq1.height, "x",sq1.sides,sq1.color,\
    ",",sq2.width,"x",sq2.height, "x",sq2.sides,sq2.color)

print("Circle Radius:",circle1.radius,circle1.color)

print("Area sq1",sq1.calcArea())
print("Area sq2",sq2.calcArea())
print("Area circle1",circle1.calcArea())
