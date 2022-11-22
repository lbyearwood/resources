# for i in range(1,11):
#     print(i)

def printUpToTen(i):
    if i > 10:
        exit()
    print(i)
    i+=1
    printUpToTen(i) # recursive call

printUpToTen(1)

