# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
usage: json2.py -a <url> -f <filetosave>
"""

import json
import datetime
import urllib


# open url and save to variable
json_data = urllib.request.urlopen('http://api.veveo.net/video/data/trends?custid=vvo&fn=get_version_info')
# urlopen returns data in bytes format convert to str utf-8
str_response = json_data.read().decode('utf-8')
#load the file in json
str_response_obj = json.loads(str_response)
#print(str_response_obj)

# parse the json data result key for "creation_date"
json_time = (str_response_obj['result']['creation_date'])


# Set current time UTC with "T" for reference only
now_time = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")

# Set time 12 hours ago UTC.
minus_time = datetime.datetime.utcnow() - datetime.timedelta(hours=12)

# Convert 12 hour time to str with "T" isoFormat
minus_time_str = minus_time.strftime("%Y%m%dT%H%M%S")

# Calculate the difference in hours
diff_time = now_time - json_time
divmod(diff_time.total_seconds(), 60)

# Print the variables
print(now_time)
print(minus_time_str)
print(json_time)

# Test the values
if json_time < minus_time_str:
    print("error data is over 12 hours old", json_time)
else:
    print("OK, date is less then 12 hours old", json_time)
