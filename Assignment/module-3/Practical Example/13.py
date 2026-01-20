'''13) Write a Python program to show single inheritance. '''

class parent:
    def parent(self):
        return "This is the parent method"

class child(parent):
    def child(self):
        return "This is the child method"
    


single = child()
print(single.parent())  
print(single.child())   
