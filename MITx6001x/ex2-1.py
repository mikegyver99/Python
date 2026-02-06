# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 23:34:00 2016

@author: mgarcial
"""

cube = 8
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3) - cube <= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
print('Cube root is:', guess)
if 