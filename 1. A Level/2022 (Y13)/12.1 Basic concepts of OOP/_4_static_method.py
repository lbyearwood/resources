"""
Static methods can be called without create an instance (object) of the class.
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


    def talk(self,message):
        print(message)

    @staticmethod
    def talk(message):
        print(message)

person = human(1,"Bob","Brown","23/08/1991","male")

human.talk("Hello world")