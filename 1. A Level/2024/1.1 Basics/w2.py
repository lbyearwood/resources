# get data from the end-user
mileage1 = int(input("enter the initial mileage"))
mileage2 = int(input("enter the current mileage"))
litresToFillTank = int(input("enter the amount of litres need to fill the tank"))

# calculate miles per gallon
totalMileage = mileage2 - mileage1
gallons = litresToFillTank/4.546
gallons = litresToFillTank * 0.22
milesPerGallon = totalMileage/gallons

# output mile per gallon
print(f"mile per gallon = {round(milesPerGallon,2)}")