# -*- coding: utf-8 -*-
"""
created on 2026-03-08 13:04:28
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Write program loop that prompts for integer, if ValueError happens, returns text and trys again.
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         print(f"You entered: {user_input}")
#         break
#     except (ValueError):
#         print("Try again")
    
# Print character and specified index in string
try:
    user_input1 = input("Enter a string: ")
    user_input2 = int(input("Enter a integer: "))
    print(f"{user_input1[user_input2]}")
except ValueError:
    print(f"Enter a number for integer")
except IndexError:
    print(f"Enter a number that is smaller")