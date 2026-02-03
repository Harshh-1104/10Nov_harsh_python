import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

# ---------- DATABASE ----------
conn = sqlite3.connect("repairmate.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS repairs(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,phone TEXT,device TEXT,issue TEXT,status TEXT)")
conn.commit()

# ---------- BASE CLASS ----------
class User:
    def show_message(self, msg):
        messagebox.showinfo("Info", msg)


# ---------- ADMIN CLASS ----------
class Admin(User):

    def open_admin_panel(self):
        win = tk.Tk()
        win.title("Admin Panel")
        win.geometry("400x400")

        tk.Label(win, text="ADMIN PANEL", font=("Georgia",14,"bold")).pack(pady=10)
        #pady means vertical space (top & bottom spacing) ,pad = padding (space), y = vertical direction
        #pady = space in UP and DOWN direction
        #This adds empty space:
        # 10 pixels above
        # 10 pixels below the widget
        # What does pady=10 actually do?
           # Before widget
           # ↑ 10px space
           # [  Widget  ]
           # ↓ 10px space
           # After widget

        tk.Label(win, text="Customer Name").pack()
        self.cstmr = tk.Entry(win); self.cstmr.pack()   
        
        #Entry is a Tkinter widget used to take text input from the user
        #self.e1 Save that input box inside the object So other methods can use it

        tk.Label(win, text="Phone").pack()
        self.phn = tk.Entry(win); self.phn.pack()

        tk.Label(win, text="Device").pack()
        self.dvc = tk.Entry(win); self.dvc.pack()

        tk.Label(win, text="Issue").pack()
        self.isu = tk.Entry(win); self.isu.pack()

        tk.Button(win, text="Add Repair", command=self.add_repair).pack(pady=20)

        win.mainloop()

    def add_repair(self):
        if self.cstmr.get()=="" or self.phn.get()=="" or self.dvc.get()=="" or self.isu.get()=="":
            messagebox.showerror("Error", "All fields required")
            return

        cur.execute("INSERT INTO repairs VALUES (NULL,?,?,?,?,?)",(self.cstmr.get(), self.phn.get(), self.dvc.get(), self.isu.get(), "Pending"))
        conn.commit()

        self.show_message("Repair added successfully")


        #delete() removes text from an Entry box
        #After delete() → it becomes empty.
        #entry.delete(start, end)-syntax 
        #(start, end): The range of characters to delete.
        #0 means the beginning of the text, and tk.END represents the end of the text
        
        self.cstmr.delete(0, tk.END)
        self.phn.delete(0, tk.END)
        self.dvc.delete(0, tk.END)
        self.isu.delete(0, tk.END)


#======= Technician window =======

class Technician(User):

    def open_tech_panel(self):
        win = tk.Tk()
        win.title("Technician Panel")
        win.geometry("520x580")

        tk.Label(win, text="TECHNICIAN PANEL", font=("Georgia",14,"bold")).pack(pady=10)

        #Listbox is a Tkinter widget used to display a list of selectable items.
        self.listbox = tk.Listbox(win, width=65)
        self.listbox.pack(pady=5)

        tk.Button(win, text="Load Repairs", command=self.load_repairs).pack()

        #for 110-114 code line -->
        #This code creates two radio buttons (Pending/Completed) that share one variable, and 
        # a button that uses that variable to update the selected repair’s status. 
        #Creates a Tkinter StringVar object and stores it in self.status.
        # StringVar holds a string and is used as the shared value for a group of radio buttons.
        # value="Pending" sets the initial value, so “Pending” will be selected by default
        
        
        self.status = tk.StringVar(value="Pending")
        tk.Radiobutton(win, text="Pending", variable=self.status, value="Pending").pack()
        tk.Radiobutton(win, text="Completed", variable=self.status, value="Completed").pack()

        tk.Button(win, text="Update status", command=self.update_status).pack(pady=5)

        tk.Label(win, text="Service cost").pack()
        self.sc = tk.Entry(win); self.sc.pack()

        tk.Label(win, text="Parts cost").pack()
        self.pc = tk.Entry(win); self.pc.pack()

        tk.Label(win, text="Tax (%)").pack()
        self.tx = tk.Entry(win); self.tx.pack()

        tk.Button(win, text="Generate invoice", command=self.generate_invoice).pack(pady=10)

        self.lbl = tk.Label(win, text="Total  0.00 $", font=("Georgia",11,"bold"))
        self.lbl.pack()

        win.mainloop()

    def load_repairs(self):
        self.listbox.delete(0, tk.END) # clear old items
        rows = cur.execute("SELECT * FROM repairs").fetchall()
        for i in rows:
            self.listbox.insert(tk.END, f"ID = {i[0]} ,Customer Name = {i[1]} , Device = {i[3]} , status = {i[5]}")  #id - name - device - status

    def update_status(self):
        # curselection() = It is a built-in Listbox method Returns the currently selected item(s) in the listbox
        if not self.listbox.curselection():   
            messagebox.showerror("Error", "Select a repair")
            return
        #curselection() returns index, not text.That’s why we use .get() after it.
        selected = self.listbox.get(self.listbox.curselection())
        rid = selected.split(",")[0].split("=")[1].strip()  #split() = removes spaces from both sides

        cur.execute("UPDATE repairs SET status=? WHERE id=?",(self.status.get(), rid))
        conn.commit()

        self.show_message("Status updated")
        self.load_repairs()

    def generate_invoice(self):
        try:
            if not self.listbox.curselection():
                messagebox.showerror("Error", "Select a repair")
                return

            service = float(self.sc.get())
            parts = float(self.pc.get())
            tax = float(self.tx.get())

            subtotal = service + parts
            total = subtotal + subtotal * tax / 100

            selected = self.listbox.get(self.listbox.curselection())
            rid = selected.split(",")[0].split("=")[1].strip()
            
            data = cur.execute("SELECT * FROM repairs WHERE id=?", (rid,)).fetchone()

            #with is used to automatically handle file opening and closing in Python 
            # and f is just a variable name representing the file object
            
            with open("invoice.txt", "a") as f:
                f.write("\n" + "="*40 + "\n")
                f.write("REPAIRMATE INVOICE\n")
                f.write(f"Date : {datetime.datetime.now()}\n")
                f.write(f"Name : {data[1]}\n")
                f.write(f"Device : {data[3]}\n")
                f.write(f"Service : {service}\n")
                f.write(f"Parts : {parts}\n")
                f.write(f"Tax : {tax}%\n")
                f.write(f"Total : {total:.2f}\n")
                f.write("="*40 + "\n")

            self.lbl.config(text=f"Total ₹ {total:.2f}")
            self.show_message("Invoice saved to invoice.txt")

        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")


# ---------- LOGIN ----------
def check_login():
    u = entry_user.get()
    p = entry_pass.get()

    if u=="admin" and p=="admin123":
        login_win.destroy()
        Admin().open_admin_panel()
    elif u=="tech" and p=="tech123":
        login_win.destroy()
        Technician().open_tech_panel()
    else:
        messagebox.showerror("Error", "Invalid login")

login_win = tk.Tk()
login_win.title("RepairMate Login")
login_win.geometry("300x250")

tk.Label(login_win, text="LOGIN", font=("Georgia",14,"bold")).pack(pady=20)

tk.Label(login_win, text="Username").pack()
entry_user = tk.Entry(login_win); entry_user.pack()

tk.Label(login_win, text="Password").pack()
entry_pass = tk.Entry(login_win, show="*"); entry_pass.pack()

tk.Button(login_win, text="Login", command=check_login).pack(pady=20)

login_win.mainloop()
