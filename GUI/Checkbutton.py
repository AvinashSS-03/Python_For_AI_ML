#Checkbutton is like a checkbox (☑️).
from tabnanny import check
#Use it when the user can choose zero, one, or many options.

from tkinter import *

root=Tk()
var1=BooleanVar()
Checkbutton(root,text="py",variable=var1).place(x=55,y=99)
var2=BooleanVar()
Checkbutton(root,text="Java",variable=var2).place(x=55,y=199)
root.mainloop()
