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


def emptyCarPark(): # complete
    global carPark
    carPark = [["empty" for cols in range(25)] for rows in range(20)]

def parkACar():
    reg = input("Please enter your car reg")
    while True:  # infinite loop
        row = int(input("Please enter a row between 1 and 20"))
        col = int(input("Please enter a column between 1 and 25"))
        if (row >= 1 and row <= 20) and (col >= 1 and col <= 25):
            # subtract 1 to handle array index
            col -= 1
            row -= 1
            if carPark[row][col] == "empty":
                carPark[row][col] = reg
                print("Car park space booked")
                break
            else:
                print("Space taken! Please select another space")
        else:
            print("Please enter a valid row and column")

def removeACar():
    pass

def displayCarParkGrid(): # complete
    for row in carPark:
        print(row)  # print the row

while True:
    menu()