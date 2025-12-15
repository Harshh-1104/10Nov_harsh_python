'''Write a Python program to create a calculator using functions.'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b

print("(1)add")
print("(2)subtract")
print("(3)multiply")
print("(4)divide")

choice = input("enter choice from 1 to 4 = ")

num1 = float(input("enter first num = "))
num2 = float(input("enter second num = "))

if choice == "1":
    print("result = ", add(num1, num2))
elif choice == "2":
    print("result = ", subtract(num1, num2))
elif choice == "3":
    print("result = ", multi(num1, num2))
elif choice == "4":
    print("result = ", divide(num1, num2))
else:
    print("invalid choice")
