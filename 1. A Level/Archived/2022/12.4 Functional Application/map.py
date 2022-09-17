l = [2,12,100,567,78,76,90]

print("convert Integers to floats")
         # map(functionName,List)
fd = list(map(float,l))
print(fd)

print("Add 5 to each number in the list")
fx = list(map(lambda x:x+5,[2,12,10]))
print(fx)

print("Determin the maximum between 3 and x")
fx = list(map(lambda x:x+5,[2,12,10]))
print(fx)

print(max(3,5))