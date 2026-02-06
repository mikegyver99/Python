# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:05:13 2016

@author: mgarcial
"""
# calculate if num is prime

from __future__ import print_function

num = 65536

for test in range(2,num):
    if num % test == 0 and num != test:
        print(num,'equals',test, '*', num/test)
        print(num,'is not a prime number.')
        break
else:
    print(num,'is a prime number!')