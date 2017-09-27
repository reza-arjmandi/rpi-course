######################################################################
#       Event.py
#
# This snippet code create a label in a window and handle all
# mouse event and keyboard event.
######################################################################

from tkinter import *

root = Tk()
prompt = 'click any button, or press a key'
w = Label(root, text = prompt, width = len(prompt), font = ("Helvetica", 16))
w.pack(pady = 50)

def key(event):
    if event.char == event.keysym:
        msg = "Normal Key {}".format(event.char)
    elif len(event.char) == 1:
        msg = "punctuation key {} ({})".format(event.keysym, event.char)
    else:
        msg = "Special Key {}".format(event.keysym)
    w.config(text = msg)

w.bind_all('<Key>', key)

def do_mouse(eventname):
    def mouse_binding(event):
        msg = "Mouse event {}".format(eventname)
        w.config(text = msg)
    w.bind_all("<{}>".format(eventname), mouse_binding)

for i in range(1, 4):
    do_mouse('Button-{}'.format(i))
    do_mouse('ButtonRelease-{}'.format(i))
    do_mouse('Double-Button-{}'.format(i))

root.mainloop()