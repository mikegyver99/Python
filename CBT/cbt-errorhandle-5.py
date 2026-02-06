# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:30:27 2016

@author: mgarcial
"""
while True:
    try:
        print("Let us solve (x/2) / (x-y)")
        print("Please enter 0 to exit")
        x = float(input("Please enter a value for x:"))
        y = float(input("Please enter a value for y:"))
        if x==0 or y==0:
            break
        z = (x/2) / (x-y)

    except ZeroDivisionError as e:
        print("There was an error in the code")
        print("You keyed in a value that cause zero denominator",str(e))
    except ValueError as e:
        print("There was an error in the code")
        print("You keyed in a value that was text.",str(e))
    except Exception as e:
        print("There was an unknown error in the code")
        print("unknown",str(e))
    else:
        print("Solving x is",x, "and y is",y, "(x/2) / (x-y) is", z)
    finally:
        #cleanup code goes here
        print("Clean Up Code")