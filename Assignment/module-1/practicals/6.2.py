'''• Write a Python program that uses a custom iterator to iterate over a list of integers.'''

def myint(nums):
    i = 0
    while i < len(nums):
        yield nums[i]
        i += 1     #increment 

num = [1, 2, 3, 4, 5]
for x in myint(num):
    print(x)
