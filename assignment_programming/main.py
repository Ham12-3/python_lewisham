from tkinter import *

from ttkbootstrap.constants import *
from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title("Assignment Programming")

# root.iconbitmap("assignment_programming/icon.ico") 

root.geometry("800x600")

def checker():
    if var1.get() == 1:
        my_label.config(text="You checked the box")

    else:
        my_label.config(text="You unchecked the box")



my_label = Label(text="Click the checkbutton below", font=("Helvetica", 18))

my_label.pack(pady=(40,10))

var1 = IntVar()

my_check = tb.Checkbutton(bootstyle="primary", command=checker,text="Check me out", variable=var1, onvalue=1, offvalue=0)  
my_check.pack(pady=10)



var2 = IntVar()


my_check2 = tb.Checkbutton(command=checker,bootstyle="danger, toolbutton", variable=var2, onvalue=1, offvalue=0, text="Check me out too")
my_check2.pack(pady=10)
root.mainloop()