# -*- coding: utf-8 -*-
"""
created on 2026-03-08 20:56:11
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Write a function with random to simulate an election with 3 candidates. Simulate 1000 votes and print the winner.
import random

def rand_87(x):
    chance_87 = random.randint(1, 100)
    if chance_87 in range(1, 88):
        return True
    else:
        return False

def rand_65(x):
    chance_87 = random.randint(1, 100)
    if chance_87 in range(1, 66):
        return True
    else:
        return False

def rand_17(x):
    chance_87 = random.randint(1, 100)
    if chance_87 in range(1, 18):
        return True
    else:
        return False

num_sims = 10_000
a_wins = 0
b_wins = 0
for i in range(num_sims):
    if sum([rand_87(1), rand_65(1), rand_17(1)]) >= 2:
        a_wins += 1
    else:
        b_wins += 1
print(f"Probability A wins: {a_wins / num_sims}")
print(f"Probability B wins: {b_wins / num_sims}")
