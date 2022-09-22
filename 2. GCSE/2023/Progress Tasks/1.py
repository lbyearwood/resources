import random

# for loop version
for i in range(1,4):
    n = int(input("enter a number"))
    if n >=100:
        n = float(n)
        randNum = random.randint(1,100)
        print("the random number is", randNum)
    else:
        n = bool(n)
        randNum = random.randint(101, 1000)
        print("the random number is",randNum)


# while loop version
i = 1
while i <=3:
    n = int(input("enter a number"))
    if n >=100:
        n = float(n)
        randNum = random.randint(1,100)
        print("the random number is", randNum)
    else:
        n = bool(n)
        randNum = random.randint(101, 1000)
        print("the random number is",randNum)
    i+=1

