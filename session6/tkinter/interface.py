######################################################################
#       Interface.py
#
# This example code demonstrate a user interface that created by
# tkinter library 
######################################################################

import tkinter 

form = tkinter.Tk() 
 
getFld = tkinter.IntVar() 
form.wm_title('File Parser') 
 
stepOne = tkinter.LabelFrame(form, text=" 1. Enter File Details: ") 
stepOne.grid(row=0, columnspan=7, sticky='W', 
             padx=5, pady=5, ipadx=5, ipady=5) 
 
helpLf = tkinter.LabelFrame(form, text=" Quick Help ") 
helpLf.grid(row=0, column=9, columnspan=2, rowspan=8,  
              sticky='NS', padx=5, pady=5) 
helpLbl = tkinter.Label(helpLf, text="Help will come - ask for it.") 
helpLbl.grid(row=0) 
 
stepTwo = tkinter.LabelFrame(form, text=" 2. Enter Table Details: ") 
stepTwo.grid(row=2, columnspan=7, sticky='W',  
              padx=5, pady=5, ipadx=5, ipady=5) 
 
stepThree = tkinter.LabelFrame(form, text=" 3. Configure: ") 
stepThree.grid(row=3, columnspan=7, sticky='W',  
                 padx=5, pady=5, ipadx=5, ipady=5) 
 
inFileLbl = tkinter.Label(stepOne, text="Select the File:") 
inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2) 
 
inFileTxt = tkinter.Entry(stepOne) 
inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3) 
 
inFileBtn = tkinter.Button(stepOne, text="Browse ...") 
inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2) 
 
outFileLbl = tkinter.Label(stepOne, text="Save File to:") 
outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2) 
 
outFileTxt = tkinter.Entry(stepOne) 
outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2) 
 
outFileBtn = tkinter.Button(stepOne, text="Browse ...") 
outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2) 
 
inEncLbl = tkinter.Label(stepOne, text="Input File Encoding:") 
inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2) 
 
inEncTxt = tkinter.Entry(stepOne) 
inEncTxt.grid(row=2, column=1, sticky='E', pady=2) 
 
outEncLbl = tkinter.Label(stepOne, text="Output File Encoding:") 
outEncLbl.grid(row=2, column=5, padx=5, pady=2) 
 
outEncTxt = tkinter.Entry(stepOne) 
outEncTxt.grid(row=2, column=7, pady=2) 
 
outTblLbl = tkinter.Label(stepTwo, 
          text="Enter the name of the table to be used in the statements:") 
outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2) 
 
outTblTxt = tkinter.Entry(stepTwo) 
outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE') 
 
fldLbl = tkinter.Label(stepTwo, 
                           text="Enter the field (column) names of the table:") 
fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W') 
 
getFldChk = tkinter.Checkbutton(stepTwo,  
                           text="Get fields automatically from input file",
                           onvalue=1, offvalue=0) 
getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE') 
 
fldRowTxt = tkinter.Entry(stepTwo) 
fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE') 
 
transChk = tkinter.Checkbutton(stepThree,  
               text="Enable Transaction", onvalue=1, offvalue=0) 
transChk.grid(row=6, sticky='W', padx=5, pady=2) 
 
transRwLbl = tkinter.Label(stepThree,  
                 text=" => Specify number of rows per transaction:") 
transRwLbl.grid(row=6, column=2, columnspan=2,  
                    sticky='W', padx=5, pady=2) 
 
transRwTxt = tkinter.Entry(stepThree) 
transRwTxt.grid(row=6, column=4, sticky='WE') 
 
form.mainloop() 

 
