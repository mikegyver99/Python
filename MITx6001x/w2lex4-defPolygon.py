# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:13:57 2016
Sums the area and lenth of polygon.
n = number of sides
s = length of sides
@author: mgarcial
"""

import math
import decimal

def polysum(n, s):
    myArea = (.25*n*s**2)//(math.tan(math.pi/n))
    myPerimeter = (n*s)**2
    mySum = (myArea + myPerimeter)
    return((mySum))
print(polysum(74, 4))
    

