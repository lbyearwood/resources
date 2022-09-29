mylist = [23,43,97,72,13,64,97,54,23]

index = 0
for i in range(len(mylist)):
    if mylist[i] == 97:
        index = i
        break

mylist.pop(index)
print("number removed")

print(mylist)
