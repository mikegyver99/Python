# def cube(x):
#     """Return the cube of the input number."""
#     product = pow(x, 3)
#     return product
# print(cube(3))

# def greet(x):
#     """Display a greeting."""
#     greet = (f"Hello {x}!")
#     return greet
# print(greet("Mike"))

def convert_cel_to_far(temp):
    """Return the Celsius temperature temp_cel converted to Fahrenheit."""
    F = temp * (9 / 5) + 32
    return F

def convert_far_to_cel(temp):
    """Return the Fahrenheit temperature temp_far converted to Celsius."""
    C = (temp - 32) * (5 / 9)
    return C


prompt = "Enter a temperature in degrees F: "
user_input = input(prompt)
print(f"temperature in Celisus is {convert_far_to_cel(float(user_input))}")


prompt = "Enter a temperature in degrees C: "
user_input = input(prompt)
print(f"temperature in Fahrenheit is {convert_cel_to_far(float(user_input))}")