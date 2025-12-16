'''18) Write a Python program to count how many times each character appears in a string. '''

string = input("enter string = ")
repeat = {}

print(f"your given string = {string}")

for i in string:
    if i in repeat:
        repeat[i] += 1
    else:
        repeat[i] = 1

print("how many times each character appears in a string = ", repeat)
