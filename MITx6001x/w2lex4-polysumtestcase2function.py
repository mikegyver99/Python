# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 23:36:43 2017

@author: Michael Garcia garciamj@eou.edu
Version
Find minimum monthly payment with 12 month payoff 
"""

balance=141
annualInterestRate=.2
mybalance=balance
mypayment=10
 
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