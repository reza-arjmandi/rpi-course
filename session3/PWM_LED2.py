import RPi.GPIO as GPIO
import time

led_pin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

led_pwm=GPIO.PWM(led_pin,50)
led_pwm.start(100)

while(True):
    for i in range(0,100):
        led_pwm.ChangeDutyCycle(i)
        print("Intensity: ",i)
        time.sleep(0.1)
        
    for i in range(100,0,-1):
        led_pwm.ChangeDutyCycle(i)
        print("Intensity: ",i)
        time.sleep(0.1)
