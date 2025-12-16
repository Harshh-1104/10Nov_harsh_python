''' 20) Write a Python program to create a parameterized function that takes two arguments and prints their sum.'''

def sum(a,b):
    return a + b

a=int(input("enter value of 'a' = "))
b=int(input("enter value of 'b' = ")) 

print(f"sum of a and b is = {sum(a,b)}")