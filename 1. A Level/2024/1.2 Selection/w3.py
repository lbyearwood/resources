orderValue = float(input("Enter the total order price>>"))
deliveryOption = input("Enter 1. Next delivery, 2. Standard Delivery>>")
total = 0 # this will store the total postage code
postageCost = 5 # set the default cost to 5
if deliveryOption == "2":
    if orderValue >= 15:
        postageCost = 0
    else:
        postageCost = 3.50
total = total + orderValue + postageCost

print(f"The total cost is {total}")
