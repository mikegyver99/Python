# -*- coding: utf-8 -*-
"""
created on 2026-03-09 19:37:41
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# captains = {}
# captains["Enterprise"] = "Picard"
# captains["Voyger"] = "Janeway"
# captains["Defiant"] = "Sisko"

# if "Enterprise" not in captains:
#     captains["Enterprise"] = "Unknown"
# if "Discovery" not in captains:
#     captains["Discovery"] = "Unknown"    
# print(captains)

captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyger", "Janway"),
        ("Defiant", "Sisko")
    ]
)
print(captains)

# Excerises
# my_dict = {
#     "California": "Sacramento",
#     "Texas": "Austin",
#     "Florida": "Tallahassee",
#     "New York": "Albany",
#     "Illinois": "Springfield",
#     50: "Honolulu"
#     }

# for state, capital in my_dict.items():
#     print(f"The capital of {state} is {capital}")
# states = {
#     "California": {
#         "capital": "Sacramento",
#         "flower": "California Poppy"
#     },
#     "New York": {
#         "capital": "Albany",
#         "flower": "Rose"
#     },
#     "Texas": {
#         "capital": "Austin",
#         "flower": "Bluebonnet"
#     }
# }
# print(states["California"]["flower"])