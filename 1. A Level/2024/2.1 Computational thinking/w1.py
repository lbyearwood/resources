sweets = int(input("Enter sweets"))
bags = int(input("Enter bags"))

if sweets > bags:
    if sweets % 2 == 0 and bags % 2 == 0:
        print("It is possible")
    elif sweets % 2 != 0 and bags % 2 != 0:
        print("It is possible")
    else:
        print("It is NOT possible")
else:
    print("It is NOT possible")
