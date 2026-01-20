'''22) Write a Python program to insert data into an SQLite3 database and fetch it. '''

import sqlite3

try:
    db=sqlite3.connect("22py.db")
    print("Database connection established successfully.")
except Exception as e:
   print(e)

#Table Create
tbl_create="create table studinfo(id integer primary key autoincrement, name varchar(20), city varchar(20))"
try:
    db.execute(tbl_create)
    print("Table created successfully.")
except Exception as e:
    print(e)
    

#Insert Data
insert_data="insert into studinfo(name,city)values('harsh','rajkot'),('ved','morbi'),('hima','junagadh'),('param','jamnagar')"

try:
    db.execute(insert_data)
    db.commit()
    print("Data inserted successfully")
except Exception as e:
    print(e)
    
#Fetch Data
select_data="select * from studinfo"
try:
    cr=db.cursor()
    cr.execute(select_data)
    data=cr.fetchall()
    for i in data:
        print(i)
except Exception as e:
    print(e)