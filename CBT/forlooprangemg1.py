# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:14:18 2016

@author: mgarcial
"""

sum = 0 
add = 2
for x in range(1,add):
    print('The current sum is',sum)
    print('How much would you like to add?')
    raw_add = input('(Type 0 to end program): ')
    add = int(raw_add)
    sum = (sum + add)
    x = 1
    if add == 0:
        break