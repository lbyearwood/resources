
binary_list =  []
decimalNumber = 210

while decimalNumber != 0:
    binary_list.append(decimalNumber % 2)
    decimalNumber //= 2


#print(binary_list[::-1])
#

for i  in range(len(binary_list)-1,0,-1):
    print(binary_list[i], end="")