"""
Class methods defines what the class can do as an object. It defines how an object behaves in a program
"""
class human:
    #constructor
    def __init__(self, id, first_name, surname, date_of_birth, gender):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth,
        self.gender = gender
    weight = None
    height = None
    bloodType = None
    hair_colour = None
    hair_length = None
    eye_colour = None
    intelligence = None
    siblings = None
    family = []
    wealth = None
    health = None
    x_location = None
    y_location = None
    nationality = None
    status = None
    # define the class methods
    def talk(self, message):
        print(message)

person = human(1,"Bob","Brown","23/08/1991","male")

person.talk("Hello world")
