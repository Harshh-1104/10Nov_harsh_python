'''• Write a Python program to create a list with elements of multiple data types (integers, 
strings, floats, etc.). '''

mylist=[111,'harsh',True,11.1,[1,2,3]]

print("data types of 'my list' = ")

   
for i in mylist:
    print(f"{i} -> {type(i)}")