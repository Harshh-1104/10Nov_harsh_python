'''12) Write a Python program to demonstrate the use of local and global variables in a class. '''


class Student:
    #global variable : shared by all objects
    school_name = "Tops Tech"

    def info(self, name, age):
        #local variables : unique to each object
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name} ")
        print(f"age = {self.age} ")
        print(f"school = {Student.school_name}")
        print("===========================")



s1 = Student()
s1.info("harsh", 22)

s2 = Student()
s2.info("ved", 21)


print("      student 1 data ")
s1.display()

print("      student 2 data  ")
s2.display()




