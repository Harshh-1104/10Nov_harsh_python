'''9) Write a Python program to handle file exceptions and use the finally block for closing the file.'''

#In Python exception handling, finally defines a block of code that will always run after the try 
# (and any except) finishes, whether an error happened or not.
# if try block of code runs then try block of finally block will run and 
# if except block of code runs then except block of finally block will run.


try:
    file_name = input("enter the file name to read = ")
    file = open(file_name, 'r')
    info = file.read()
    print("file info = ")
    print(info)
except FileNotFoundError:
    print("Error-> The file was not found")
finally:
    try:
        file.close()
        print("File closed successfully")
    except NameError:
        print("File was never opened, so nothing to close")
    