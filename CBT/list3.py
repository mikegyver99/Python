# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 15:46:48 2016

@author: mgarcial
"""

names = ["Nic", "Lee", "Roger", "Vick", "Ollie", "Bob", "Alice", "Dave"]

print(names)

raw_newIndex = input('Please enter the index to replace:')
newIndex = int(raw_newIndex)

newName = input('Please enter the name to put into index:')

names[newIndex] = newName
print(names)

newName = input('Please enter the name to add to the list:')
names.append(newName)
print(names)

remName = input('Please enter name to remove from the list:')
names.remove(remName)
print(names)