# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:02:50 2016

@author: mgarcial
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = 1    
    if a == 1 or b == 1:
        return 1
    if a > b:
        while b > 1:
            if a%b == 0:
                return b
            else:
                if a%(b-x) == 0 and b%(b-x) ==0:
                    return b-x
                else:
                    x += 1
    if b > a:
        while a > 1:
            if b%a == 0:
                return a
            else:
                if b%(a-x) == 0 and a%(a-x) == 0:
                    return a-x
                else:
                    x += 1
gcdIter(110, 190)