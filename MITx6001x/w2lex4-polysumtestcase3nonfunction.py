# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 23:36:43 2017

@author: Michael Garcia garciamj@eou.edu
Version
Find minimum monthly payment with 12 month payoff 
"""

balance = 472
annualInterestRate = .25
mybalance = balance
mypayment = 0
count = 0

while mybalance > 0:
    #set payment +10
    count += 1   
    mypayment += .01
    #set mybalance intial value
    mybalance = balance
    #loop/count for 12 payments    
    for month in range(12):
        print(mybalance)
        #set new balance after payment
        newbalance = mybalance - mypayment
        #add interest for updated mybalance        
        mybalance = newbalance + (newbalance*(annualInterestRate/12))
        
print("Lowest Payment:",mypayment)


 
"""
def f_mypayment(mybalance, mypayment):
    for i in range(0,12):
        mybalance=(mybalance-mypayment)
        mybalance=(mybalance+((annualInterestRate/12)*mybalance))
    if mybalance <= 0:
        print("Lowest Payment:",mypayment)
    if mybalance >=0:
        mypayment += 10
        return f_mypayment(balance, mypayment)
f_mypayment(3329, 10)
"""