######################################################################
#       Button.py
#
# This snippet code create a button in a window and handle mouse 
# click event
######################################################################

from tkinter import *

root = Tk()
v = StringVar()
w = Label(root, textvariable = v, fg = 'blue')
v.set('You didnt click button')

def clickTest(event):
    v.set('You clicked button')

w.pack()
b = Button(root, text = 'click me')
b.pack(pady = 30)
b.bind('<Button-1>', clickTest)
root.mainloop()