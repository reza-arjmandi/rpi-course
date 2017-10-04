######################################################################
#       Menu.py
#
# This example code demonstrate the Menu class in 
# tkinter library 
######################################################################

from tkinter import *
root = Tk()

def display():
    v = StringVar()
    label = Label(textvariable = v)
    v.set("You selected an option")
    label.pack()

menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar)
filemenu.add_command(label="Open", command = display)
filemenu.add_command(label="Save", command = display)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = root.quit)
menubar.add_cascade(label="File", menu = filemenu)
# create more pulldown menus
editmenu = Menu(menubar)
editmenu.add_command(label="Cut", command = display)
editmenu.add_command(label="Copy", command = display)
editmenu.add_command(label="Paste", command = display)
menubar.add_cascade(label="Edit", menu = editmenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label = "About", command = display)
menubar.add_cascade(label = "Help", menu = helpmenu)
# display the menu
root.config(menu = menubar)
mainloop()
