######################################################################
#       HCSR04.py
#
# This program read data from HCSR04 sensor and then print it.
######################################################################

import RPi.GPIO as GPIO
import time

trigPin = 18
echoPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

def SendTriggerPulse():
    GPIO.output(trigPin, True)
    time.sleep(0.0001)
    GPIO.output(trigPin, False)

def WaitForEcho(value, timeout):
    count = timeout
    while GPIO.input(echoPin) != value and count > 0:
        count = count - 1

def GetDistance():
    SendTriggerPulse()
    WaitForEcho(True, 100000)
    start = time.time()
    WaitForEcho(False, 100000)
    finish = time.time()
    pulseLen = finish - start
    distCm = pulseLen / 0.000058
    distInch = distCm / 2.5
    return (distCm, distInch)

while True:
    print("cm=%f\tinches=%f" % GetDistance())
    time.sleep(1)
