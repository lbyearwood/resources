list2D = []# empty list
cols = 3
rows = 5
word = "This is a message"

word = word.replace(" ","")
# ['This', 'is', 'a', 'message']

print(word)


for i in range(rows): # populate the list with lists of zeros
    list2D.append([0]*cols)

x = 0
for col in range(cols):
    for row in range(rows):
        if word[x] != " ": # if not a space character
            list2D[row][col] = word[x] # update list2d index
        x += 1  # increment the index of x

        if x >= len(word):
            break

for list in list2D:
    print(list)


for row in range(rows):
    for col in range(cols):
        print(list2D[row][col], end="")