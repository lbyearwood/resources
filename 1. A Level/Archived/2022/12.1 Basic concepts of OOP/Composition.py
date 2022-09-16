# Composition is a stricter form of association. It defines a one-way relationship
# that specifies an 'is-part-of' relationship between two classes.
# For example, you can say that a room is part of a house. The rooms cannot exist outside of the house.
# In a town planning simulation, if you deleted a house object, the rooms would also be deleted.
class house:
    def __init__(self, door_number, address, value, type):
        self.doorNumber = door_number
        self.address = address
        self.value=value
        self.type = type
        # the instantiation of the rooms are composed below
        self.Room1 = room("Parents Bedroom")
        self.Room2 = room("Children Bedroom")
        self.Room3 = room("Living room")
        self.Room4 = room("Kitchen")
        self.Room5 = room("Bathroom")

    def get_value(self):
       return (self.value)

    def get_addess(self):
       return self.doorNumber + " " + self.address

class room:
    def __init__(self,type):
        self.type=type

house1 = house("54", "Barthelow Close", 850000, "Semi-detached")

print(house1.get_addess())

