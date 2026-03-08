# -*- coding: utf-8 -*-
"""
created on 2026-03-08 12:06:33
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
num = int(input("Enter a postive integer: "))
if num > 0:
    for i in range(1, num + 1):
        if (num % i) == 0:
            print(f"{i} is a factor of {num}")

else:
    ("Print enter a postive integer.")