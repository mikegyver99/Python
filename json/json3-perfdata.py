# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
usage: json2.py -a <url> -f <filetosave>
"""

import json
import datetime
import urllib
import urllib.request
import re


try:
    # open url and save to object
    json_url = urllib.request.urlopen('http://api.veveo.net/video/data/trends?custid=vvo&fn=get_version_info')
    #json_url = urllib.request.urlopen('http://www.example.com')
    # urlopen returns data in bytes format convert to str utf-8
    json_url_str = json_url.read().decode('utf-8')
    #load the file in json format str
    json_url_obj = json.loads(json_url_str)
    # parse the json data result key for "creation_date"
    json_time = (json_url_obj['resul']['creation_date'])
    
    
    
    
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
    diff_time_flt = (diff_time.seconds // 3600)


    print(diff_time_flt)
    # Print the variables
    print(now_time)
    #print(minus_time_str)
    print(json_time)
except (ValueError, OSError, KeyError) as err:
    print("ERROR: Input is not valid JSON",err)


# Test the values
try:
    if json_time < minus_time_str:
        print("ERROR; data is over 12 hours old",json_time,"| Time Difference Hours: ",diff_time_flt)
    else:
        print("OK; date is less then 12 hours old", json_time,"| Time Difference Hours: ",diff_time_flt)
except (ValueError, OSError, NameError) as err:
    print("ERROR: Input is not valid",err)