'''• Write a Python program to handle exceptions in a simple calculator (division by zero, invalid 
input). '''

try:
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    calc = input("press \n1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n")
    
    if calc == '1':
        print(f"Result = {num1 + num2}")
    elif calc == '2':
        print(f"Result = {num1 - num2}")
    elif calc == '3':
        print(f"Result = {num1 * num2}")
    elif calc == '4':
        print(f"Result = {num1 / num2}")
    else:
        print("Invalid operation!")
        

except ZeroDivisionError:
    print("Cannot divide by zero")

