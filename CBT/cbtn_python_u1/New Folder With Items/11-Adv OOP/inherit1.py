from __future__ import print_function
import math

class Shape():
	def __init__(self):
		self.color = "Red"
		self.sides = 0

class Square(Shape):
	def __init__(self, w, c):
		Shape.__init__(self)
		self.width = w
		self.color = c

sq1 = Square(5, "Blue")
sq2 = Square(9, "Green")

print("Square Sizes:",sq1.width,"x",sq1.sides,sq1.color,
	  ",",sq2.width,"x",sq2.sides,sq2.color)

