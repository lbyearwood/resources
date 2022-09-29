mark = int(input("Please enter your mark"))
attendancePercentage = int(input("Please enter your attendance rate"))
if attendancePercentage >= 90:
    if mark > 90:
        print("Your grade is an A")
    elif mark > 80:
        print("Your grade is an B")
    elif mark > 70:
        print("Your grade is an C")
    else:
        print("A mark less than 71 means you have failed")
else:
    print("A attendance rate less than 90% means you have failed")


# alternative using match case

match mark:
        case mark if mark > 90:
            print("Your grade is an A")
        case mark if mark > 80:
            print("Your grade is an B")
        case mark if mark > 70:
            print("Your grade is an C")
        case _: # case anything else
            print("A mark less than 71 means you have failed")