from datetime import datetime

class Human:
    countHumans = 0 # class variable
    def __init__(self,id,firstName,surname,DOB): # constructor
        # object variables
        self.id = id
        self.firstName = firstName
        self.surname = surname
        self.DOB = DOB
    def _talk(self,message):
        print(message)
        self.__test()

    def __test(self):
        self._talk("test")

class Child(Human): # inherit the Human class properties and methods
    pass

if __name__ == "__main__":

    newPerson = Child(1,"Tom","Brown","10/01/2023")
    newPerson.test()
    newPerson1 = Human(1,"Bob","Brown","10/01/2023")
    newPerson1.test()
    print(newPerson1.firstName)







