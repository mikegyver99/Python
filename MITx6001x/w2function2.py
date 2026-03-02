# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:10:07 2016

@author: mgarcial
"""

# Explanation: Contains several small functions illustrating scope rules
# in Python (`f`, `g`, `h`) and how local/global `x` behave when accessed
# or modified inside functions. Some calls will raise UnboundLocalError.

def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

def g(y):
    print(x)
    print(x + 1)
x = 5
g(x)
print(x)

def h(y):
    x = x + 1
x = 5
h(x)
print(x)