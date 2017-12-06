######################################################################
#       Grid.py
#
# This snippet code demonstrate the Grid class application
# in tkinter library
######################################################################

from Tkinter import *

def show_entry_fields():
    v = StringVar()
    L1 = Label(master, textvariable = v)
    v.set('First Name: {}, Last Name: {}'.format(e1.get(), e2.get()))
    L1.grid(row = 2)

master = Tk()
master.title("Grid")
Label(master, text = "First Name").grid(row = 0)
Label(master,text="Last Name").grid(row = 1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row = 0, column = 1)
e2.grid(row=1, column = 1)
B1 = Button(master, text = 'Quit', command = master.quit)
B1.grid(row = 3, column = 0, sticky = W, pady = 4)
B2 = Button(master, text = "show", command = show_entry_fields)
B2.grid(row = 3, column = 1, sticky = W, pady = 4)
master.mainloop()