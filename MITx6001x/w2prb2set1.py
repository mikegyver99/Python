# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:45:28 2017

@author: mgarcial
"""

"""
Created on Wed Apr  5 22:23:08 2017

@author: Michael Garcia garciamj@eou.edu
Version 
test case 1
"""
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