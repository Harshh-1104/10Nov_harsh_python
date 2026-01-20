'''14) Write a Python program to show multilevel inheritance.'''

class grandparent:
    def grandparent(self):
        return "This is the grandparent method"
    
class parent(grandparent):
    def parent(self):
        return "This is the parent method"
    
class child(parent):
    def child(self):
        return "This is the child method"
    
multi = child()
print(multi.grandparent())
print(multi.parent())
print(multi.child())
