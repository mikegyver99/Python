"""
created on 2026-03-07 14:09:26
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
str_num = "3"
num = int(str_num)
print(f"type of objec {type(num)} value: {num}")
print(f"float value {float(num)}")

str1 = "3.14"
num = 6
print(f"{str1} {str(num)}")

prompt = "enter number: "
user_input1 = input(prompt)
user_input2 = input("again " + prompt)
multi_num = int(user_input1) * int(user_input2)
print(f"The product of  {user_input1} and {user_input2} is {str(multi_num)}")