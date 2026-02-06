#!/home/mgarcial/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
usage: json4.py -a "url" -b jsonkey -c jsonsubkey
"""

import json
import datetime
import urllib.request
import sys
import argparse

# Add argparse to grab arguments from the commandline
# set type to be int for systemid
# set type to be str for channels
parser = argparse.ArgumentParser(description='This is a to parse json for url.')
parser.add_argument('-a','--url', type=str, help='url', required=True)
parser.add_argument('-b','--jsonkey', type=str, help='jsonkey', required=True)
parser.add_argument('-c','--jsonsubkey', type=str, help='jsonsubkey')
args = parser.parse_args()

# show values of args
#print("url:",args.url)
#print("jsonkey:",args.jsonkey)
#print("jsonsubkey:",args.jsonsubkey)

#Validate data
try:
    # open url and save to variable
    #json_data = urllib.request.urlopen('http://api.veveo.net/video/data/trends?custid=vvo&fn=get_version_info')
    json_data = urllib.request.urlopen(args.url)
    
    # urlopen returns data in bytes format convert to str utf-8
    str_response = json_data.read().decode('utf-8')
    #load the file in json
    str_response_obj = json.loads(str_response)
    #print(str_response_obj)

    
    # parse the json data result key for "creation_date"
    #json_time = (str_response_obj['result']['creation_date'])
    json_time = (str_response_obj[args.jsonkey][args.jsonsubkey])
    
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
    
    # Print the variables
    #print(diff_time_flt)
    #print(now_time)
    #print(minus_time_str)
    #print(json_time)
except (ValueError, OSError, NameError, KeyError) as err:
    print("ERROR: Input is not valid JSON Data", err)

# Test the values
try:
    if json_time < minus_time_str:
        print("ERROR data is over 12 hours old", json_time,"| Time Difference Hours: ",diff_time)
    else:
        print("OK data is less then 12 hours old", json_time,"| Time Difference Hours: ",diff_time)
except (ValueError, OSError, NameError) as err:
    print("ERROR: Input is not valid",err)