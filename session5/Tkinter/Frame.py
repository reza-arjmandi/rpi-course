######################################################################
#       Frame.py
#
# This snippet code demonstrate the Frame class application
# in tkinter library
######################################################################

from tkinter import *

tx = 'creating a frame'
root = Tk()
fr = Frame(root, borderwidth = 10)
fr.pack(side = LEFT, padx = 15, pady = 15)
L1 = Label(fr, text = 'I am in frame')
L1.pack(side = LEFT)
L2 = Label(root, text = 'I am in root')
L2.pack(side = RIGHT)
B1 = Button(fr, text = 'I am in frame')
B1.pack(side = RIGHT)
root.title(tx)
root.mainloop()
