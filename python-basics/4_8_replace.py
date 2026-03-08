"""
created on 2026-03-07 14:48:30
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""

print("AAA".find("a"))  # outputs -1 as not found

str1 = "Somebody said something to Samatha"
str1_replace = str1.replace("s", "x")
print(str1_replace)

prompt = "Input some letters: "
user_input = input(prompt)
find_input = user_input.find("a")
print(f"found letter \"a\" at index: {find_input} if value is -1 means letter not found")