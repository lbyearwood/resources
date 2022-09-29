total = 0 # total will sum the amount fo rainfall for the year
list = [] # that store the rainfall for each month
for i in range(12):
    amount = float(input("Enter rainfall amount")) # capture rainfall for a month
    list.append(amount)# add to the list
    total += amount # add to total

total = round(total,1) # round total to 1 decimal place
average = total / 12 # calcualte the average

count = 0
for i in range(len(list)):
    if list[i] > average: # if the rainfall is above the average
        count +=1 # increment count by 1

print(f"There were {count} months above the average") # print message to the user
