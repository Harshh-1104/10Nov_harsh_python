'''• Write a Python program that uses reduce() to find the product of a list of numbers. '''

'''from functools import reduce
reduce(function, iterable[, initializer])'''

'''reduce(lambda x,y: x+y, [1, 2, 3, 4])
(1+2) = 3
(3+3) = 6  
(6+4) = 10  ← Final result'''




from functools import reduce

def multi(x, y):
    return x * y

numbers=[1,2,3,4,5]

product = reduce(multi, numbers)

print(product)