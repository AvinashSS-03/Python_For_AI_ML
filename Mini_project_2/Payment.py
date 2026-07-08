from tkinter import *
import sqlite3
com=sqlite3.connect("DataBase")
cur=com.cursor()
import Data

def payment_now():
    root=Tk()
    Label(text="Billing system", fg="black", bg="yellow",
          font=("Times New Roman", 30, "bold")).place(x=500, y=100)

    cur.execute("""
    INSERT INTO Database
    (user_id,selected_movie,
     selected_theater, selected_timing,
     selected_seat, total_rupees)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        Data.user_id,
        Data.movie,
        Data.theater,
        Data.timing,
        ",".join(Data.selected_seat),
        Data.Amount
    ))
    com.commit()




    root.geometry("1920x1080")
    root.mainloop()
#payment_now()