'''• Create a mini-project where students combine conditional statements, loops, and functions 
to create a basic Python application, such as a simple calculator or a grade management 
system. 
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b



while True:
    print("\nenter '0' to exit")
    print("1) add")
    print("2) subtract") 
    print("3) multiply")
    print("4) divide")
    n1=int(input("enter first value = "))
    n2=int(input("enter second value = "))
    choice = int(input("choose (1/2/3/4): "))
   
    if choice == 0:
        print("calculating done")
        break  
    elif choice == 1:
        print(f"Result add: {add(n1, n2)}")
    elif choice ==2:
        print(f"Result sub: {sub(n1, n2)}")
    elif choice == 3:
        print(f"Result multi: {multi(n1, n2)}")
    elif choice == 4:
        print(f"Result div: {div(n1, n2)}")
    else:
        print("Wrong choice")
        
