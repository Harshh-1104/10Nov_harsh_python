print("====== Welcome to Collection Type Demo ======")




while True:

    print("What do you want to check ?")

    choice=int(input("1) List\n2) Tuple\n3) Set\n4) Dictionary\n5) Exit the menu\nEnter your choice = "))

    if choice == 1:
        list_item=input("Enter how many elements you want in list = ")
        my_list=[]
        for i in range(int(list_item)):
            element=input("Enter element = ")
            my_list.append(element)
        print("Your List is = ",my_list)
        
        print("what to do you want to do with list ?")
        list_choice=int(input("1) Add Element\n2) Remove Element\nEnter your choice = "))
        if list_choice == 1:
            add_element=input("Enter element to add in list = ")
            my_list.append(add_element)
            print("Updated List is = ",my_list)
        elif list_choice == 2:
            remove_element=input("Enter element to remove from list = ")
            my_list.remove(remove_element)
            print("Updated List is = ",my_list)
        
    elif choice == 2:
        tuple_item=input("Enter how many elements you want in tuple = ")
        my_list_for_tuple=[]
        for i in range(int(tuple_item)):
            element=input("Enter element = ")
            my_list_for_tuple.append(element)
        my_tuple=tuple(my_list_for_tuple)
        
        print("Your Tuple is = ",my_tuple)
        print("what to do you want to do with tuple ?")
        choice_tuple=int(input("1) Count Element\n2) Find Index of Element\nEnter your choice = "))
        
        if choice_tuple == 1:
            print(f"Count of elements in tuple is = ",len(my_tuple))
        elif choice_tuple == 2:
            index_element=input("Enter element to find index in tuple = ")
            print(f"Index of {index_element} in tuple is = {my_tuple.index(index_element)}")    
            
    elif choice == 3:
        set_item=input("Enter how many elements you want in set = ")
        my_set=set()
        for i in range(int(set_item)):
            element=input("Enter element = ")
            my_set.add(element)
        print("Your Set is = ",my_set)
        
        print("what to do you want to do with set ?")
        set_choice=int(input("1) Add Element\n2) Remove Element\nEnter your choice = "))
        if set_choice == 1:
            add_element=input("Enter element to add in set = ")
            my_set.add(add_element)
            print("Updated Set is = ",my_set)
        elif set_choice == 2:
            remove_element=input("Enter element to remove from set = ")
            my_set.remove(remove_element)
            print("Updated Set is = ",my_set)
            
    elif choice == 4:
        dict_item=input("Enter how many key-value pairs you want in dictionary = ")
        my_dict={}
        for i in range(int(dict_item)):
            key=input("Enter key = ")
            value=input("Enter value = ")
            my_dict[key]=value
        print("Your Dictionary is = ",my_dict)
        print("what to do you want to do with dictionary ?")
        
        dict_choice=int(input("1) Add Key-Value Pair\n2) Remove Key-Value Pair\nEnter your choice = "))
        if dict_choice == 1:
            key=input("Enter key to add in dictionary = ")
            value=input("Enter value to add in dictionary = ")
            my_dict[key]=value
            print("Updated Dictionary is = ",my_dict)
        elif dict_choice == 2:
            key=input("Enter key to remove from dictionary = ")
            my_dict.pop(key)
            print("Updated Dictionary is = ",my_dict)
        
    elif choice == 5:
        print("=========== Goodbye =============")
        break
    
    