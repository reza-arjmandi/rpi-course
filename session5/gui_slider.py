from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 500)
pwm.start(0)

class App:
	
    def __init__(self, master):
        scale = Scale(master, from_=0, to=100, 
              orient=HORIZONTAL, command=self.update)
        scale.pack(expand=True, fill=BOTH, padx=20, pady=20)

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('PWM Power Control')
app = App(root)
root.geometry("500x100+0+0")
root.mainloop()

