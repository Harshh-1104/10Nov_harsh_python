''' 23) Write a Python program to search for a word in a string using re.search()'''

import re

str=input("Enter the string = ")
print("Given string is = ",str)

word=input("Enter the word that u want to search = ")

match=re.search(word,str)  

if match:
    print("Word found in given string")
else:
    print("Word not found in given string")