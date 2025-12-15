'''Write a Python program to sort a list using both sort() and sorted().'''


'''Using sort()  -> sorts the same list (in-place), original 
Using sorted() -> returns a NEW sorted list, original can be reused
default: ascending order'''


list1 = [50,20,90,10,50,60]
print("original list1 = ", list1)

list1.sort()  
print("after sort() = ", list1)

list2 = [50,20,90,10,50,60]
sorted = sorted(list2)  
   
print("original list (list2) = ", list2)
print("sorted list (using sorted()) = ", sorted)
