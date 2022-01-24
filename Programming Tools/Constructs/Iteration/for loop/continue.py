# the continue statement will skip an iteration

for i in range(1,6):
    continue # skip every iteration
    print("i =",i)

for i in range(1, 6):
    if i == 3:  # Skip the iteration if i = 3. Continue with the next iteration:
        continue
    print("i =", i)

