# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 08:35:00 2017

@author: Michael Garcia garciamj@eou.edu
Version 
"""

mydict = { "dev-group1": { "hosts": [ "dev-sys1", "dev-sys2" ] }, "dev-group2": { "hosts": [ "dev-sys3", "dev-sys4" ] } }
for k, v in mydict.items():
    if 'dev-sys1' in v:
        print(k)
