######################################################################
#	InternetSensor.py
#
# This program measure Raspberry pi cpu temprature and then send
# it with a dweet.io service.
######################################################################

import os, time
import urllib2

def CpuTemp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    temp = dev.read()[5:-3]
    return temp

while True:
    temp = CpuTemp()
    print("Raspberry Pi Temp:", temp)
    urllib2.urlopen("https://dweet.io/dweet/for/RpiCourseDweet?temp={}".format(temp))
    time.sleep(1)