_2DArray = [[0 for cols in range(10)] for rows in range(10)]


# this will traverse across a row
for row in range(10):
    for col in range(10):
        print(_2DArray[row][col])

# this will traverse down a column
for col in range(10):
    for row in range(10):
        print(_2DArray[row][col])
