from tkinter import *
import sqlite3
from tkinter import messagebox
import Select_movie
import Data
com=sqlite3.connect('DataBase')
cur=com.cursor()

def open_login():
    root=Tk()

    Label(text="Welcome to Movie ticket booking system",fg="black",bg="yellow",font=("Times New Roman",30,"bold")).place(x=500,y=100)
    Label(text="Login",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=750,y=200)
    Label(text="UserName",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=650,y=250)
    Label(text="Password",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=650,y=300)
    Label(text="New user?",fg="black",bg="yellow",font=("Times New Roman",15,"bold")).place(x=700,y=400)

    Name=StringVar()
    password=StringVar()
    Entry(textvariable=Name).place(x=750,y=255)
    Entry(textvariable=password).place(x=750,y=305)
    def submit():
        user=Name.get()
        pas=password.get()
        cur.execute("select name,password from Users where name=? and Password=?",(user,pas))
        u=cur.fetchall()
        t=cur.fetchone()
        if t:
            user_id=t[0]
            Data.user_id=user_id
        if u:
            root.destroy()
            Select_movie.open_movie()
        else:
            messagebox.showinfo("Invalid username or Password")


    def  Register():
        root.destroy()
        c=Tk()
        Label(text="Register", fg="black", bg="yellow",
              font=("Times New Roman", 30, "bold")).place(x=500, y=100)
        Label(text="UserName", fg="black", bg="yellow", font=("Times New Roman", 15, "bold")).place(x=650, y=250)
        Label(text="Password", fg="black", bg="yellow", font=("Times New Roman", 15, "bold")).place(x=650, y=300)

        Name = StringVar()
        Password = StringVar()
        Entry(textvariable=Name).place(x=750, y=255)
        Entry(textvariable=Password).place(x=750, y=305)

        def create_account():
            username=Name.get()
            u_password=Password.get()
            cur.execute("""
            INSERT INTO Users
            (name,password)
            VALUES (?, ?)
            """, (
                username,
                u_password
            ))


            messagebox.showinfo("Success", "Account created successfully!")

            c.destroy()
            open_login()

        Button(text="Create New Account", command=create_account).place(x=700, y=400)

        c.geometry("1920x1080")
        c.title("Register Page")
        c.mainloop()

    Button(text="submit",command=submit).place(x=750,y=350)
    Button(text="Register",command=Register).place(x=800,y=400)

    root.geometry("1920x1080")
    root.title("Login Page")
    root.mainloop()
open_login()