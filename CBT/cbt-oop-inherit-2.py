# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 13:48:57 2016

@author: mgarcial
"""

class Shape:
    def __init__(self):
        self.color = "Red"
        self.sides = 0
        
class Square(Shape):
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width = w
        
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.color = c

sq1 = Square(5, "Blue")
sq2 = Square(9, "Green")

circle1 = Circle(12, "Yellow")

print("Square Sizes:",sq1.width, "x",sq1.sides,sq1.color,\
    ",",sq2.width, "x",sq2.sides,sq2.color)

print("Circle:",circle1.radius,circle1.color)