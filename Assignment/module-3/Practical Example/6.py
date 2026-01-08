'''6) Write a Python program to check the current position of the file cursor using tell(). '''


#read()=reads the file from the beginning to end
#read(n)=reads n characters from the file
#tell()=returns the current position of file cursor if you put read() it will return
# the position after reading that much characters
#tell(n) returns an integer value of the current position of file cursor read(n) characters
#if you put read(3) first then read(5) then tell() will return 8 as the current position of file cursor


file_name = input("Enter the file name to read = ")
file = open(file_name, 'r')

info = file.read(3)
print("info in file = ")
print(info)
position = file.tell()
print("current position of file cursor = ", position)
file.close()

