from person_class import person

class child(person):

    # over the method
    def talk(self):
        print("Morning")

personB = child("Janet","Murray",12)
personB.talk()