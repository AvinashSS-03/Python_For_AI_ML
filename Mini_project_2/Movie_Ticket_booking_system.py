"""
Project Title:

Movie Ticket Booking System

 Tech Stack :

Language: Python
GUI Library: Tkinter
Database: SQLite3

 GUI Pages:

Login / Register Page

Movie Selection Page

Seat & Time Selection Page

Booking Summary Page

Confirmation Message

 Work flow :

User opens app → Login/Register. (Labels, Entry, button and message box)

Selects movie → theatre → show time. (Labels, Drop down, button)

Chooses number of seats. ( Buttons)

System calculates total and shows summary. ( Labels)

On confirm, details stored in SQLite database.
"""
import sqlite3
import Data
com=sqlite3.connect('DataBase')
cur=com.cursor()
#cur.execute("Delete  from Users")
#cur.execute("Delete from Database")
#com.commit()

cur.execute("""
Create table If not exists Users( 
    user_id Integer Primary Key Autoincrement,
    name varchar(100),
    password varchar(100)
    )
    """)
com.commit()
cur.execute("""
Create table If not exists Database( 
    booking_id integer primary key Autoincrement,
    user_id Integer,
    selected_movie varchar(100),
    selected_theater varchar(100),
    selected_timing varchar(100),
    selected_seat varchar(100),
    total_rupees integer,
    Foreign Key(user_id) references Users(user_id)
    
    )
    """)
com.commit()
def savebooking():
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
def prints():
    print(Data.user_id)
    print(Data.movie)
    print(Data.theater)
    print(Data.timing)
    print(Data.selected_seat)
    print(Data.Amount)
    cur.execute("""
    SELECT
        Users.user_id,
        Users.name,
        Users.password,
        Database.selected_movie,
        Database.selected_theater,
        Database.selected_timing,
        Database.selected_seat,
        Database.total_rupees
    FROM Users
    INNER JOIN Database
    ON Users.user_id = Database.user_id
    """)
    com.commit()
cur.execute("SELECT * FROM Users")
print(cur.fetchall())

cur.execute("SELECT * FROM Database")
print(cur.fetchall())
cur.execute("""
   SELECT
       Users.user_id,
       Users.name,
       Users.password,
       Database.selected_movie,
       Database.selected_theater,
       Database.selected_timing,
       Database.selected_seat,
       Database.total_rupees
   FROM Users
   INNER JOIN Database
   ON Users.user_id = Database.user_id
   """)
rows = cur.fetchall()

print(rows)

