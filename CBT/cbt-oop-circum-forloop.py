from __future__ import print_function
import math,random

def calcCircum(radius):
  return math.pi * 2 * radius

class Circle:
  pass

circles = []

for i in range(0,5):
  c = Circle()
  c.radius = random.uniform(1.1,56)
  c.circumference = calcCircum(c.radius)
  circles.append(c)
for c in circles:
  print(c.radius,c.circumference)
