'''Write a Python program to generate random numbers using the random module. '''

import random

x=random.randint(100,999)
print(f"random int from 100-999 = {x}")

y=random.random()
print(f"random int from 0.0-1.0 = {y}")

z=random.randrange(0, 10, 2)
print(f"random even number from 0-10 = {z}")