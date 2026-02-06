# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:27:44 2016

@author: mgarcial
"""

x = 81
epsilon = 0.01
guess = (low + high)/2.0
low = 1.0
high = x
num_guess = 0

while abs(guess**2 - x) >= epsilon:
    if guess**2 > x:
        high = guess
    else:
        low = guess
    guess = (high + low)/2.0
    num_guess += 1
print('num_guesses: =', num_guess)
print(guess, 'is close to square root')