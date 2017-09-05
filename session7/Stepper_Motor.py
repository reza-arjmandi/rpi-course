######################################################################
#       Stepper_Motor.py
#
# This program control the speed and direction of a stepper motor
# that connected to gpio
######################################################################


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

coilA1Pin = 18
coilA2Pin = 23
coilB1Pin = 24
coilB2Pin = 17

GPIO.setup(coilA1Pin, GPIO.OUT)
GPIO.setup(coilA2Pin, GPIO.OUT)
GPIO.setup(coilB1Pin, GPIO.OUT)
GPIO.setup(coilB2Pin, GPIO.OUT)

forwardSeq = ['1010', '0110', '0101', '1001']
reverseSeq = list(forwardSeq) # to copy the list
reverseSeq.reverse()

def Forward(delay, steps):
  for i in range(steps):
    for step in forwardSeq:
      SetStep(step)
      time.sleep(delay)

def Backward(delay, steps):
  for i in range(steps):
    for step in reverseSeq:
      SetStep(step)
      time.sleep(delay)


def SetStep(step):
  GPIO.output(coilA1Pin, step[0] == '1')
  GPIO.output(coilA2Pin, step[1] == '1')
  GPIO.output(coilB1Pin, step[2] == '1')
  GPIO.output(coilB2Pin, step[3] == '1')

while True:
  SetStep('0000')
  delay = raw_input("Delay between steps (milliseconds)?")
  steps = raw_input("How many steps forward? ")
  Forward(int(delay) / 1000.0, int(steps))
  SetStep('0000')
  steps = raw_input("How many steps backwards? ")
  Backward(int(delay) / 1000.0, int(steps))
