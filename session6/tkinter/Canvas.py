######################################################################
#       Canvas.py
#
# This example code demonstrate the canvas class
# for drawing shapes in tkinter library 
######################################################################

from tkinter import *

master = Tk()
w = Canvas(master, width = 200, height=100)
w.pack()
w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill = "red", dash = (4, 4))
w.create_rectangle(50, 25, 150, 75, fill = "blue")
w.create_oval(10, 20, 30, 40, fill = "red") ## circle
w.create_oval(170, 20, 200, 40, fill = "red") ## elipse
mainloop()
