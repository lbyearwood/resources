# populate by inline assignment
letters = ["d","f","a","r","k","q","n","z","i","o"]

# populate by appending
letters.append("y")
found = False
searchItem = "s"

# search the array / list for an item
for i in range(0,len(letters)):
    if letters[i] == searchItem:
        found = True # if the item is found set it to True
        break

# print the search result to the user
if found == True:
    print("letter found")
else:
    print("Not found")
