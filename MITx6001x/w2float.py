# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:20:25 2016

@author: mgarcial
"""

num = 100

if num < 0 :
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result