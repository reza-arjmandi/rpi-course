######################################################################
#       Read_Input.py
#
# This program configure gpio 18 as input and then read it
# continusly.
######################################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while(1):
    input_state=GPIO.input(18)
    if(input_state==0):
        print("Button pressed")
        time.sleep(0.2)
