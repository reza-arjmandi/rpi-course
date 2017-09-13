######################################################################
#       PWM_LED_2.py
#
# This program produce a pwm and control light exposure of an LED
# in such a way that exposure increase until reach to maximum 
# then decrease until reach to minimum periodically 
######################################################################

import RPi.GPIO as GPIO
import time

ledPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

ledPwm = GPIO.PWM(ledPin, 50)
ledPwm.start(100)

while(True):
    print("Increase Mode")
    for i in range(0, 100):
        ledPwm.ChangeDutyCycle(i)
	time.sleep(0.01)

    print("Decrease Mode")
    for i in range(100, 0, -1):
        ledPwm.ChangeDutyCycle(i)
	time.sleep(0.01)
