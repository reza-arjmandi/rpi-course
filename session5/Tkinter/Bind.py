######################################################################
#       Bind.py
#
# This snippet code demonstrate bind mechanism in tkinter
######################################################################

from tkinter import *

root = Tk()

def func1(event):
    print(event.x, event.y)
    root.wm_title("{}, {}".format(event.x, event.y))
    
root.bind('<Button-1>', func1)
root.mainloop()


    
