# -*- coding: utf-8 -*-
"""
created on 2026-03-08 12:35:03
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Write a program that repeatedly asks the user for some input and quits
# if the user enters "q" or "Q"
# while True:
#     user_input = input("Enter q or Q to quit: ")
#     if user_input in ("q", "Q"):
#         break

# Write a progam that loops over numbers 1 to 50 and all numbers not multiples of 3.
for n in range(1, 51):
    if n % 3 == 0:
        continue
    print(f"{n}")