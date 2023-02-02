class animal():
    def __init__(self,type,numberOfeyes,numberOfLegs):
        self.type = type
        self.numberOfeyes = numberOfeyes
        self.numberOfLegs = numberOfLegs
    @abstractMethod
    def makeSound(self):
       pass
    def move(self):
       pass
    def eating(self):
       pass
    def mating(self):
       pass

class cow(animal):
    pass

    # method overriding
    def makeSound(self):
        print("Moo")

class chicken(animal):
    pass

    # method overriding
    def makeSound(self):
        print("Cluck")



cow1 = cow("cow",2,4)
cow1.makeSound()
