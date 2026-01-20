'''11) Write a Python program to create a class and access the properties of the class using an object. '''

class Person:
    def info(self, name, age):
        print(f"Name = {name} \n Age = {age}")
        
p1 = Person()
p1.info("harsh", 22)


