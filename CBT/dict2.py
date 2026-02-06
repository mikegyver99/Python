# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:09:53 2016

@author: mgarcial
"""

dates = {"Jan":1, "Feb":1, "Mar":1,}
print(dates)

#Modify existing Key/Value
newKey = input("Enter key to change:")
raw_newVal = input("Enter the value to change:")
newVal = int(raw_newVal)

dates[newKey] = newVal
print(dates)

#Add new Key/Value
newKey = input("Enter new key to add:")
raw_newVal = input("Enter new value:")
newVal = int(raw_newVal)

dates[newKey] = newVal
print(dates)