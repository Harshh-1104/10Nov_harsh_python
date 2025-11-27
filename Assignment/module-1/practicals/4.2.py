'''• Practical Example 6: Write a Python program to check if a number is prime using if_else.'''


num = int(input("enter a number : "))

for i in range(2, num):
    if num % i == 0:
        print(num, "is not a prime number")
        break
        
else:
    print(num, "is a prime number")
      
