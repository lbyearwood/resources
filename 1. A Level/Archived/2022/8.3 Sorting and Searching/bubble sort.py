list=[4,2,100,67,90,39,100,76]
swapMade = True

while swapMade:
    for i in range(len(list)-1):
        swapMade = False
        if list[i] > list[i+1]:
            swap = list[i]
            list[i] = list[i+1]
            list[i+1] = swap
            swapMade = True
print(list)




