'''21) Write a Python program to create a database and a table using SQLite3.'''

import sqlite3

try:
    db=sqlite3.connect("21py.db")
    print("Database connection established successfully.")
except Exception as e:
   print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement, name varchar(20), city varchar(20))"
try:
    db.execute(tbl_create)
    print("Table created successfully")
except Exception as e:
    print(e)