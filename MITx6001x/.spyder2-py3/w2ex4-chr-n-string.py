# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:10:07 2016

@author: mgarcial


"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    b = 0
    e = 0
    m = int(len(aStr)/2)
    l = int(len(aStr))
    print(str(char) + " " + str(aStr))
    if char == aStr:
        return True
    if len(aStr) == 0:
        return False
    else:
        def inChar(char, aStr[b:m]):
            if char >= aStr[0] or char <= aStr[m]:
            if char == aStr[0] or char == aStr[m]:
                return True
            else:
                b += 1
                m -= 1
                return inChar(char, aStr[b:m])
        if char >= aStr[m+1] and char <= aStr[l]:
        if char == aStr[m+1] or char == aStr[l]:
            return True
        else:
            e += 1
            m -= 1
            inChar(char, aStr[m:l])
    return isIn
print(isIn('d', 'abcdefghijklmnop'))