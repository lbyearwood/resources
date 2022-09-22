name=["aishah","iman","mohammed","ku","jess","declan"]

searchItem = input("Enter student name").lower()
recordNumber = 0
found = False
for i in range(0,len(name)):
    if name[i] == searchItem:
        recordNumber = i + 1 # record number
        found = True

if found == True:
    print(f"{searchItem}'s record number is {recordNumber}")
else:
    print("not found")



fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)


