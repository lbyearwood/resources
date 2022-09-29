numbers = [45, 101, 87, 3, 60, 0, 34, -6,90] # list / array of values (numbers)
counter = 0 # start at zero because the index of the list / array starts at zero

numbers[4] = 78
# for ITEM in LIST

for i in range(0,len(numbers)): #-1
    if numbers[i] < 0:
        # change the value to 1000
        numbers[i] = 1000
    # end if

# End for
print(numbers)