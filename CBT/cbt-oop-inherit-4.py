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
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width = w
        self.color = c
    def calcArea(self):
        return(self.width*2)
        
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius = r
        self.color = c
    def calcArea(self):
        return(math.pi * self.radius**2)
        
class Triangle(Shape):
    def __init__(self,s1,s2,s3,c):
        Shape.__init__(self)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.color = c
    def calcArea(self):
        return(self.s1 * self.s2 * self.s3)
        
sq1 = Square(5,"Blue")
sq2 = Square(9,"Green")
circle1 = Circle(12,"Yellow")
triangle1 = Triangle(5,5,5,"Orange")

print("Area sq1",sq1.calcArea(),sq1.color)
print("Area sq2",sq2.calcArea(),sq2.color)
print("Area circle1",circle1.calcArea(),circle1.color)
print("Area triangle1",triangle1.calcArea(),triangle1.color)