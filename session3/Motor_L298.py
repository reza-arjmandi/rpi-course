######################################################################
#       Motor_L298.py
#
# This program control speed and direction of motor DC with L298
# chip
# Run this program with python3. eg: sudo python3 Motor_L298.py
######################################################################

import RPi.GPIO as GPIO
import time

enablePin = 18
inPin1 = 23
inPin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enablePin, GPIO.OUT)
GPIO.setup(inPin1, GPIO.OUT)
GPIO.setup(inPin2, GPIO.OUT)

pwm = GPIO.PWM(enablePin, 500)
pwm.start(0)

def Clockwise():
    GPIO.output(inPin1, True)
    GPIO.output(inPin2, False)

def CounterClockwise():
    GPIO.output(inPin1, False)
    GPIO.output(inPin2, True)

while True:
    cmd = input("command f/r 0..9 e.g. f5: ")
    direction = cmd[0]

    if (direction == "f"):
        Clockwise()
    else:
        CounterClockwise()

    speed = int(cmd[1]) * 10
    pwm.ChangeDutyCycle(speed)
