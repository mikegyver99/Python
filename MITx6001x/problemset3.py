# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:29:39 2016

@author: mgarcial
"""
s = 'rjrwffoqjjn'
i = 0
j = 1
k = 0
w = s[0]
x = 0
for i in range(len(s)-1):
    if s[i] <= s[i+j]:
        if s[i-1] <= s[i]:
            x = s[k:i+2]
            if len(x) > len(w):
                w = x
        else:
            k = i
            x = s[i:i+2]
            if len(x) > len(w):
                w = x        
print("Longest substring in alphabetical order is:", w)