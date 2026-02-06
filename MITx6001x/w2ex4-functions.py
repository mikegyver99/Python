# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:42:13 2016

@author: mgarcial
"""

x = 12
def g(x):
  x = x + 1
  def h(y):
      return x + y
  return h(6)
g(x)