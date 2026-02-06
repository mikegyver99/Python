from __future__ import print_function
import math, random

def calcCircumference(radius):
	return math.pi * 2 * radius
		
class Circle:
	pass

circles = []

for i in range(0,10):
	c = Circle()
	c.radius = random.uniform(1.1, 9.5)
	c.circumference = calcCircumference(c.radius)
	circles.append(c)

for c in circles:
	print("Radius:",c.radius, \
		"circumference:",c.circumference)


