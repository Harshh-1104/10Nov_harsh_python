'''• Write a Python program to demonstrate handling multiple exceptions.'''

#this is for handling error if you put character instead of number and #also handling division by zero error


try:
    num = int(input("enter number = "))
    print(f"if we divide 1000 by {num} = {1000 / num}")
except ValueError:
    print("please enter a number")
except ZeroDivisionError:
    print("cannot divide by zero")
