''' 7) Write a Python program to handle exceptions in a calculator.'''

num1 = float(input("Enter first number = "))
num2 = float(input("Enter second number = "))

try:
    calc = input("<== press ==> \n1) for addition \n2) for subtraction \n3) for multiplication \n4) for division \n")
    if calc == '1':
        print(f"result = {num1 + num2}")
    elif calc == '2':
        print(f"result = {num1 - num2}")
    elif calc == '3':
        print(f"result = {num1 * num2}")
    elif calc == '4':
        print(f"result = {num1 / num2}")
    else:
        print("Invalid operation")
        
except ZeroDivisionError:
    print("Error-> Division by zero is not allowed")
except ValueError:
    print("Error-> Please enter numeric values")

