# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:01:19 2016

@author: mgarcial
"""
s = 'bobnbobnbob'
i = 0
numBobs = 0
for char in s:
    if s[i:i+3] == 'bob':
        numBobs += 1
        i += 1
    else:
        i += 1
print('Number of times bob occurs is: ' + str(numBobs))