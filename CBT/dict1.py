# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:05:04 2016

@author: mgarcial
"""

ages = {"Alpha":1, "Beta":2, "Gamma":3, "Delta":4}
print(ages.keys())
x = ages.keys()
print(x[2])

for age in ages:
    print(age,ages[age])