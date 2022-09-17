class person:
    hair_colour = None
    age = None
    first_name = None
    surname = None
    nationality = None
    def __init__(self,fn,sn,ag):
        # decide what needs to occur before the object is created
        self.first_name = fn
        self.surname = sn
        self.age = ag
    def __del__(self):
        pass


personA = person("Joe","Bloggs",0) # instantiated the object

print(personA.first_name)

