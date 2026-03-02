# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:14:04 2016

@author: mgarcial
"""

# Explanation: Prompts for an integer and checks whether it is a perfect cube
# by incrementing ans until ans**3 >= x; reports the cube root if exact.

x = int(input("Enter an interger: "))

ans = 0

while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))