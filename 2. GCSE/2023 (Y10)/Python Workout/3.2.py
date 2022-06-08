import random

a = int(input("Enter a number"))
b = int(input("Enter a number"))

if b > a:
    for i in range(a,b+1):
        print(random.randint(1,1000))
else:
    print("number 2 must larger than number 1")