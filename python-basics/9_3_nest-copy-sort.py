# -*- coding: utf-8 -*-
"""
created on 2026-03-09 12:37:34
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
data = ((1, 2), (3, 4))
row = 1
for i in data:
    print(f"Row {row} sum: {sum(i)}")
    row += 1

numbers = [4, 3, 2, 1]
numbers_copy = numbers[:]

numbers.sort(reverse=False)
print(f"{numbers} {numbers_copy}")