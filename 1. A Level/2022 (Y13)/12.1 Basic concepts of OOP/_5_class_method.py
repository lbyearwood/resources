"""
Class methods can be called without create an instance (object) of the class.
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
    age = 0
    #constructor
    def __init__(self, id, first_name, surname, date_of_birth, gender):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth,
        self.gender = gender
        self.age = 19


    @classmethod
    def view_age(self):
        print(self.age) # class method can access class attributes

    @classmethod
    def view_name(self):
        print(self.first_name)# class method cannot access object attributes

person = human(1,"Bob","Brown","23/08/1991","male")

person.view_age()
person.view_name()