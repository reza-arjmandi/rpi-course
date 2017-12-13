import time
import dweepy
import RPi.GPIO as GPIO

KEY = 'rpi_course_iot_projects'

led = [18, 23, 24]
led_states = [0, 0, 0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def UpdateLeds():
    for i in range(len(led_states)):
        GPIO.output(led[i], led_states[i])

while True:
    try:
        for dweet in dweepy.listen_for_dweets_from(KEY):
            if(dweet['content']['led0'] == 1):
                led_states[0] = not led_states[0]
            elif(dweet['content']['led1'] == 1):
                led_states[1] = not led_states[1]
            elif(dweet['content']['led2'] == 1):
                led_states[2] = not led_states[2]
            UpdateLeds()
    except Exception as e:
        pass
