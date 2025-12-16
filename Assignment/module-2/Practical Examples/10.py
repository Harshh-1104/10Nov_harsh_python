'''10) Write a Python program to access the value of the first index in a tuple.'''

list=[]
taplu=()

n=int(input("how many values u want to store in tuple ? = "))

for i in range(n):
    values=input(f"enter value  {i+1} = ")
    list.append(values)
    
taplu=tuple(list)
print(f"tuple = {taplu}")

print(f"first element of tuple = {taplu[0]}")