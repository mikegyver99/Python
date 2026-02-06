# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:29:38 2016

@author: mgarcial
"""

ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Sqaure root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking ... did you mean", -x, "?")