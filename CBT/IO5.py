"""I/O example: read name and age, perform simple arithmetic.

Demonstrates using input functions and basic numeric operations
(addition, multiplication, division) on the provided age.
"""

from __future__ import print_function

userName = input('Please enter your name: ' )
age = int(input('Please enter your age: '))

factor = 2
finalAge = age + factor
multAge = age * factor
divAge = float(age) / factor

print('In', factor, 'years you will be', finalAge, 'years old', userName )
print('Your age multilplied by', factor, 'is', multAge )
print('Your age divided by', factor, 'is', divAge )
