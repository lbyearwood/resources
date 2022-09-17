score = 0
count = 0
total = 0
while score !=-1:
    score = int(input("enter a number"))
    count += 1
    total += score

print(f"The average score was {total/count}")
