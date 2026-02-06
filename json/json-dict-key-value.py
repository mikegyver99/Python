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
parser.add_argument('-u','--url', type=str, help='url')
parser.add_argument('-K','--jsonkey1', type=str, help='jsonkey1')
parser.add_argument('-L','--jsonkey2', type=str, help='jsonkey2')
parser.add_argument('-M','--jsonkey3', type=str, help='jsonkey3')
parser.add_argument('-N','--jsonkey4', type=str, help='jsonkey4')
parser.add_argument('-O','--jsonkey5', type=str, help='jsonkey5')
parser.add_argument('-P','--jsonkey6', type=str, help='jsonkey6')
parser.add_argument('-Q','--jsonkey7', type=str, help='jsonkey7')
parser.add_argument('-R','--jsonkey8', type=str, help='jsonkey8')
parser.add_argument('-r','--regexstr', type=str, help='regexstr')
args = parser.parse_args()

json_data = urllib.request.urlopen("http://condorsearch.veveo.net/search?DS=255&RFTR=256&PN=12&XUA=rovicondor&ECT=5&ver=3.0&RPR=10&os=&XPID=pkg00%40ALL.ROVICSI20&country=USA&w=tom%20cruise&_qa=1")

str_response = json_data.read().decode('utf-8')

str_response_obj = json.loads(str_response)

#jk1 = str('VtvRsps')
#jk2 = str('RC')
#jk3 = str('LRTM')

#print(args.jsonkey1,args.jsonkey2,args.jsonkey3,args.jsonkey4)

#print(str_response_obj[args.jsonkey1][args.jsonkey2][args.jsonkey3])
#print(str_response_obj[args.jsonkey1][args.jsonkey2][args.jsonkey3][args.jsonkey4])
print(str_response_obj[args.jsonkey1][args.jsonkey2][args.jsonkey3][0][args.jsonkey4][args.jsonkey5][0][args.jsonkey6])
