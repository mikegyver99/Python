# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:38:03 2017

@author: mgarcial
"""

# Paste your code into this box
'''
Created on Mon Apr 10 23:36:43 2017

@author: Michael Garcia garciamj@eou.edu
Version
Find minimum monthly payment with 12 month payoff 
'''
mybalance=balance
mypayment=0

while mybalance > 0:
    #set payment +10
    mypayment += 10
    #set mybalance intial value
    mybalance = balance
    #loop/count for 12 payments    
    for month in range(12):
        #print(mybalance)
        #set new balance after payment
        newbalance = mybalance - mypayment
        #add interest for updated mybalance        
        mybalance = newbalance + (newbalance*(annualInterestRate/12))
        
print("Lowest Payment:",mypayment)