import tkinter
from tkinter import messagebox,ttk

def calculate_sum():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    messagebox.showinfo("result = ", f"The sum is = {result}")

calc = tkinter.Tk()
calc.title("Sum calc")
calc.geometry("300x200")

label_num1 = ttk.Label(calc, text="Enter first number = ")
label_num2= ttk.Label(calc, text="Enter second number = ")
entry_num1 = ttk.Entry(calc)
entry_num2 = ttk.Entry(calc)

button_calculate = ttk.Button(calc, text="Calculate Sum", command=calculate_sum)

label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
button_calculate.pack()

calc.mainloop()
