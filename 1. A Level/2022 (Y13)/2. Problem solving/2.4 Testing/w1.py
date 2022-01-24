def validateInput():
    validInput = False
    while not(validInput):
        highestTemp = int(input("Please enter max temp, 999 to finish "))
        lowestTemp = int(input("Please enter lowest temp "))

        if (highestTemp <= 80 and highestTemp >=-108) \
                and (lowestTemp <= 80 and lowestTemp >=-108) \
                or (lowestTemp == 999 and highestTemp == 999) : # if temp within range
               return lowestTemp, highestTemp
        else:
            print("invalid inputs, please try again")


# Unit 2 Problem Solving Lesson 4 Worksheet question 1
highestTemp = 0
lowestTemp = 0
list_of_highest_temp = []
list_of_lowest_temp = []
totalMaxTemp = 0
numDaysRecorded = 0
daysAboveAverage = 0
noDaysSubZero = 0

# TASK: validate the user input

while highestTemp != 999 and lowestTemp !=999:
    lowestTemp,highestTemp = validateInput()
    list_of_highest_temp.append(highestTemp)
    list_of_lowest_temp.append(lowestTemp)
    numDaysRecorded = numDaysRecorded + 1
    totalMaxTemp = totalMaxTemp + highestTemp
    if lowestTemp < 0:
        noDaysSubZero = noDaysSubZero + 1
    # endif


# endwhile

averageMaxTemp = totalMaxTemp / numDaysRecorded

daysAboveAverage = 0
for n in range(0, numDaysRecorded):
    if list_of_highest_temp[n] > averageMaxTemp:
        daysAboveAverage = daysAboveAverage + 1
    # ENDIF
# ENDFOR

print("Days max temp above average ", daysAboveAverage)
print("Days min temperature below zero ", noDaysSubZero)
