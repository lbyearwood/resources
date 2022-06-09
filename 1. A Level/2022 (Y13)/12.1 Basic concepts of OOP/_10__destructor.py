"""
a constructor is a special type of subroutine that is immediately called when a class is instatiated as an object.
It prepares the new object for use, often accepting arguments that the constructor uses to set required member attributes.
"""
class human:
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
    # __init__ the constructor
    def __init__(self, id, first_name, surname, date_of_birth, gender):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth,
        self.gender = gender


    def __del__(self):
        print('Destructor called, Human deleted.')