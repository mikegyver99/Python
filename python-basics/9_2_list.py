# -*- coding: utf-8 -*-
"""
created on 2026-03-09 10:36:49
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Make a list of rice and beans.
food = ["rice", "beans"]
print(food)

food.append("broccoli")
print(food)

food.extend(("bread", "pizza"))
print(food)

print(food[0:2])

print(food[-1:])

breakfast = "eggs,fruit,orange juice".split(",")
print(breakfast)
print(len(breakfast))
# List Comprehension
lengths = [len(item) for item in breakfast]
print(lengths)