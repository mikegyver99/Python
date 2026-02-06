from __future__ import print_function
import math

class Shape():
	def __init__(self):
		self.color = "Red"
		self.sides = 0

	def calcArea(self):
		return 0

class Square(Shape):
	def __init__(self, w, c):
		Shape.__init__(self)
		self.width = w
		self.color = c

	def calcArea(self):
			return self.width ** 2

class Circle(Shape):
	def __init__(self, r, c):
		Shape.__init__(self)
		self.radius = r
		self.color = c 

	def calcArea(self):
		return math.pi * (self.radius ** 2)

class Triangle(Shape):
	def __init__(self,s1,s2,s3,c):
		Shape.__init__(self)
		self.s1 = s1
		self.s2 = s2
		self.s3 = s3
		self.color = c

def printArea(s):
	print(s.calcArea())

sq1 = Square(5, "Blue")
sq2 = Square(9, "Green")

circle1 = Circle(10,"Orange")
t1 = Triangle(2,3,4,"Purple")

print("Square Sizes:",sq1.width,"x",sq1.sides,sq1.color,
	  ",",sq2.width,"x",sq2.sides,sq2.color)
print("Circle:",circle1.radius,circle1.color)

printArea(t1)
