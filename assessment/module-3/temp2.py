import tkinter as tk
from tkinter import messagebox
import sqlite3

# ================= DATABASE =================
conn = sqlite3.connect("repairmate.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS repairs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    phone TEXT,
    device_model TEXT,
    issue TEXT,
    status TEXT
)
""")
conn.commit()

# ================= LOGIN =================
def login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == "admin" and pwd == "admin123":
        login_window.destroy()
        admin_window()
    elif user == "tech" and pwd == "tech123":
        login_window.destroy()
        technician_window()
    else:
        messagebox.showerror("Error", "Invalid Login")

# ================= ADMIN =================
def save_data():
    try:
        if entry_name.get()=="" or entry_phone.get()=="" or entry_model.get()=="" or entry_issue.get()=="":
            raise Exception("All fields required")

        cursor.execute(
            "INSERT INTO repairs VALUES (NULL,?,?,?,?,?)",
            (entry_name.get(), entry_phone.get(),
             entry_model.get(), entry_issue.get(), "Pending")
        )
        conn.commit()
        messagebox.showinfo("Success", "Repair Added")

        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_model.delete(0, tk.END)
        entry_issue.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))

def admin_window():
    global entry_name, entry_phone, entry_model, entry_issue

    win = tk.Tk()
    win.title("Admin Panel")
    win.geometry("500x450")

    tk.Label(win, text="ADMIN DASHBOARD", font=("Arial",16,"bold")).pack(pady=10)

    tk.Label(win, text="Customer Name").pack()
    entry_name = tk.Entry(win, width=40)
    entry_name.pack()

    tk.Label(win, text="Phone Number").pack()
    entry_phone = tk.Entry(win, width=40)
    entry_phone.pack()

    tk.Label(win, text="Device Model").pack()
    entry_model = tk.Entry(win, width=40)
    entry_model.pack()

    tk.Label(win, text="Repair Issue").pack()
    entry_issue = tk.Entry(win, width=40)
    entry_issue.pack()

    tk.Button(win, text="Add Repair Record", width=20, command=save_data).pack(pady=20)
    win.mainloop()

# ================= TECHNICIAN =================
def show_help():
    messagebox.showinfo(
        "What is What - Technician Menu",
        "Repair Record List:\n"
        "- Displays all repair jobs\n"
        "- Select ONE record before updating\n\n"
        "Edit Section:\n"
        "- Update repair issue\n"
        "- Change status using checkboxes\n\n"
        "Update Repair:\n"
        "- Saves changes to database"
    )

def show_load_help():
    messagebox.showinfo(
        "Load Repair List - What is This?",
        "Load Repairs Button:\n"
        "- Fetches all repair records from database\n"
        "- Displays them in the list on left side\n\n"
        "List Details:\n"
        "ID      : Unique repair number\n"
        "Customer: Customer name\n"
        "Device  : Device model\n"
        "Issue   : Current repair problem\n"
        "Status  : Pending or Completed\n\n"
        "Next Step:\n"
        "- Select a repair from list to edit it"
    )

def load_repairs():
    listbox.delete(0, tk.END)
    rows = cursor.execute(
        "SELECT id, customer_name, device_model, issue, status FROM repairs"
    ).fetchall()

    for r in rows:
        listbox.insert(
            tk.END,
            f"ID:{r[0]} | {r[1]} | {r[2]} | {r[3]} | Status:{r[4]}"
        )

def update_repair():
    try:
        selected = listbox.get(listbox.curselection())
        repair_id = int(selected.split("|")[0].split(":")[1])

        if entry_new_issue.get() == "":
            raise Exception("Issue cannot be empty")

        if pending_var.get() == 1:
            status = "Pending"
        elif completed_var.get() == 1:
            status = "Completed"
        else:
            raise Exception("Select repair status")

        cursor.execute(
            "UPDATE repairs SET issue=?, status=? WHERE id=?",
            (entry_new_issue.get(), status, repair_id)
        )
        conn.commit()

        messagebox.showinfo("Success", "Repair Updated Successfully")
        load_repairs()

    except Exception as e:
        messagebox.showerror("Error", str(e))

def technician_window():
    global listbox, entry_new_issue, pending_var, completed_var

    win = tk.Tk()
    win.title("Technician Panel")
    win.geometry("950x600")

    # -------- MENU BAR --------
    menu_bar = tk.Menu(win)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="What is What", command=show_help)
    help_menu.add_command(label="Load Repair List - What is This?", command=show_load_help)

    menu_bar.add_cascade(label="Help", menu=help_menu)
    win.config(menu=menu_bar)

    # -------- TITLE --------
    tk.Label(win, text="TECHNICIAN DASHBOARD", font=("Arial",16,"bold")).pack(pady=5)
    tk.Label(
        win,
        text="Load repairs → Select repair → Update issue & status",
        font=("Arial",10)
    ).pack(pady=5)

    main_frame = tk.Frame(win)
    main_frame.pack(fill="both", expand=True, padx=10)

    # -------- LEFT PANEL --------
    left_frame = tk.Frame(main_frame, bd=2, relief="groove")
    left_frame.pack(side="left", fill="both", expand=True, padx=10)

    tk.Label(left_frame, text="REPAIR RECORD LIST", font=("Arial",12,"bold")).pack(pady=5)

    listbox = tk.Listbox(left_frame, width=95, height=18)
    listbox.pack(padx=10, pady=10)

    tk.Button(left_frame, text="Load Repairs", width=20, command=load_repairs).pack(pady=10)

    # -------- RIGHT PANEL --------
    right_frame = tk.Frame(main_frame, bd=2, relief="groove")
    right_frame.pack(side="right", fill="y", padx=10)

    tk.Label(right_frame, text="EDIT SELECTED REPAIR", font=("Arial",12,"bold")).pack(pady=10)

    tk.Label(right_frame, text="New Repair Issue").pack(anchor="w", padx=10)
    entry_new_issue = tk.Entry(right_frame, width=30)
    entry_new_issue.pack(padx=10, pady=5)

    tk.Label(right_frame, text="Repair Status").pack(anchor="w", padx=10)

    pending_var = tk.IntVar()
    completed_var = tk.IntVar()

    tk.Checkbutton(
        right_frame, text="Pending",
        variable=pending_var,
        command=lambda: completed_var.set(0)
    ).pack(anchor="w", padx=20)

    tk.Checkbutton(
        right_frame, text="Completed",
        variable=completed_var,
        command=lambda: pending_var.set(0)
    ).pack(anchor="w", padx=20)

    tk.Button(
        right_frame,
        text="Update Repair",
        width=20,
        command=update_repair
    ).pack(pady=20)

    win.mainloop()

# ================= LOGIN WINDOW =================
login_window = tk.Tk()
login_window.title("RepairMate Login")
login_window.geometry("400x300")

tk.Label(login_window, text="REPAIRMATE LOGIN", font=("Arial",16,"bold")).pack(pady=20)

tk.Label(login_window, text="Username").pack()
entry_user = tk.Entry(login_window, width=30)
entry_user.pack()

tk.Label(login_window, text="Password").pack()
entry_pass = tk.Entry(login_window, show="*", width=30)
entry_pass.pack()

tk.Button(login_window, text="Login", width=20, command=login).pack(pady=20)
login_window.mainloop()
