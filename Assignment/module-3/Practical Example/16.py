'''16) Write a Python program to show hierarchical inheritance.'''

class surname:
    def last_name(self):
        return "chauhan"
    
class boy(surname):
    def fname_b(self):
        return "harsh"
    
class girl(surname):
    def fname_g(self):
        return "harshiii"
    
b = boy()
g = girl()

print(f"boy's full name is  {b.fname_b()} {b.last_name()}")
print(f"girl's full name is  {g.fname_g()} {g.last_name()}")




    


