'''Write a Python program to merge two lists into one dictionary using a loop.'''

my_info={"name":"harsh" , "age":22 , "city":"rajkot", "height":6.2 , "course":"python" , "adult":True}

key=["name","age","city","height","course","adult"]
value=["harsh",22,"rajkot",6.2,"python",True]
dictionary={}

for i in range(len(key)):
    dictionary[key[i]]= value[i]
    
print(f"dictionary = {dictionary}")
