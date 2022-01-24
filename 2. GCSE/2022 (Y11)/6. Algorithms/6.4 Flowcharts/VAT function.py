def findVAT(total): # subroutine with one parameter
    vat = total * 0.2
    return vat

total1 = float(input("enter total"))
total2 = total1 + findVAT(total1) # calling code with total1 as the argument
# ? = 100.0 + 20.0
print(total2)