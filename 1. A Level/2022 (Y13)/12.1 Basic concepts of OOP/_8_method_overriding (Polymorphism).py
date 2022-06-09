class person():
    def __init__(self):
        self.firstname = "Tasha"
        self.surname = "Carble"

    # this method must be overridden
    def print_full_name(self):
        pass

class child(person): # inherit the person parent class
    def __init__(self):
        super().__init__() # use the constructor of the parent class

    def print_full_name(self): # polymorphism Overriding - is to change the behaviour of the inherited method
            print(self.firstname ,self.surname)



personB = child()
personB.print_full_name()

