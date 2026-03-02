# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:08:12 2016

@author: mgarcial
"""

# Explanation: Defines `printName` which prints a name either in "First Last"
# or "Last, First" order depending on the boolean `reverse` flag.

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
