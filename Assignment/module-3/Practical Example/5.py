'''5) Write a Python program to read a file and print the data on the console. '''

file_name = input("Enter the file name to read = ")
file = open(file_name, 'r')
info = file.read()
print("info in file = ")
print(info)
file.close()
