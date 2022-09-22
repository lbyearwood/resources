while True: # infinite loop
    threeDigitNumber = input("Enter a three digit number")
    if len(threeDigitNumber) != 3:
        print("Error... Try again")
    else:
        break

# e.g 378
threeDigitNumber = int(threeDigitNumber) # convert to integer
hundreds = threeDigitNumber // 100 # e.g 3
tens = (threeDigitNumber % 100) // 10 # e.g 7
units = (threeDigitNumber % 100) % 10 # e.g 8

print(hundreds, ("hundred " if hundreds == 1 else "hundreds "), end="")
print(tens, ("ten " if tens == 1 else "tens "), end="")
print(units, ("unit " if units == 1 else "units "), end="")

# ternary operator