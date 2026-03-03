# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:27:44 2016

@author: mgarcial
"""

# Explanation: Implements a binary search (bisection) method to approximate
# the square root of `x` within `epsilon`. The algorithm maintains a low and
# high bound for the square root and iteratively narrows the range until the
# guess is close enough to the actual square root. 
# It also counts the number of guesses made to reach the approximation.

x = 81
epsilon = 0.01
low = 1.0
high = x
guess = (low + high)/2.0
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