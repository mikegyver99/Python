# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:42:12 2016

@author: mgarcial
"""

s = 'abcdefghi'
print(range(len(s)))
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'i':
        print("There is an a or i")
