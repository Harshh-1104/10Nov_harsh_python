'''19) Write a Python program to show method overloading.'''

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