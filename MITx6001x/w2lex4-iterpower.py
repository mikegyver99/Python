# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:30:54 2016

@author: mgarcial
"""
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    count = exp
    total = base
    if count == 0:
        return 1
    while count > 1:
        total = base*total
        count -= 1
    return total