# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:20:34 2016

@author: mgarcial
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    print (str(a) + " " + str(b))
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

gcdRecur(85, 10)