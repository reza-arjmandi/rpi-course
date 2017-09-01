######################################################################
#	WebSensor.py
#
# This program measure Raspberry pi cpu temprature and run web
# application and visualize it with a guage.
######################################################################

import os, time
from bottle import route, run, template

def CpuTemp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    temp = dev.read()[5:-3]
    return temp

@route('/temp')
def Temp():
    return CpuTemp()

@route('/')
def index():
	return template('main.html')

@route('/raphael')
def index():
	return template('raphael.2.1.0.min.js')

@route('/justgage')
def index():
	return template('justgage.1.0.1.min.js')

run(host='192.168.43.49', port=80)
