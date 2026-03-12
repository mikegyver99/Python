# -*- coding: utf-8 -*-
"""
created on 2026-03-09 23:30:25
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# Triva game on state capitals, repeat ask if incorrect. print Goodbye if correct or "exit"
import random

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
}
print(capitals_dict)

state, capital = random.choice(list(capitals_dict.items()))
prompt = (f"What is the capital of {state}?(exit to quit): ")
user_input = ""
while True:
    user_input = input(prompt).lower()
    if user_input == "exit":
        print("Goodbye")
        break
    if user_input.lower() == capital.lower():
        print("Goodbye")
        break