grid = []

def populateGrid():
        grid.append(["1","2","3"])
        grid.append(["4","5","6"])
        grid.append(["7", "8","9"])

def printGrid():
    for list in grid:
        print(list)

def choosePosition():
    cellPos = int(input("Please select a position (1 - 9)"))
    while cellPos < 1 or cellPos > 9:
            print("Invalid position. Try again")


def runGame():
    populateGrid()
    printGrid()
    choosePosition()

runGame()

