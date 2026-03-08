# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 20:15:06 2017

@author: Michael Garcia garciamj@eou.edu
Version 
"""
def parse_csv_line(line):
    result = line.split(",")
    return(result)


myline = "Hello, World, Nice, to, meet, you" 
print(parse_csv_line(myline))

