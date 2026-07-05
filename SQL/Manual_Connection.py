#To install my sql connector package use
#pip  install mysql-connector-python

import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""

)