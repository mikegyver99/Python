# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:21:16 2016

@author: mgarcial
"""

def isIn(char, aStr):
    l = int(len(aStr))
    if l%2 == 0:
        m = int((l/2)-1)
    else:
        m = int(l/2)
    if char <= aStr[m]:
        return isIn(isFnd(char, aStr[0:m]))
    else:
        return isIn(isFnd(char, aStr[m:-1]))
        
def isFnd(char, aStr):
    if int(len(aStr)) == 1 and aStr == char:
        return True
    if char == aStr[0] or char == aStr[-1]:
        return True
    else:
        return isFnd(char, aStr[0:-1])

print(isIn('c', 'abcdefghi'))