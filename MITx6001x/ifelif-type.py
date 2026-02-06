# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:29:20 2016

@author: mgarcial
"""
# == takes presedence over "or" so must test each variable

varA = int(1)
varB = int(2)
if type(varA) == str or type(varB) == str:
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
else:
    print("smaller")