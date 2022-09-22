numbers = [] # empty array
numbers = [34,234,556,231,1,22,89] # populated array

total = 0
#range(start point, end point, step)
for i in range(len(numbers)-1,-1,-1):
    total += numbers[i] # sum of values
    print(numbers[i])

avg = total / len(numbers) # average

