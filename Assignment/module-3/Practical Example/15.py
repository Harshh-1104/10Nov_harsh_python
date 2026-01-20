'''15) Write a Python program to show multiple inheritance.'''

class parent1:
    def parent1(self):
        return "This is the 1st parent method"

class parent2:
    def parent2(self):
        return "This is the 2nd parent method"

class child(parent1, parent2):
    def child(self):
        return "This is the child method"
    
multi = child()
print(multi.parent1())
print(multi.parent2())
print(multi.child())

