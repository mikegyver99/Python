# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:43:29 2016

@author: mgarcial
"""
while True:
    try:
        print("Let us solve (x/2) / (x-y)")
        print("Please enter 0 to exit")
        x = float(input("Please enter a value for x:"))
        y = float(input("Please enter a value for y:"))
        if x==0 or y==0:
            break
        z = (x/2) / (x-y)

        print("Solving x is",x, "and y is",y, "(x/2) / (x-y) is", z)
    except Exception as e:
        print("There was an error in the code.", e)