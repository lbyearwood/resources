class Human():
    countHumans = 0 # class variable
    def __init__(self,id,firstName,surname,DOB): # constructor
        # object variables
        self.id = id
        self.firstName = firstName
        self.surname = surname
        self.DOB = DOB
        self._pin = "6374"

    @property # getter
    def change_pin(self):
        return self._pin

    @change_pin.setter # setter
    def change_pin(self, newpin):
        self._pin = newpin

    def printPin(self):
        print(self._pin)

newPerson = Human(1,"Tina","Ford","15/08/2005")
newPerson.change_pin ="7082"
newPerson.printPin()
newPerson._pin = 3623
newPerson.printPin()