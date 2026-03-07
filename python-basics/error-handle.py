# The Goal: Write a snippet that asks a user for two numbers and divides them.
# Use a try/except block to handle cases where the user enters text instead of a number, or tries to divide by zero.
input_value1 = input("Enter a number: ")
input_value2 = input("Enter a number: ")
try:
	number1 = int(input_value1)
	number2 = int(input_value2)
	if number1 == 0 or number2 ==0:
		print(f"number needs to be greater than 0")
		exit(1)
	else:
		answer = number1 / number2
		print(f"Result of division: {answer}")
		
except ValueError:
	print("Invalid input. Please enter a number.")

