# Planning
# 1) modularising problem - completed
# 2) what global data structures are needed, otherwise they are local?
# 3) what constructs are needed?

def breadSize():
    # get the user's choice
    userChoice = input("Enter [1] 6 inch - £1.65 or Enter [2] 12 inch - £2.05")
    if userChoice == "1":
        return 1.65 # return 1.65 for option 1
    elif userChoice == "2":
        return 2.05 # return 2.05 for option 2

def breadType():
    pass

def breadFillings():
    pass

def additionalFee():
    pass

def mainSub():
    price = 0
    breadSizeFee = breadSize()
    price = price + breadSizeFee