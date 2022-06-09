class human:
    # __init__ intialize the constructor
    def __init__(self, id, first_name, surname, date_of_birth, gender):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth,
        self.gender = gender
        self.weight = None
        self.height = None
        self.bloodType = None
        self.hair_colour = None
        self.hair_length = None
        self.eye_colour = None
        self.intelligence = None
        self.siblings = None
        self.family = []
        self.wealth = None
        self.health = None
        self.x_location = None
        self.y_location = None
        self.nationality = None
        self.status = None

    def talk(self,message):
        print(message)