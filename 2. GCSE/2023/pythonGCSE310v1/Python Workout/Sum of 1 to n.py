# 1 prompt the user to input a number
# repeatedly increment a counter by 1
# sum up the counters in sum
# print the value of sum

n = int(input("enter a number"))
sum = 0
for counter in range(1,n):
    sum = sum + counter

print(sum)