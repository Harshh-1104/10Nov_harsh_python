'''Write Python programs to demonstrate method overloading and method overriding. '''

#Method overloading
print("========= Method overloading ========")

class student:
    def info(self,id):
        print("id = ",id)      
    def info(self,name):
        print("Name = ",name)
    def info(self,height):
        print("Height = ",height)

st=student()
st.info(11)
st.info("harsh")

#Method overriding
print("\n========= Method overriding ========")

class parent:
    def show(self):
        print("parent class")
        
class child(parent):
    def show(self):
        print("child class")
        
ch=child()
ch.show()
pa=parent()
pa.show()




