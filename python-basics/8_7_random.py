# -*- coding: utf-8 -*-
"""
created on 2026-03-08 17:28:48
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# write function that simulates a die roll and returns the result.
import random
# def die_roll():
#     roll = random.randint(1, 6)
#     return roll

# print(die_roll())

# write function that simulates a die roll and returns the result. 
# Then write a loop that rolls the die 10,000 times and prints the average of the rolls.
def die_roll():
    roll = random.randint(1, 6)
    return roll

num_rolls = 10_000
total = 0
for roll in range(num_rolls):
    total += die_roll()

avg_roll = (total / num_rolls)
print(f"The average of {num_rolls} rolls is {avg_roll}")