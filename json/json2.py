# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
"""

import json
import datetime
import urllib


# open url and save to file
urlfile = urllib.request.URLopener()
urlfile.retrieve("http://api.veveo.net/video/data/trends?custid=vvo&fn=get_version_info", "file.json")

#open file an parse json
file = 'file.json'
json_file = open(file)
json_data = json.load(json_file)
json_time = (json_data['result']['creation_date'])


# Set current time UTC with "T"
now_time = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")

# Set time 12 hours ago UTC.
minus_time = datetime.datetime.utcnow() - datetime.timedelta(hours=12)

# Set 12 hour time to str
minus_time_str = minus_time.strftime("%Y%m%dT%H%M%S")

# Print the variables
print(now_time)
print(minus_time_str)
print(json_time)

# Test the values
if json_time < minus_time_str:
    print("error data is over 12 hours old", json_time)
else:
    print("OK, date is less then 12 hours old", json_time)
