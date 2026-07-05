from tkinter import *
#buuton is used to create a button so whenever we click some function is to be done
#coomand -->call functions
#quit -> exit the code
root=Tk()
def greet():
    print("Welcome to python")
Button(text="Click",command=greet).place(x=65,y=63)
Button(text="Exit",command=quit).place(x=25,y=93)

root.mainloop()


# we can destroy to close the window permenately root.destroy()