'''• Write a Python program to create a class and access its properties using an object. '''

class MyClass:
    def info(self, name, age):
        self.name = name
        self.age = age
        
H = MyClass()
H.info("Harsh", 22)
print("Name = ", H.name)
print("Age = ", H.age)


