code = 0
oldModels = 0
totalCount = 0
while code !="9999":
    while True: # check if 4 digits
        code = input("enter 4 digit code")
        if len(code) !=4:
            print("Try again")
        else:
            if code[3] == "6" or code[3] == "7" or code[3] == "8":
                oldModels += 1 # augmented increment
            totalCount += 1
            break # break loop

print(f"Total old models entered is {oldModels}")
print(f"Total models entered is {totalCount-1}")
