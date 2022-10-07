import  random
grid = [[0 for cols in range(10)] for rows in range(10)]

x = random.randint(0,9)
y = random.randint(0,9)

grid[x][y] = 1
print(grid)