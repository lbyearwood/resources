import random
babies = [random.randint(1500,4000) for i in range(100)]
total = 0
for weight in babies:
    total +=weight
avg = total / len(babies)
count = 0
threshold = avg-500
for weight in babies:
    if weight < (threshold):
        count+=1
print(f"The number of babies below the threshold {threshold} is {count}")
print(f"The average is {avg}")

