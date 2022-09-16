import random

a = int(input("enter a number"))
b = int(input("enter a number greater than the first number"))

if b > a:
    for counter in range(a,b):
        print(random.randint(1,1000))
else:
    print("Error B is less than A")