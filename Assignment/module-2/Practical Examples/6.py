''' 6) Write a Python program to insert elements into an empty list using a for loop and append(). '''

list = []

n=int(input("how many values u want to store ? = "))

for i in range(n):
    value=input(f"enter value  {i+1} = ")
    list.append(value)
    
print(list)
    