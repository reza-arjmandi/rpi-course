from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

class app:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        self.checkvar=BooleanVar()
        check=Checkbutton(frame,text='LED',command=self.update,variable=self.checkvar,onvalue=True,offvalue=False)
        check.grid(row=1)

    def update(self):
        GPIO.output(18,self.checkvar.get())

root=Tk()
root.wm_title('on / off switch')
App=app(root)
root.geometry('200x50+0+0')
root.mainloop()

