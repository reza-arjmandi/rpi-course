import RPi.GPIO as GPIO
import time

enable_pin=18
in_pin1=23
in_pin2=24

GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(in_pin1,GPIO.OUT)
GPIO.setup(in_pin2,GPIO.OUT)

pwm=GPIO.PWM(enable_pin,500)
pwm.start(0)

def clockwise():
    GPIO.output(in_pin1,True)
    GPIO.output(in_pin2,False)

def counter_clockwise():
    GPIO.output(in_pin1,False)
    GPIO.output(in_pin2,True)

while True:
    cmd=input("command f/r 0..9 e.g. f5: ")
    direction=cmd[0]

    if (direction=="f"):
        clockwise()
    else:
        counter_clockwise()

    speed=int(cmd[1]) *10
    pwm.ChangeDutyCycle(speed)
        
