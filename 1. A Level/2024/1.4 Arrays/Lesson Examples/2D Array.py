row = 10
col = 10

# list comprehension
grid = [[0 for i in range(col)] for j in range(row)] # initialise the grid with 0s
grid[9][9] = 1
for list in grid:
    print(list)
