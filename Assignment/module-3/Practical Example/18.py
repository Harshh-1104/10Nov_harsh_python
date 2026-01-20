'''18) Write a Python program to demonstrate the use of super() in inheritance. '''

#super() is used to call parent class methods from a child class without rewriting code
# single inheritance defines the parent-child relationship,
# while super() is used to access parent class members

class Surname:
    def last_name(self):
        return "Chauhan"
    
class Boy(Surname):
    def first_name(self, first):
        self.first_name = first
    
    def full_name(self):
        return f"{self.first_name} {super().last_name()}"
    
b = Boy()
b.first_name("Harsh")
print(f"Boy's full name is {b.full_name()}")

