''' 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.'''

my_info={"name":"harsh" , "age":22 , "city":"rajkot", "height":6.2 , "course":"python" , "adult":True}

print(f"dictionary = {my_info}")

key=list(my_info.keys())
print(f"keys of given dictionary = {key}")

value=list(my_info.values())
print(f"values of given dictionary = {value}")