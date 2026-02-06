# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:48:57 2016

@author: mgarcial
"""

class Shape:
    def __init__(self):
        self.color = "Red"
        self.sides = 4
    def calcAreaSqr(self):
        return(self.width*self.height);
        
class Square(Shape):
    def __init__(self,w,h,c):
        Shape.__init__(self)
        self.width = w
        self.height = h
        
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.color = c

sq1 = Square(5,7,"Blue")
sq2 = Square(9,11,"Green")

circle1 = Circle(12,"Yellow")

print("Square Sizes:",sq1.width, "x", sq1.height, "x",sq1.sides,sq1.color,\
    ",",sq2.width,"x",sq2.height, "x",sq2.sides,sq2.color)

print("Circle:",circle1.radius,circle1.color)

print(sq1.calcAreaSqr())