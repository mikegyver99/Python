# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:00:00 2016

@author: mgarcial
"""

from __future__ import print_function

num = 9 # a number greater than 2 but less than 10
prime = True # a boolean to remember if this number is prime or not

for test in range(2,num):
    if num % test == 0 and num != test:
        print(num,'equals',test, '*', num/test)
        prime = False
        break
        
if prime:
    print(num,'is a prime number!')
else:
    print(num,'is not a prime number')