# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:42:12 2016

@author: mgarcial
"""

# Explanation: Iterates over the characters of `s` and reports if an 'a'
# or 'i' appears; demonstrates indexing through a string.

s = 'abcdefghi'
print(range(len(s)))
for i in range(len(s)):
    if s[i] == 'a' or s[i] == 'i':
        print("There is an a or i")
