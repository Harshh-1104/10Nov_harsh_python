''' Write a Python program to write multiple strings into a file. '''

file="4.2.txt"
write = open(file, 'w')
write.writelines(["Hellooooooo ", "\ni am harsh anddddd ", "\nhave a great day "])
write.close()