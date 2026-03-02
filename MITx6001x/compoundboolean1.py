# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Explanation: Demonstrates compound boolean checks to determine the smallest
# of three variables (intended to compare x, y, z). Note: `z` is undefined
# in this snippet so running it will raise a NameError.
x = 11
y = 21


if x < y and x < z:
    print (' x is the least')
elif y < z:
    print ('y is the least')
else:
    print ('z is the least')