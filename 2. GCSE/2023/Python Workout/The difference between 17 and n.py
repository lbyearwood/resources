# 1. input a number
# 2. Check if n is greater than 17
# 3. calculate the difference between the number and 17
# 4. if n > 17

n = int(input("Enter a number"))
difference = n - 17
if n > 17:
    print(abs(difference*2))
else:
    print(difference)