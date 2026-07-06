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

com=sqlite3.connect('DataBase')
cur=com.cursor()
cur.execute("Create table If not exists Database( name varchar(100),Password varchar(100))")
cur.execute("select * from DataBase")
for i in cur:
    print(i)
print("hello")