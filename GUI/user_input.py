from tkinter import *
"""
StringVar() → Strings
IntVar() → Integers
DoubleVar() → Floating-point (decimal) numbers
BooleanVar() → True/False
"""
root=Tk()
name=StringVar()
age=IntVar()
salary=DoubleVar()
retired=BooleanVar()

Label(text="Enter your name",fg="black",bg="yellow",font=("Times New Roman",14,"bold")).place(x=20,y=50)
Label(text="Enter your Age",fg="black",bg="yellow",font=("Times New Roman",14,"bold")).place(x=20,y=100)
Label(text="Enter your Salary",fg="black",bg="yellow",font=("Times New Roman",14,"bold")).place(x=20,y=150)
Label(text="Are you retired ? ",fg="black",bg="yellow",font=("Times New Roman",14,"bold")).place(x=20,y=200)

Entry(textvariable=name).place(x=220,y=50)
Entry(textvariable=age).place(x=220,y=100)
Entry(textvariable=salary).place(x=220,y=150)
Entry(textvariable=retired).place(x=220,y=200)
print(name.get())
root.mainloop()