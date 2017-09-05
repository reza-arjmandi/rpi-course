######################################################################
#       Keypad.py
#
# This program read matrix keypad and print label of pressed button
######################################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rows = [17, 27, 22, 18]
cols = [23, 24, 25, 8]
keys = [
    ['1', '2', '3','F1'],
    ['4', '5', '6','F2'],
    ['7', '8', '9','F3'],
    ['Stop', '0', 'Start','Enter']]

for rowPin in rows:
    GPIO.setup(rowPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

for colPin in cols:
    GPIO.setup(colPin, GPIO.OUT)

def GetKey():
    key = 0
    for colNum, colPin in enumerate(cols):
        GPIO.output(colPin, 1)
        for rowNum, rowPin in enumerate(rows):
            if GPIO.input(rowPin):
                key = keys[rowNum][colNum]
        GPIO.output(colPin, 0)
    return key

while True:
    key = GetKey()
    if key :
        print(key)
    time.sleep(0.3)
