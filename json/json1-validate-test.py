# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:35:41 2016

@author: Michael Garcia garciamj@eou.edu
"""

import json
import datetime
import re
import urllib

file = "2.json"
#open a file
try:
    json_file = open(file)
    json_file_dict = json.load(json_file)
    json_file_str = json.dumps(json_file_dict)
except ValueError:
    print("ERROR: Input is not valid JSON Data")

