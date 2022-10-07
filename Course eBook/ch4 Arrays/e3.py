import random
mark = [[random.randint(0,100) for cols in range(3)] for rows in range(5)]
total  = 0
for rows in range(0,5):
    avg = 0
    for cols in range(0,3):
        avg += mark[rows][cols]
        total += mark[rows][cols]
    avg = round(avg / 3,2)
    print(f"The average for student {rows+1} is {avg}")
    print(f"The class average {round(total/15)}")
