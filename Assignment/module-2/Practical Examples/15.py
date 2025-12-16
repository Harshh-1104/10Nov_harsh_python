''' 15) Write a Python program to update a value at a particular key in a dictionary.'''

my_info={"name":"harsh" , "age":22 , "city":"rajkot", "height":6.2 , "course":"python" , "adult":True}


my_info["age"] = 23
my_info["grade"] = "A"
print("after updating age=23 and adding grade = ", my_info)

edit = {"city": "Porbandar", "age": 92}
my_info.update(edit)
print("after update() with new values : ",my_info)