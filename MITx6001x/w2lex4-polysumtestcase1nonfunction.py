# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 22:51:29 2017

@author: Michael Garcia garciamj@eou.edu
Version 
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
count=1
months=12 
while months >= 0:
    if count==13:
        print("Remaining balance:",(round(balance,2)))
        break
    else:
        mmp=(monthlyPaymentRate*balance)
        balance=(balance-mmp)
        balance=(balance+((annualInterestRate/12)*balance))
        #print("Month",count,"Remaining balance:",(round(balance,2)))
        months -= 1
        count=count+1 
