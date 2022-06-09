import random

a = int(input("Enter a number"))
b = int(input("Enter a number"))

if b > a:
    for i in range(a,b+1):
        print(random.randint(1,1000))
else:
    for i in range(b, a, -1):
        print(random.randint(1,1000))