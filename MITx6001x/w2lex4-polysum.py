# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:58:32 2017

@author: Michael Garcia garciamj@eou.edu
Version 
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:13:57 2016
Sums the area and lenth of polygon.
n = number of sides
s = length of sides
@author: mgarcial
"""

import math

def polysum(n, s):
    myArea = (.25*n*s**2)/(math.tan(math.pi/n))
    myPerimeter = (n*s)
    mySum = (myArea + (myPerimeter**2))
    print(myArea)
    print(myPerimeter)
    return round(mySum,4)
print(polysum(24, 18))