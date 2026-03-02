# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:02:36 2016

@author: mgarcial
"""

# Explanation: Uses an incremental search (`step`) to try to find a real
# square root of `x` within `epsilon` tolerance; reports success or failure.

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))