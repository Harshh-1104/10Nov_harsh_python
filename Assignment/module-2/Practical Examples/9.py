''' 9) Write a Python program to concatenate two tuples into one. '''

list1=[]
list2=[]
t1=()
t2=()


n1=int(input("how many values u want to store in tuple 1 ? = "))

for i in range(n1):
    values1=input(f"enter value  {i+1} = ")
    list1.append(values1)
    
t1=tuple(list1)
print(f"tuple 1 = {t1}")


n2=int(input("how many values u want to store in tuple 2 ? = "))

for j in range(n2):
    values2=input(f"enter value  {j+1} = ")
    list2.append(values2)
    
t2=tuple(list2)
print(f"tuple 2 = {t2}")

t=t1+t2
print(f"concatenate of two tuple = {t}")
