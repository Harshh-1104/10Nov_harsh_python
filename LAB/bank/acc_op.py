import random 
def acc_op():
    name=input("Enter holder's name = ")
    n=name
    bank_type=input("Enter account type name = ")
    b=bank_type
    acc_num = random.randint(100000000,999999999)
    return n,b,acc_num
   
def deposit():    
    Total_balance=int(input("enter an amount to deposit = "))
    return Total_balance
    
def withdraw():
    Total_balance=deposit()
    w=int(input("enter how much u want to withdraw = "))
    if Total_balance > w:
        Total_balance=Total_balance-w
        return Total_balance
    else:
        print("enter valid amount")
       
    
def statement():
    n,b,acc_num=acc_op()
    Total_balance=withdraw()
    print(f"acc holder's name ={n}")
    print(f"acc type = {b}")
    print(f"acc number = {acc_num}")
    print(f"Total balance = {Total_balance}")

    
   
print(acc_op)
print(deposit)
print(withdraw)
print(statement)
   
    