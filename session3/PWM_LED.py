######################################################################
#       PWM_LED.py
#
# This program produce a pwm and control light exposure of an LED
# with changing it's duty cycle
######################################################################

import RPi.GPIO as GPIO

ledPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

pwmLed = GPIO.PWM(ledPin, 100)
pwmLed.start(100)

while(True):
    dutyStr = input("Please Enter Brightness(0 to 100): ")
    duty = int(dutyStr)
    pwmLed.ChangeDutyCycle(duty)
    
