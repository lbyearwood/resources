import random
rows = 12
cols = 4

finance_array = []

for i in range(rows):
    finance_array.append([0]*cols)


for row in range(rows):
    for col in range(cols):
        finance_array[row][col] = random.randint(30000,1200000)

for list in finance_array:
    print(list)


# answer 2
# Write an algorithm to print all the values for March between 2016 and 2019. You must use an iteration construct.
march = 0
for col in range(cols):
        march += finance_array[2][col]

print("The total sales for march covering 2016 to 2019 is £", march)

# answer 3
# Write an algorithm to add the values for Aug 2017 and Jun 2018 together.

sum = finance_array[7][1] + finance_array[5][2]

print(f"The sum of sales for Aug 2017 and Jun 2018 is £{sum:,}")

# answer 4
#Write an algorithm to produce the sum for all monthly sales in 2018
_2018 = 0
for row in range(rows):
        _2018 += finance_array[row][2]

print(f"The total sales for 2018 is £{_2018:,}")

# answer 5
# Write an algorithm to calculate the average sales for 2019
_2019 = 0
for row in range(rows):
        _2019 += finance_array[row][3]

avg = round(_2019 / rows,2)
print(f"The avg total sales for 2019 is £{avg:,}")