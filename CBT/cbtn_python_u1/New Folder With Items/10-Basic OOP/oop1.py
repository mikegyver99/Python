from __future__ import print_function
import math

def calcCircumference(radius):
	return math.pi * 2 * radius

class Circle:
	pass

circle1 = Circle()

circle1.radius = 4.2

print(circle1.radius)

circle2 = Circle()
circle2.radius = 3.9
print(circle2.radius)

