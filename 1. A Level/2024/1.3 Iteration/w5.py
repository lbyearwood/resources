test1= 0
test2 = 0
test3 = 0
totalYear = 0

# get test results for 30 pupils
for pupilNo in range (1,31):
	print(f"Pupil no. {pupilNo}")
	test1 = test1 + int(input("Enter score for test 1>>"))
	test2 = test2 + int(input("Enter score for test 2>>"))
	test3 = test3 + int(input("Enter score for test 3>>"))

totalYear = test1 + test2 + test3

# average score for each test
average1 = test1 / 30
average2 = test2 / 30
average3 = test3 / 30

# average score for all three test
averageYear = totalYear/3

# output the results
print("Average for test 1:", round(average1,2))
print("Average for test 2:", round(average2,2))
print("Average for test 3:", round(average3,2))
print("Average for all tests:", round(averageYear,2))

