'''20) Write a Python program to show method overriding.'''

print("\n========= Method overriding ========")

class parent:
    def show(self):
        print("parent class")
        
class child():
    def show(self):
        print("child class")
        
ch=child()
ch.show()

pa=parent()
pa.show()