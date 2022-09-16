binaryString = "101001110001110001000111111000111000"
def majority_vote(one,two,three):
    x = 0
    if one == "1":
        x += 1
    if two == "1":
        x += 1
    if three == "1":
        x += 1
    if x >= 2:
        return 1
    else:
        return 0

def majority_vote2(one, two, three):
    binaryString1 = one + two + three
    num = binaryString1.index("1")
    if num >= 2:
        return 1
    else:
        return 0

for i in range(0,len(binaryString), 3):
    one = binaryString[i]
    two = binaryString[i + 1]
    three = binaryString[i + 2]
    digit = majority_vote2(one,two, three)
    print(digit)





