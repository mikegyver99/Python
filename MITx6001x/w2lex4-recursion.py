# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:30:55 2016

@author: mgarcial
"""

def recurPower(base, exp):
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp - 1)
print(recurPower(2, 4))