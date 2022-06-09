# __ double underscore = private
# _  single underscore = protected
# These are conventions only. Python is unable to enforce private attributes or methods
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
    age = 0
    _pin = "9823"

    @property # getter property
    def change_pin(self):
        return self._pin

    @change_pin.setter # setter property
    def change_pin(self,newpin):
        self._pin = newpin


new_person = human(id, "Tina", "Ford", "15/01/21", "female")

new_person.change_pin = "0907"

print(new_person._pin)