import RPi.GPIO as GPIO

led_pin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)

pwm_led=GPIO.PWM(led_pin,100)
pwm_led.start(100)

while(True):
    duty_s=input("Please Enter Brightness(0 to 100): ")
    duty=int(duty_s)
    pwm_led.ChangeDutyCycle(duty)
    
