
# this list will be used to print the months
# months[12]
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
temp = [] # empty list

def storeTemp(): # store the temp for every month
    for count in range(0,len(months)):
        tempVar = float(input(f"Enter the temp for {months[count]}"))
        temp.append(tempVar)

storeTemp() # call the procedure

# print the temperature for each month
def printTemps():
    for i in range(0,len(months)):
        print(f"the temperature for {months[i]} was {temp[i]} degree celsius")

printTemps() # use the procedure

def printHighestTemp():
    h = -100000000000000
    m = ""
    for x in range(0,len(temp)):
        if temp[x] > h:
            h = temp[x]
            m = months[x]

    print(f"The highest temperature in the year was in {m} at {h} degrees celsius")

printHighestTemp()