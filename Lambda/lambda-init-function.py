# Lab from learn.cantrill.io - not a real application, just a demonstration of Lambda initialization and cold starts.
# Module-level code runs during Lambda initialization (the "init" phase).
# This initialization executes when a new execution environment is created
# (commonly called a cold start). Code at module top-level runs once per
# execution environment and can establish state (e.g., DB connections)
# that persists across subsequent invocations which reuse the same environment.
# If Lambda creates new environments (scaling, container recycling), the
# initialization code runs again for those environments.
import json, os, time, logging

print('Cold Start! .. Loading function')
dbconnected=False # First Run
if dbconnected==False:
  print ("Coldstart DB Connection ... ETA 5s")
  time.sleep(5) # SIMULATE DB CONNECTION TIME
  print ("Connected to DB....")
  dbconnected=True

def lambda_handler(event, context):
  global dbconnected
  if dbconnected==False:
    print ("Connecting to super-secret CATDB ... in handler ETA 5s")
    time.sleep(5) # SIMULATE DB CONNECTION TIME
    print ("Connected to DB....")
    dbconnected=True
    
  if dbconnected==True:
    print ("DB Connected....moving to app code")
    print ("Running application.. something something ... cats & doggos")
    
  return { 'statusCode': 200, 'body': json.dumps('Finished!') }

