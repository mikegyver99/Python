# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:23:08 2017

@author: Michael Garcia garciamj@eou.edu
Version 
test case 1
"""
count=0
months=12
def mon_payment(balance, annualInterestRate, monthlyPaymentRate):
    global months
    global count
    count=count+1    
    while months > 0:
        mmp=(monthlyPaymentRate*balance)
        balance=(balance-mmp)
        balance=(balance+((annualInterestRate/12)*balance))
        print("Month",count,"Remaining balance:",(round(balance,2)))
        months -= 1
        return mon_payment(balance, annualInterestRate, monthlyPaymentRate)
mon_payment(42, 0.2, 0.04)