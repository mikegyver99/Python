# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:45:05 2016

@author: mgarcial
"""
# create a while loop
from __future__ import print_function

sum = 0
add = 1

while add !=0:
    print('The current sum is:',sum)
    print('How much would you like to add?', end='')
    raw_add = input('(Type 0 to end program): ')
    add = int(raw_add)
    sum = sum + add