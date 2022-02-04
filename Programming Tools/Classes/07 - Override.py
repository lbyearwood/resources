from person_class import person

class child(person):
    # over the method
    def talk(self, house):
        print("Morning")
        return True
personB = child("Janet","Murray",12)
personB.talk()