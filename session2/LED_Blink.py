######################################################################
#       LED_Blink.py
#
# This program measure blink the LED that connected to GPIO 18
# every half second
######################################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

while(True):
    GPIO.output(18,1)
    print("ON")
    time.sleep(0.5)
    GPIO.output(18,0)
    print("OFF")
    time.sleep(0.5)
