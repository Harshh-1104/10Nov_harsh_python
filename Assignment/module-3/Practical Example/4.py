''' 4) Write a Python program to create a file and print the string into the 
file.'''

file_name = input("Enter the file name = ")
str = input("Enter the string to write into the file = ")

file = open(file_name, 'w')
file.write(str)
file.close()

