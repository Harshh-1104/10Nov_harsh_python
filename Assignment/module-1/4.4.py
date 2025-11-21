'''• Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
using a nested if. '''


age = int(input("enter your age : "))
weight = float(input("enter your weight : "))


if age >= 18:
    if weight >= 50:
        print("you are eligible")
    else:
        print("you are not eligible to donate blood bcz your weight is less than 50kg")
else:
    print("you are not eligible to donate blood bcz you are under 18 y/o")
