''' 24) Write a Python program to match a word in a string using re.match().'''

import re

str=input("Enter the string = ")
print("Given string is = ",str)

word=input("Enter the word that u want to match = ")
match=re.match(word,str)

if match:
    print("Word matched in given string")
else:
    print("Word not matched in given string")