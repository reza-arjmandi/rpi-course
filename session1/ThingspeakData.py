######################################################################
#	ThingspeakData.py
#
# This program measure Raspberry pi cpu temprature and then send 
# to thingspeak IOT server for data visualization.
######################################################################

import time, os, urllib, urllib2

DELAY = 15
BASEURL = 'https://api.thingspeak.com/update?api_key={}&field1={}'
KEY = '7ZJO38PBX7NFQH8K'

def sendData(temp):
	completeUrl = BASEURL.format(KEY, temp)
    	response = urllib2.urlopen(url=completeUrl)
    	print(response.read())

def cpuTemp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    temperature = dev.read()[5:-3]
    return temperature

while True:
    temp = cpuTemp()
    print("CPU Temp (C): {}".format(temp))
    sendData(temp)
    time.sleep(DELAY)
