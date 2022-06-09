class apartment():
    _NextDoorNumber = 1 # class variable
    def __init__(self): # add door number
        self._DoorNumber = apartment._NextDoorNumber
        apartment._NextDoorNumber += 1

apartmentBuilding = []

def createAlistOfapartments():
    for i in range(10): # create 10 apartments
        aprt = apartment()
        apartmentBuilding.append(aprt)

def printListOfApartments():
    for apartment in apartmentBuilding:
        print("Door number:",apartment._DoorNumber)

createAlistOfapartments()
printListOfApartments()