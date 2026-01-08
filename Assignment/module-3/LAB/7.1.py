'''Write Python programs to demonstrate different types of inheritance (single, multiple, 
multilevel, etc.).'''

#Single
class parent:
    def parent(self):
        print("parent class of single inheritance")      
class child(parent):
    def child(self):
        print("child class of single inheritance")

print("========= Single Inheritance ========")
single = child()
single.parent()
single.child()



#multiple
class father:
    def father(self):
        print("father class of multiple inheritance")
class mother:
    def mother(self):
        print("mother class of multiple inheritance")
class son(father, mother):
    def son(self):
        print("son class of multiple inheritance")

print("\n========= Multiple Inheritance ========")
multiple = son()
multiple.father()
multiple.mother()
multiple.son()


#multilevel
class grandparent:
    def grandparent(self):
        print("grandparent class of multilevel inheritance")
class parent(grandparent):
    def parent(self):
        print("parent class of multilevel inheritance")
class child(parent):
    def child(self):
        print("child class of multilevel inheritance")

print("\n========= Multilevel Inheritance ========")
multilevel = child()
multilevel.grandparent()
multilevel.parent()
multilevel.child()
