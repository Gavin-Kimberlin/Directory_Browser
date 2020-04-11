from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
 
 
 
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Directory Browser")
        self.minsize(500, 75)
        self.button()
        self.directory = tk.Entry(self.master,text='',width=50)
        self.directory.grid(row=0,column=1,rowspan=1,columnspan=3,padx=15,pady=22)
 
 
 
    def button(self):
        self.button = ttk.Button(self.master, text = "Browse A Directory",command = self.fileDialog)
        self.button.grid(column=0,row=0,padx=15,pady=20)
 
 
    def fileDialog(self):
 
        self.directoryname = filedialog.askdirectory(initialdir =  "/", title = "Select A Directory")
        self.label = ttk.Label(self.master, text = "")
        self.directory.insert(0,self.directoryname)
        

 
root = Root()
root.mainloop()
