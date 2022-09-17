total = 0 # assign total 0

while not(total >= 1.50): # check if the condition is false
    total = total + float(input("Enter coins"))

print("Dispense drink")

if total > 1.50:
    change = total - 1.5
    print("your change is",change)






