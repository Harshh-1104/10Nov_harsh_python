'''Write a Python program that manipulates and prints strings using various string methods.'''

str='my name is Harsh Chauhan.'

print("capitalize : ",str.capitalize())
print("casefold : ",str.casefold())
print("upper case:", str.upper())
print("lower case:", str.lower())
print("title case:", str.title())
print("replace 'Chauhan' with 'Ch':", str.replace("Chauhan", "Ch"))
print("split by space : ", str.split( ))
print('swapcase : ',str.swapcase())
print('slice it after 2nd character : ',str[2:])
print(str.center(40, "*"))
print("harsh is {0} at {1}".format("bad","coding"))
print("Is alpha:", "Hello".isalpha())
print("Is digit:", "123".isdigit())