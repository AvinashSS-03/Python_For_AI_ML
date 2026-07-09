from tkinter import *
import sqlite3
import  Movie_Ticket_booking_system
import Data

def payment_now():
    root=Tk()
    Label(text="Billing system", fg="black", bg="yellow",
          font=("Times New Roman", 30, "bold")).place(x=500, y=100)

    Movie_Ticket_booking_system.cur.execute("""
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
    Movie_Ticket_booking_system.com.commit()

    bill = f"""
     ========================================================
                     MOVIE TICKET BOOKING                    
     ========================================================
      Customer Name : {Data.username:<35}
     --------------------------------------------------------
      Movie         : {Data.movie:<35}
      Theater       : {Data.theater:<35}
      Show Time     : {Data.timing:<35}
      Seats         : {", ".join(Data.selected_seat):<35}
     --------------------------------------------------------
      Ticket Price  : ₹100                                   
      No. of Seats  : {len(Data.selected_seat):<35}
    --------------------------------------------------------
     Total Amount  : ₹{Data.Amount:<34}
     ========================================================
                   THANK YOU! VISIT AGAIN                    
     ========================================================
    """
    Label(
    root,
    text=bill,
    font=("Times New Roman", 12, "bold"),
    bg="white",
    fg="black"
    ).place(x=500, y=200)

    Movie_Ticket_booking_system.prints()


    root.geometry("1920x1080")
    root.mainloop()
