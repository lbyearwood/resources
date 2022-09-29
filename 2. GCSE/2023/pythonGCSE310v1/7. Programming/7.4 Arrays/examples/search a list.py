import random
            # list comprehension
mylist = [random.randint(1,100) for i in range(500)]
count = 0
for i in range(len(mylist)):
    if mylist[i] == 55:
        count +=1
        print("Number Found")
      