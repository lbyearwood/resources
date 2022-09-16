fileName = "towns.txt"
def displayMenu():
   print("Please choose an option:")
   print("1. Enter a town name and its population")
   print("2. Print the town name with the largest population")
   print("3. Exit the program")
   userChoice = input(">>")
   return userChoice


def recordData():
   while True:
       townName = input("Enter the name of the town\n>>")
       townPopulation = input("Enter the population of the town\n>>")
       file = open(fileName,"a")
       file.writelines(townName + "\n")
       file.writelines(townPopulation + "\n")
       choice = input("input another town [Y] Yes or [N] No\n>>").upper()
       if choice == "N":
           file.close()
           break
       elif choice != "Y":
           print("Invalid input")

def printLargestPopulation():
   with open(fileName) as file:
       list = file.read().split("\n")

   largestTownName = list[0]
   largestPopulation = list[1]
   for i in range(3,len(list)-1,2):
       if int(list[i]) > int(largestPopulation):
           largestTownName = list[i-1]
           largestPopulation = list[i]
   print("The town with the largest population is",largestTownName)

while True:
   choice = displayMenu()
   match choice:
       case "1":
           recordData()
       case "2":
           printLargestPopulation()
       case "3":
           break
       case _:
           print("Invalid option! Try again")
