# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:42:13 2016

@author: mgarcial
"""

 # Explanation:
 # - A global variable x is defined with value 12.
 # - The function `g(x)` takes a parameter named `x` which shadows the global `x`.
 # - Inside `g`, the parameter `x` is incremented by 1.
 # - `h(y)` is an inner function that closes over (captures) the `x`
 #   from `g`'s scope and returns `x + y`.
 # - `g` returns the result of calling `h(6)`, so `g(x_param)` computes
 #   `(x_param + 1) + 6` using the `x` local to `g`.
 # - Calling `g(x)` with the global `x` (12) yields 19, but that value
 #   is not printed or stored.

x = 12
def g(x):
  x = x + 1
  def h(y):
      return x + y
  return h(6)
g(x)