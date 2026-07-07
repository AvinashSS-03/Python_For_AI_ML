import sqlite3
com=sqlite3.connect("Movie")
cur=com.cursor()
cur.execute("""
    CREATE TABLE If not exists Movies(movie TEXT,theater TEXT,timing TEXT)
    """
)
cur.execute("Delete from Movies")
cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Bahubali", "INOX Navalur", "09:00 AM")
)

cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Bahubali", "PVR Navalur", "02:00 PM")
)
cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Bahubali", "INOX Navalur", "02:00 PM")
)

cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Kgf", "PVR Navalur", "02:00 PM")
)

cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Kgf", "IMAX Sholinganallur", "08:00 PM")
)



cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Avenger", "IMAX Sholinganallur", "10:00 PM")
)

cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Kgf", "IMAX Sholinganallur", "10:00 PM")
)

cur.execute(
    "INSERT INTO Movies(movie, theater, timing) VALUES (?, ?, ?)",
    ("Bahubali", "IMAX Sholinganallur", "10:00 PM")
)

com.commit()

cur.execute("select * from Movies")
for i in cur:
    print(i)
