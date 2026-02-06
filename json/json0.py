# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:32:06 2016

@author: Michael Garcia garciamj@eou.edu
"""

import json
j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print(j['two'])