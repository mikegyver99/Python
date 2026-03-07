# Challenge 1: The FizzBuzz Classic
# The Goal: Write a program that prints numbers from 1 to 50.
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".
# What this evaluates: Your understanding of the for loop and if/elif/else conditional logic.

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)