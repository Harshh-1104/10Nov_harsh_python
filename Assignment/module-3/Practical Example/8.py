''' 8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).'''

try:
    file_name = input("enter the file name to read = ")
    file=open(file_name, 'r')
    info = file.read()
    print("File info = ")
    print(info)
    
    num1 = float(input("Enter the number that you want to divide = "))
    num2 = float(input("Enter the number that you want to divide with = "))
   
    print(f"result = {num1 / num2}")
except FileNotFoundError:
    print("Error-> The file was not found.")
except ZeroDivisionError:
    print("Error-> Division by zero is not allowed.")
