# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:41:59 2016

@author: mgarcial
"""
# Explanation: Attempts to count occurrences of the substring 'bob' in `s`.
# Note: the loop iterates characters, so the conditional `if char == 'bob'`
# will never be true — the intended approach is to check slices of `s`.
numBobs = 0
s = 'bobfdsfsdbobasdfasdbob'
for char in s:
    if char == 'bob':
        numBobs += 1
print('Number of times bob occurs is:: ' + (str(numBobs))) 