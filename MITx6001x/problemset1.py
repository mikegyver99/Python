# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:41:59 2016

@author: mgarcial
"""
numBobs = 0
s = 'bobfdsfsdbobasdfasdbob'
for char in s:
    if char == 'bob':
        numBobs += 1
print('Number of times bob occurs is:: ' + (str(numBobs))) 