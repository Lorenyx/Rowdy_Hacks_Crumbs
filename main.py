from time import process_time_ns
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
import modules

from click import command
from modules.debian_hash import get_hash

from modules.sys_identify import get_os

def retrieve_input():
    print(hash_var.get())
    print(path_var.get())
    ttk.Label(frm,font=("Comic Sans", 20),text=hash_var.get(),foreground=('RED')).grid(column=1,row=2) 





tk = tkinter
root = Tk()
root.title("Hash comparator")
hash_var = tk.StringVar()
path_var = tk.StringVar()


frm = ttk.Frame(root,padding=10)
frm.grid()



ttk.Label(frm, text="Enter Hash:\t").grid(column=0, row=0) 
hash_text = Entry(frm,textvariable=hash_var)
hash_text.grid(column=1,row=0)
ttk.Label(frm, text="Enter Path:\t").grid(column=0, row=1) 
path_text  = Entry(frm,textvariable=path_var)
path_text.grid(column=1,row=1)

ttk.Label(frm,text="Executable Status:\t").grid(column=0,row=2)



ttk.Button(frm, text="Check", command=retrieve_input).grid(column=2, row=2)
dist = get_os()
if (dist == "debian"):
    get_hash()
root.mainloop()

