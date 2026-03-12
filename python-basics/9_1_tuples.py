# -*- coding: utf-8 -*-
"""
created on 2026-03-08 22:14:08
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
cardinal_numbers = ("first", "second", "third")
print(f"{cardinal_numbers[1]}")

position1, position2, position3 = cardinal_numbers
print(position1, position2, position3, sep="\n")

my_name = tuple("Mike")
print("x" in my_name)

not_my_name = tuple(my_name[1:])
print(not_my_name)