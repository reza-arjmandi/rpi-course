######################################################################
#       Touch_Keypad.py
#
# This program read touch keypad and print lable of pressed button
######################################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def ReadKeyPad():
	keyState = 0
	for i in range(1, 17):
		GPIO.output(18, 0)
		if(GPIO.input(23) == 0):
			keyState=i
		GPIO.output(18, 1)
	return keyState

lastKey = -1
while 1:
	key = ReadKeyPad()
	if(key != lastKey and key > 0):
		print(key)
		lastKey = key
	time.sleep(0.1)

