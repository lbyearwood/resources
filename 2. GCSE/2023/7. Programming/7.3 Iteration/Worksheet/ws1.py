score = 0
count = 0
while score !=-1:
    score = int(input("enter a number"))
    if score > 100:
        count += 1
        print(f"You have entered {count} numbers over 100")