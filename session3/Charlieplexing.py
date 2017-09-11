######################################################################
#       Charlieplexing.py
#
# This program control 6 LED with 3 GPIO pin for demonstrate
# Charlieplexing methode
######################################################################

import RPi.GPIO as GPIO

pins = [18,23,24]

pinLedStates = [[1,0,-1],
                [0,1,-1],
                [-1,1,0],
                [-1,0,1],
                [1,-1,0],
                [0,-1,1]]
				
GPIO.setmode(GPIO.BCM)

def SetPin(pinIndex, pinState):
    if (pinState == -1):
        GPIO.setup(pins[pinIndex], GPIO.IN)
    else:
        GPIO.setup(pins[pinIndex], GPIO.OUT)
        GPIO.output(pins[pinIndex], pinState)

def LightLed(ledNumber):
    for (pinIndex, pinState) in enumerate(pinLedStates[ledNumber]):
        SetPin(pinIndex, pinState)

SetPin(0, -1)
SetPin(1, -1)
SetPin(2, -1)

while(True):
    x = int(input("Pin 0 to 5: "))
    LightLed(x)
