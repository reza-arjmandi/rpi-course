#!/usr/bin/env python

import time, os, urllib, urllib2 

DELAY = 15 # Seconds




BASE_URL = 'https://api.thingspeak.com/update?api_key={}&field1={}'
KEY = '7ZJO38PBX7NFQH8K'

def send_data(temp): 
	completeUrl = BASE_URL.format(KEY, temp)
    	response = urllib2.urlopen(url=completeUrl)
    	print(response.read())

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return cpu_temp
    
while True:
    temp = cpu_temp()
    print("CPU Temp (C): " + str(temp))
    send_data(temp)
    time.sleep(DELAY)
        
