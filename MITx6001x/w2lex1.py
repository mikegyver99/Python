# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:30:50 2016

@author: mgarcial
"""
print("Please think of a number between 0 and 100!")
high = 100
low = 0
guess = int((high + low)/2.0)
ans = "z"
while ans != "c":
    print("Is your secret number", guess, end='?')
    print()
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.",end='')
    ans = input("Enter 'c' to indicate I guessed correctly. ")
    if ans != "h" and ans != "l" and ans != "c":
        print("Sorry, I did not understand your input.")
    if ans == "h":
        high = guess
        guess = int((high + low)/2.0)
        
    elif ans == "l":
        low = guess
        guess = int((high + low)/2.0)
        
print("Game over. Your secret number was:", guess)