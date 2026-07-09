from pickle import GLOBAL
from tkinter import *
import sqlite3
# select movie ,theater ,showtimes
from tkinter import messagebox
import Payment
import Data
import Movie_Ticket_booking_system






def open_movie():

    root=Tk()
    movie=[]
    selected_seat=[]
    Label(text="Welcome to Movie ticket booking system",fg="black",bg="yellow",font=("Times New Roman",30,"bold")).place(x=500,y=100)
    Label(text="Select Movie",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=650,y=200)
    Label(text="Select Theater",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=650,y=300)
    Label(text="Select ShowTimes",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=650,y=450)
    seat_string=""
    bahubali=BooleanVar()
    Checkbutton(root,text="BAHUBALI",variable=bahubali).place(x=800,y=200)
    kgf=BooleanVar()
    Checkbutton(root,text="KGF",variable=kgf).place(x=800,y=220)
    Avengers=BooleanVar()
    Checkbutton(root,text="AVENGERS",variable=Avengers).place(x=800,y=240)
    r=""
    def confirm():
        global r
        if bahubali.get():
            movie.append("BAHUBALI")
            r="bahubali"

        if kgf.get():
            movie.append("KGF")
            r="KGF"

        if Avengers.get():
            movie.append("AVENGERS")
            r="Avengers"
        if r!="":
            messagebox.showinfo("Succesfull","The movie selected are: "+ r)

        else:
            messagebox.showinfo("unsuccesfull","Click correct movie")
        Label(root,text="The Movie You Selected:  "+r).place(x=1050,y=260)
        Data.movie=r


    Button(text="Confirm",command=confirm).place(x=800,y=260)

    theater=StringVar()
    theater.set("")
    Radiobutton(root,text="INOX - Navalur -Chennai",variable=theater,value="INOX - Navalur -Chennai").place(x=800,y=320)
    Radiobutton(root,text="INOX - Siruseri -Chennai",variable=theater,value="INOX - Siruseri -Chennai").place(x=800,y=340)
    Radiobutton(root,text="PVR - Navalur -Chennai",variable=theater,value="PVR - Navalur -Chennai").place(x=800,y=360)
    Radiobutton(root,text="IMAX - Sholinganallur -Chennai",variable=theater,value="IMAX - Sholinganallur -Chennai").place(x=800,y=380)
    Radiobutton(root,text="AGS - Vivira Mall -Chennai",variable=theater,value="AGS - Vivira Mall -Chennai",).place(x=800,y=400)

    def confirm_theater():
        if theater.get()=="":
            messagebox.showinfo("Un-Succesfull","Select a Theater")
        else:
            movie.append(theater.get())
            messagebox.showinfo("Succesfull","you selected "+theater.get())

        Label(root,text="The Theater:  " + theater.get() ).place(x=1050,y=460)
        Data.theater=theater.get()


    Button(text="Confirm",command=confirm_theater).place(x=800,y=420)


    Showtiming=StringVar()
    Showtiming.set("")
    Radiobutton(root,text="09.00 AM",variable=Showtiming,value="09.00 AM").place(x=800,y=500)
    Radiobutton(root,text="11.00 AM",variable=Showtiming,value="11.00 AM").place(x=800,y=520)
    Radiobutton(root,text="2.00 PM",variable=Showtiming,value="2.00 PM").place(x=800,y=540)
    Radiobutton(root,text="4.00 PM",variable=Showtiming,value="4.00 PM").place(x=800,y=560)
    Radiobutton(root,text="06.00 PM",variable=Showtiming,value="06.00 PM",).place(x=800,y=580)
    Radiobutton(root,text="08.00 PM",variable=Showtiming,value="08.00 PM",).place(x=800,y=600)
    Radiobutton(root,text="10.00 PM",variable=Showtiming,value="10.00 PM",).place(x=800,y=620)

    def confirm_timing():
        movie.append(Showtiming.get())
        if  Showtiming.get()=="":
            messagebox.showinfo("Un-Succesfull","Select Correct Timing")
        else:
            messagebox.showinfo("Succesfull","you selected "+Showtiming.get())
            Label(root,text="The timing You Selected:  "+ Showtiming.get()).place(x=1050,y=660)
            Data.timing=Showtiming.get()


    Button(text="Confirm",command=confirm_timing).place(x=800,y=640)
    def movieticket():
        Label(root,text="Confirm the details: \n " + "\n".join(movie)).place(x=600,y=600)
    def book():
        root.destroy()
        c=Tk()
        Label(text="Billing",fg="black",bg="yellow",font=("Times New Roman",30,"bold")).place(x=500,y=100)
        Label(text="Select Tickets", fg="black", bg="yellow",
        font=("Times New Roman", 30, "bold")).place(x=500, y=100)

        def selecte_seat(button,seat):
            if seat in selected_seat:
                selected_seat.remove(seat)
                button.config(bg="SystemButtonFace")
            else:
                selected_seat.append(seat)
                button.config(bg="green")
        rows=["A","B","C","D","E","F","G","H","I","J"]
        x = 500
        y = 200
        for i,rows in enumerate(rows):
            x=500
            for col in range(1,9):
                seat=f"{rows}{col}"

                btn=Button(c,text=seat,width=4)
                btn.config(command=lambda b=btn,s=seat:selecte_seat(b,s))

                btn.place(x=x,y=y)
                x+=50
            y+=50
        def confirm_ticket():
            Label(c,text="The selected seats are "+"-".join(selected_seat)).place(x=950,y=500)
            Label(c,text="The Movie Details:"+"\n".join(movie)).place(x=950,y=550)
            Amount=len(selected_seat)*100
            Data.Amount=Amount
            Data.selected_seat= selected_seat



            def payment():
                c.destroy()
                Payment.payment_now()

            Button(text="Go for Payment", command=payment).place(x=950, y=650)
        Button(text="Confirm",command=confirm_ticket).place(x=900,y=700)
        Button(text="Confirm", command=confirm_ticket).place(x=900, y=700)


        c.geometry("1920x1080")
        c.title("")
        c.mainloop()

    Button(text="Book tickets",command=book).place(x=700,y=700)



    root.geometry("1920x1080")
    root.title("MovieBooking")
    root.mainloop()

open_movie()
