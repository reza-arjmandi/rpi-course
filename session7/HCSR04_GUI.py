######################################################################
#       HCSR04_GUI.py
#
# This program read HCSR04 sensor data and print on a label in GUI
######################################################################

from Tkinter import *
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
    WaitForEcho(True, 10000)
    start = time.time()
    WaitForEcho(False, 10000)
    finish = time.time()
    pulseLen = finish - start
    distCm = pulseLen / 0.000058
    distInch = distCm / 2.5
    return (distCm, distInch)

class App:
	
    def __init__(self, master):
        self.master = master
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Distance (cm)', font=("Helvetica", 32))
        label.grid(row=0)
        self.readingLabel = Label(frame, text='00.00', font=("Helvetica", 110))
        self.readingLabel.grid(row=1)
        self.UpdateReading()

    def UpdateReading(self):
        cm, inch = GetDistance()
        readingStr = "{:.2f}".format(cm)
        self.readingLabel.configure(text=readingStr)
        self.master.after(500, self.UpdateReading)


root = Tk()
root.wm_title('Range Finder')
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()

