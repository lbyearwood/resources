# run-time error - this error will cause the program to crash
# logical / human error - this error will not crash
# the program, however the program will not perform as intended
# syntax error - similar to the grammar rules of a language

name=["aishah","iman","mohammed","ku","jess","declan"]

searchItem = input("Enter student name").lower()
try:
    recordNumber = name.index(searchItem)
    recordNumber += 1
    print(f"{searchItem}'s record number is {recordNumber}")
except Exception as e:
    print("Record not found")




