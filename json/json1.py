# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:56:54 2016

@author: Michael Garcia garciamj@eou.edu
"""

import json
import datetime

#j = sys.argv[1.json]

file = '1.json'

#open a file
json_file = open(file)
json_data = json.load(json_file)
json_file.close()

# open url


json_time_str = (json_data['result']['creation_date'])

# reomve the T from isoformat
##json_time_digits = re.sub('T', r'', json_time)

now_time = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")

minus_time = datetime.datetime.utcnow() - datetime.timedelta(hours=12)

minus_time_str = minus_time.strftime("%Y%m%dT%H%M%S")

#print(now_time)
print(minus_time_str)
print(json_time_str)
print(type(minus_time_str))

if json_time_str < minus_time_str:
    print("error data is over 12 hours old", json_time_str)
else:
    print("OK, data is less then 12 hours old", json_time_str)


#if [int(json_time_digits) < int(now_time)]:
#    print("error")