'''• Write a Python program to remove elements from a list using pop() and remove().'''

OG = [10, 20, 30, 40, 50, 60]
print("original list = ", OG)

remove_last = OG.pop()       
print("after pop() = ", OG)
print("remove element (last) = ", remove_last)

remove_in1 = OG.pop(1)    
print("after pop(1) = ", OG)
print("remove element at index 1 = ", remove_in1)


OG.remove(30)                 
print("after remove(30) = ", OG)
