import random

class Bank_system:
    def info(self):
        print("============ Welcome to the Bank ==============")
        self.name = input("Enter account holder's name = ")
        self.acc_no = random.randint(100000, 999999)
        self.balance = 0
        
class Deposit_Withdraw(Bank_system):
    def depo(self):
        try:
            amount = int(input("Enter amount to be deposited must be 2000+ : "))
            if amount > 2000:
                self.balance += amount
                print(f"Deposit amount = {amount}")
                print(f"New balance = {self.balance}")
            else:
                raise Exception("Deposit amount must be 2000+")
        except Exception as e:
            print(e)
            exit()   

class Withdraw(Deposit_Withdraw):
    def withdraw(self):
        try:
            amount = int(input("Enter amount to be withdrawn = "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn = {amount}")
                print(f"New Balance = {self.balance}")
            else:
                raise Exception("Insufficient balance")
        except Exception as e:
            print(e)
            exit()  
      
class Statement(Withdraw):      
    def statement(self):
        print("===== Account Statement =====")
        print(f"Account holder name = {self.name}")
        print(f"Account number = {self.acc_no}")
        print(f"Current balance = {self.balance}")
        print("=============================")
        

acc_op = Statement()
acc_op.info()
acc_op.depo()
acc_op.withdraw()
acc_op.statement()
