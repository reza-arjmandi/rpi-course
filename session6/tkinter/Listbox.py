######################################################################
#       ListBox.py
#
# This example code demonstrate the listbox class in conjuction
# with scrollable in tkinter library 
######################################################################

import tkinter
from tkinter import *

root = Tk()
root.title('a scrollable listbox')
# create the listbox (height/width in char)
listbox = Listbox(root, width = 50, height = 6 , selectmode = BROWSE)
listbox.grid(row = 0, column = 0)
# create a vertical scrollbar to the right of the listbox
yscroll = Scrollbar(command = listbox.yview, orient = VERTICAL)
yscroll.grid(row = 0, column = 1, sticky='n' + 's')
listbox.configure(yscrollcommand = yscroll.set)
# now load the listbox with data
book_list = [
'C Programming', 'C# programming', 'Java Programming', 'Python Programming',
'Software engineering', 'Programming languages', 'Algorithms', 
'Data structure', 'Security ', 'Socket programming',
'Computer Networks', 'Computer Architecture']
for item in book_list:
    # insert each new item to the end of the listbox
    listbox.insert('end', item)
# optionally scroll to the bottom of the listbox
lines = len(book_list)
listbox.yview_scroll(lines, 'units')
root.mainloop()
