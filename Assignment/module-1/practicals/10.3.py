'''• Write a Python program that filters out even numbers using the filter() function.'''

'''filter(function, iterable)
How it works:
Applies function to each element of iterable

Keeps elements where function returns True

Discards elements where function returns False

Returns a filter object (iterator) - convert to list() to see results
'''

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(n):
    return n % 2 == 0

even_num = list(filter(even, num))

print("OG list:", num)
print("even numbers:", even_num)