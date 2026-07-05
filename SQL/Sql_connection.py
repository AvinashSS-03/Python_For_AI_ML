#Without manual sql DB connection
import sqlite3
com=sqlite3.connect('practice') #it will create a sql database as practice
cur=com.cursor() # It is used to create a cursor
#cursor is used to write query in function
cur.execute("create  table practice(Name varchar(100),Id int )")
#execute() is used to send an SQL statement to the database so that SQLite can perform the requested operation
cur.execute("insert into practice values('Avinash',1),('Rashmika',2)")
cur.execute("select * from practice")
for i in cur:
    print(i)