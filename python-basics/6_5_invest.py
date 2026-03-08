"""
created on 2026-03-07 19:39:07
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
def invest(principal, rate, time):
    """Display year on year growth of an initial investment"""
    for i in range(1, time +1):
        results = principal + (principal * rate)
        principal = results
        print(f"Year {i:}: ${principal}")

principal = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
time = int(input("Enter a number of years: "))

invest(100, .05, 4)
