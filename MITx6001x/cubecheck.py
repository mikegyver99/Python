# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:14:04 2016

@author: mgarcial
"""

x = int(input("Enter an interger: "))

ans = 0

while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))