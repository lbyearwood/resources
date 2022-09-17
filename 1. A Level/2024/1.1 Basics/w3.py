#### PLANNING ####
# INPUT NoStudents
# INPUT NoBooks
# BooksPerStudent = NoBooks // NoStudents
# OUTPUT BooksPerStudent
# BooksLeftOver = NoBooks % NoStudents
# OUTPUT BooksLeftOver

# Convert to Python
noStudents = int(input("Enter number of students"))
noBooks = int(input("Enter number of books"))
booksPerStudent = noBooks // noStudents
print(f"Books per student: {booksPerStudent}")
booksLeftOver = noBooks % noStudents
print(f"Books left over: {booksLeftOver}")
