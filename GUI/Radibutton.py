#A Radiobutton lets the user choose only one option from a group.


from tkinter import *
root=Tk()
v=IntVar()
Radiobutton(root,text="male",variable=v,value=1).place(x=55,y=99)
Radiobutton(root,text="Female",variable=v,value=2).place(x=55,y=199)
root.mainloop()