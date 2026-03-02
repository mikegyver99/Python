# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:47:36 2016

@author: mgarcial
"""

# Explanation: Counts upward from 0 to 5 using a while-loop,
# then prints the final value after the loop finishes.

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)