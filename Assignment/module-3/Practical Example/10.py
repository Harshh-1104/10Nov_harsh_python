'''10) Write a Python program to print custom exceptions. '''



    
#       raise	                            except
#Used to create an error	     |   Used to handle an error
#Throws an exception	         |   Catches an exception
#Stops normal program flow	     |   Prevents program crash
#Used inside try or anywhere	 |   Used only with try


age=int(input("Enter your age: "))

try:
    if age < 18:
        raise Exception("age must be 18 or above")
except Exception as e:
    print(e)
    
    