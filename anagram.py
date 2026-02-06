# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:45:04 2017

@author: Michael Garcia garciamj@eou.edu
Version 
"""

from collections import Counter
# defind function to check for anagram
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
# call function with two words to compare print if True or False
if is_anagram("cinema", "iceman"):
    print("True")
else:
    print("False")
