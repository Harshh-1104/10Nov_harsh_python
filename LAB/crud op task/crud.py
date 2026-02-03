import sqlite3

print(" ====== crud op using sqlite3 ======")
db = sqlite3.connect('school.db')
cr = db.cursor()

tbl_name = input("Enter Table Name(ex: std_11):- ")
tbl_create = f"CREATE TABLE {tbl_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, ph_number TEXT, city TEXT)"
try:
    cr.execute(tbl_create)
    print("Table created")
except Exception as e:
    print(e)
    
def add_data():
    std_name = input("Enter Student Name:- ")
    std_num = input("Enter Student's Father Phone Number:- ")
    std_city = input("Enter Student City:- ")
    insert_data = f"INSERT INTO {tbl_name} (name, ph_number, city) VALUES ('{std_name}', '{std_num}', '{std_city}')"
    try:
        cr.execute(insert_data)
        db.commit()
        print("Data Inserted")
    except Exception as e:
        print(e)
    
def update_data():
    select = int(input("What do you want to update?\n1) Student Name\n2) Phone Number (Father)\n3) City\n:- "))
    roll_num = int(input("Enter Student Roll number:- "))
    
    if select == 1:
        n_name = input("Enter Student New Name:- ")
        update_q = f"UPDATE {tbl_name} SET name = '{n_name}' WHERE id = {roll_num}"
    elif select == 2:
        n_number = input("Enter Student New Phone Number:- ")
        update_q = f"UPDATE {tbl_name} SET ph_number = '{n_number}' WHERE id = {roll_num}"
    elif select == 3:
        n_city = input("Enter Student New City:- ")
        update_q = f"UPDATE {tbl_name} SET city = '{n_city}' WHERE id = {roll_num}"
    else:
        print("Invalid choice")
        return
    
    try:
        cr.execute(update_q)
        db.commit()
        print("Data Updated")
    except Exception as e:
        print(e)
        
def view_data():
    select = int(input("View Data = \n1)All Students\n2)Specific Student\n= "))
    
    if select == 1:
        view_all = f"SELECT * FROM {tbl_name}"
        try:
            cr.execute(view_all)
            rows = cr.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
    elif select == 2:
        roll_num = int(input("Enter Student Roll number:- "))
        view_spe = f"SELECT * FROM {tbl_name} WHERE id = {roll_num}"
        try:
            cr.execute(view_spe)
            row = cr.fetchone()
            print(row)
        except Exception as e:
            print(e)
    else:
        print("Invalid choice")
   
def delete_data():
    roll_num = int(input("Enter Student Roll number to delete:- "))
    delete_q = f"DELETE FROM {tbl_name} WHERE id = {roll_num}"
    try:
        cr.execute(delete_q)
        db.commit()
        print("Data Deleted")
    except Exception as e:
        print(e) 
   
    
    
while True:
    choice=int(input("1)add data\n2)update data\n3)view data\n4)delete data\n5)exit\n:-"))
    
    if choice == 1:
        add_data()
        
    elif choice == 2:
        update_data()
    
    elif choice == 3:
        view_data()
        
    elif choice == 4:
        delete_data()
    
    elif choice == 5:
        print("goodbyeee")
        break