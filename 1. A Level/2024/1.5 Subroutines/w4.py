carPark = [["empty" for cols in range(25)] for rows in range(20)]

def menu():
    # display menu of options
    print("1. Reset all spaces in the car park to 'empty'")
    print("2. Park a car")
    print("3. Remove a car")
    print("4. Display the car park grid")
    print("5. Quit")
    while True:
        option = input("Enter your choice: ")

        if option == "1":
            emptyCarPark()
            break
        elif option == "2":
            parkACar()
            break
        elif option == "3":
            removeACar()
            break
        elif option == "4":
            displayCarParkGrid()
            break
        elif option == "5":
            print("Goodbye")
            exit()
        else:
            print("Please choose a value option between 1 and 5")


def emptyCarPark():
    pass

def parkACar():
    pass

def removeACar():
    pass

def displayCarParkGrid():
    for row in carPark:
        print(row)  # print the row


menu()