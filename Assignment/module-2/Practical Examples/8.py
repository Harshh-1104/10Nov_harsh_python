''' 8) Write a Python program to create a tuple with multiple data types'''

list=[]
taplu=()

n=int(input("how many values u want to store in tuple ? = "))

for i in range(n):
    values=input(f"enter value  {i+1} = ")
    list.append(values)
    
taplu=tuple(list)
print(f"tuple = {taplu}")
    