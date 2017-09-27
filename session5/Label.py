######################################################################
#       Label.py
#
# This snippet code create 3 label in a window
######################################################################

from tkinter import *

root = Tk()
root.title('label')

w = Label(root, text = "I am a first", bg = 'red', fg = 'white', padx = 50, font = ("Helvetica", 16))
w.pack()

var=StringVar()
x = Label(root, textvariable = var, bg = 'green', fg = 'black', padx = 50, font = ("Arial", 16))
x.pack()
var.set("I am a first")

z=Label(root, text = 'I am a first', bg = 'blue', fg = 'white', padx = 50, font = ("Helvetica", 16))
z.pack()

root.mainloop()