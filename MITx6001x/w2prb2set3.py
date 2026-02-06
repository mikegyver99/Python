# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:47:39 2017

@author: mgarcial
"""

# Paste your code into this box
"""
Created on Mon Apr 10 23:36:43 2017

@author: Michael Garcia garciamj@eou.edu
Version
Find minimum monthly payment with 12 month payoff 
"""
prevBalance = balance
monthIntRate = annualInterestRate / 12.0
count =0 # will count months
lowBound = balance/12.0
upBound = (balance *((1+ monthIntRate)**12))/12.0
guess = round((lowBound + upBound)/2.0, 2)

while prevBalance > 0:
    monthUnPaidBal = prevBalance - guess
    updateBalance = (monthUnPaidBal) + (monthIntRate * monthUnPaidBal)
    prevBalance = round(updateBalance,2)
    count +=1  
    if count==12 and (prevBalance< .10 and prevBalance>-.10):  #after 12 months and prevBalance is +/- .10 then we got it
        break
    elif count ==12: 
        if prevBalance>0: 
            prevBalance = balance # reset prevBalance to original balance
            count=0 # reset count to do another 12 months
            lowBound = guess      
        elif prevBalance<0: 
            prevBalance = balance # reset prevBalance to original balance
            count=0 # reset count to do another 12 months
            upBound = guess
    guess = round((lowBound + upBound)/2.0,2)  


print("Lowest Payment:", guess)