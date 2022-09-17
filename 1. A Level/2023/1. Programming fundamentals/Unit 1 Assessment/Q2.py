Temperature = 0
Highest = 0
Lowest = 50
Total = 0
for index in range (1 ,6):
	Temperature = input("Enter Temperature")
	if Temperature > Highest:
		Highest = Temperature

	if Temperature < Lowest:
		Lowest = Temperature
	Total = Total + Temperature

Average = Total / 5
print("Highest:", Highest)
print("Lowest", Lowest)
print("Average", Average)

