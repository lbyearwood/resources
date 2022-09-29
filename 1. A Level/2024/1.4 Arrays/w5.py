grid = [["x" for cols in range(4)] for rows in range(6)] # populate the grid
grid [0][0] = "o" # set the default value
for row in grid:
    print(row)

while True:
    while True: # validate user input
        row = int(input("enter row"))
        col = int(input("enter col"))
        if (col >= 1 and col <=4) and (row >= 1 and row <=6):
            col -=1 # sanitize the input
            row -=1
            break
        else:
            print("Error try again")

    grid = [["x" for cols in range(4)] for rows in range(6)] # clear grid

    grid[row][col] = "o" # update player position

    for row in grid: # print grid
        print(row)

