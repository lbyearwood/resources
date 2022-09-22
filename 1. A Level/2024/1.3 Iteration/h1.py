letters = "kdfjghadkjhjgfdakgjndfkjmfndfgk"
smallestLetter = letters[0]
largestLetter = letters[0]
for i in range(0,len(letters)):
    # check if the current letter is larger than the largest stored letter
    if letters[i] > largestLetter:
        largestLetter = letters[i]
    if letters[i] < smallestLetter:
        smallestLetter = letters[i]

print(f"Smallest letter is {smallestLetter}")
print(f"largest letter is {largestLetter}")