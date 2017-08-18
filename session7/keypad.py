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

for row_pin in rows:
    GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for col_pin in cols:
    GPIO.setup(col_pin, GPIO.OUT)

def get_key():
    key = 0
    for col_num, col_pin in enumerate(cols):
        GPIO.output(col_pin, 1)
        for row_num, row_pin in enumerate(rows):
            if GPIO.input(row_pin):
                key = keys[row_num][col_num]
        GPIO.output(col_pin, 0)
    return key

while True:
    key = get_key()
    if key :
        print(key)
    time.sleep(0.3)
