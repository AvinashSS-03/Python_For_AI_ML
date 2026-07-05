from tkinter import *
root=Tk()
Label(text="Name",fg="black",bg="pink",font=("Times New Roman", 14,"bold")).place(x=96,y=77)
root.geometry("400x300") #create runtime windowsize
root.title("GUI prctice") #title
root.minsize(250,250) #minmum page size
root.maxsize(900,900) # maximum page size
root.mainloop()

