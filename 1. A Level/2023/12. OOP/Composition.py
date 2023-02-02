class house:
    def __init__(self,doorNumber,address,value,type):
        self.doorNumber = doorNumber
        self.address = address
        self.value = value
        self.type = type
        self.Room1 = room("Living Room")
        self.Room2 = room("bedroom")
        self.Room3 = room("Kitchen")
        self.Room4 = room("Bath room")


class room:
    def __init__(self,type):
        self.type = type


house1 = house("67","Brass hays close", 235_000, "semi-detached")