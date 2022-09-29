import random
total = [0,0,0,0]
outletSales = [[random.randint(10000,80000) for cols in range(4)] for rows in range(50)]


for quarter in range(4):
    for row in range(50):
        total[quarter] += outletSales[row][quarter]
    print(f"The total for {quarter+1} quarter is £{total[quarter]}")