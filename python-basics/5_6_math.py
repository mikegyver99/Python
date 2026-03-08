"""
created on 2026-03-07 16:38:18
@author: michael garcia mikejgarcia@gmail.com
version 1.0
# """
# prompt = "Enter a number: "
# user_input = float(input(prompt))
# result = round(user_input, 2)
# print(f"{user_input} rounded to 2 decimal places is {result}")


# prompt = "Enter a number: "
# user_input = float(input(prompt))
# result = abs(user_input)
# print(f"The absolute value of {user_input} is {result}")

prompt = "Enter a number: "
user_input = float(input(prompt))
user_input2 = float(input("Next number" + prompt))
result = user_input - user_input2
print(f"The difference between {user_input} and {user_input2} is an integer? {result.is_integer()}")