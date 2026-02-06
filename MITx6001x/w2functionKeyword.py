# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:08:12 2016

@author: mgarcial
"""

def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
