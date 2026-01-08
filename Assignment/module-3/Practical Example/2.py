''' 2) Write a Python program to read a string, an integer, and a float from 
the keyboard and display them. '''

list=[]
string=input("Enter a string = ")
integer=int(input("Enter an integer = "))
floating=float(input("Enter a float = "))

list.append(string)
list.append(integer)
list.append(floating)

print("The entered values are = ")
for i in list:
    print(i)    
    
