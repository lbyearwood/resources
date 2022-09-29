grid = []
rows = 10
cols = 6
defaultValue = "empty"

for i in range(rows):
    grid.append([defaultValue]*cols)

for row in grid:
    print(row)


grid[0][0]  = "dsdafgf32"

option = input("Would you like to park a car? Y/N").upper()
reg = input("Please enter your car reg")
while True: # infinite loop
    if option == "Y":
        row = int(input("Please enter a row between 1 and 10"))
        col = int(input("Please enter a column between 1 and 6"))
        if (row >= 1 and row <=10) and (col >= 1 and col <=6):
            col -= 1
            row -= 1
            if grid[row][col] == "empty":
                grid[row][col] = reg
                print("Car space booked")
                break
            else:
                print("Please select another space")
        else:
            print("Please enter a valid row and column")