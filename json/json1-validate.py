# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
"""

import json
import datetime
import re
import urllib

file = "1.json"
#open a file
json_file = open(file)
json_file_dict = json.load(json_file)
json_file_str = json.dumps(json_file_dict)
print(json_file_dict,json_file_str)


#Function to validate if json
def is_json(f):
  try:
    json_object = json.loads(f)
  except (ValueError):
    return False
  return True
  

#validate if json formatted
isinstance(json_file_str, str)

if (is_json(json_file_str)) == False:
    print("ERROR: data is not json, check url output | Time Difference Hours: """)
    exit
else:
    json_time = (json_file_dict["result"]["creation_date"])
    
    # Set current time UTC with "T" for reference only
    now_time = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    
    # Set time 12 hours ago UTC.
    minus_time = datetime.datetime.utcnow() - datetime.timedelta(hours=12)
    
    # Convert 12 hour time to str with "T" isoFormat
    minus_time_str = minus_time.strftime("%Y%m%dT%H%M%S")
    
    
    # Calculate the difference in hours
    # reomve the T from isoformat
    json_time_digits = re.sub('T', r'', json_time)
    now_time_digits = re.sub('T', r'', now_time)
    jt = datetime.datetime.strptime(str(json_time_digits),'%Y%m%d%H%M%S')
    nt = datetime.datetime.strptime(str(now_time_digits),'%Y%m%d%H%M%S')
    
    diff_time = (nt - jt)
    diff_time_int = (diff_time.seconds // 3600)
    
    print(diff_time_int)
    # Print the variables
    print(now_time)
    #print(minus_time_str)
    print(json_time)
    
    
    # Test the values
    if json_time < minus_time_str:
        print("ERROR; data is over 12 hours old",json_time,"| Time Difference Hours: ",diff_time_int)
    else:
        print("OK; date is less then 12 hours old", json_time,"| Time Difference Hours: ",diff_time_int)
