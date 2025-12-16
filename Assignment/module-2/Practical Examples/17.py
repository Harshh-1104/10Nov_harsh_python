''' 17) Write a Python program to convert two lists into one dictionary using a for loop.'''

#my_info={"name":"harsh" , "age":22 , "city":"rajkot", "height":6.2 , "course":"python" , "adult":True}

key=["name","age","city","height","course","adult"]
value=["harsh",22,"rajkot",6.2,"python",True]

my_info={}

for i in range(len(key)):
    my_info[key[i]]=value[i]
    
print(f"two list into one dict = {my_info}")