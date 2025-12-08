menu={"pizza":200,"burger":150,"hotdog":250,"chhas":20}


p=0
b=0
h=0
t=0
item_num={}

print("this is ur menu and select wht u want to eat :)")

num_list = list(menu.keys())  
for i in range(len(num_list)):  
    num = 1+i                   
    item = num_list[i]
    item_num[num] = item
    print(f"{num}) {item.title()} = {menu[item]}")
    
    

'''print("what do u want to order ?")

order={}

while True:
    choose=input("\nenter food item name and when you are done ordering, enter 'order' ")'''
    

order={}

while True:
    choose=input("\nEnter number of food item and enter='0' to confirm order : ")
    
    choose=int(choose)
    if choose==0:
        break
    if choose in num_list:
        item=num_list[choose]
        n=int(input(f"how many {item.tittle()}?"))
        if item in order:
            order[item] = n + order[item] 
        else:
            order[item] = n
    
    