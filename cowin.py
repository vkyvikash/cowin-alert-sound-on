#!/usr/bin/python

import os
import requests
import time
from datetime import datetime, timedelta
import argparse
from sys import platform

# Speech dispatcher
speech_dispatcher = 'say' # for Mac
if 'linux' in platform:
    speech_dispatcher = 'spd-say'

# Tomorrow
tomorrow = datetime.today() + timedelta(1)
tomorrow = tomorrow.strftime("%d-%m-%Y")

default_age_limit = 18

# Arguments parser
ap = argparse.ArgumentParser()
ap.add_argument("-dist", "--district-id", required=True, help="District ID for your district(you will have to find this id from cowin website)")
ap.add_argument("-age", "--age-limit", required=False, help="Age limit, 18 or 45? Defaults to 18", default=default_age_limit)
args = vars(ap.parse_args())

district_id = int(args['district_id'])
age_limit = int(args['age_limit'])

done = False
while not done:
    #resp = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(district_id, tomorrow), 
    resp = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(district_id, tomorrow), 
                        headers={
                            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                            "accept": "application/json"
                        }
           )
    resp = resp.json()
    sessions = resp.get('sessions', [])
    print ("Vaccine dila de bhagwan!")
    pincodes = [session.get('pincode') for session in sessions if session.get('min_age_limit', default_age_limit) == age_limit]
    if pincodes:
       for pincode in pincodes:
           print (pincode)
           os.system('{} "{}"'.format(speech_dispatcher, pincode))
    time.sleep(10)
    
os.system('{} "your program has finished"'.format(speech_dispatcher))