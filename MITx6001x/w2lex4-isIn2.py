# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:10:40 2016

@author: mgarcial
"""

def isIn(char, aStr):
    if aStr == '' or (len(aStr) <=1 and aStr != char):
        return False
    m = aStr[len(aStr)//2]
    if char == m:
        return True
    elif char < m:        
        return isIn(char, aStr[:len(aStr)//2])
    elif char > m:
        return isIn(char, aStr[len(aStr)//2:])
        
print(isIn('g', 'abcdefghi'))