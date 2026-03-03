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
    print('f: local x =', x)
x = 5
f(x)
print('module: global x =', x)

def g(y):
    print('g: global x =', x)
    print('g: computed x+1 (uses global) =', x + 1)
x = 5
g(x)
print('module: global x =', x)

def h(y):
    """Return y incremented by one and show local value.

    Prints the local parameter value then returns the incremented
    result so the caller can update the global if desired.
    """
    print('h: local y =', y)
    return y + 1

x = 5
x = h(x)
print('module: global x =', x)