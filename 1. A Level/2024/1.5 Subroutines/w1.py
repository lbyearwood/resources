def timesTable(table, startNum, endNum, pupilName):
    print(f"hi", pupilName, "here is your times table")
    for i in range(startNum,endNum+1):
        product = table * i
        print(f"{table} x {i} = {product}")


name = input("Enter your name")
t = int(input("What times table would you like to calculate?"))
s = int(input("Enter start point"))
e = int(input("Enter end point"))

timesTable(t,s,e,name)