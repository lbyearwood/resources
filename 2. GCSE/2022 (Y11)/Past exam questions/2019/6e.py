riders = 0

while riders <=8:
    height = int(input("Please input your height in cm"))
    if height >= 140:
        riders = riders + 1
        print("Please enter the ride")
    elif height >=120:
        adultRiding = input("Are you riding with an adult? Y/N").lower()
        if adultRiding == "y":
            riders = riders + 2
            print("Please enter the ride")
        else:
            print("You are NOT allowed on this ride")
        #endIF
    else:
        print("You are NOT allowed on this ride")
    #endIF

# end for loop
