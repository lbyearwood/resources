# Write a python program that will:
# -Print all odd numbers between 1 and 2000
# - Append all even numbers to a list between 1 and 2000
evens = []
for i in range(1,2001): # print odd numbers using step argument
    if i % 2 == 1:
        print(i)
    else:
        evens.append(i)
        
print(evens)
