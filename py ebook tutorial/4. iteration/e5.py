import random

for i in range(1000):
    total = 0
    for x in range(10):
        total += random.randint(1,10)
    print(f"average = {total/10}")



