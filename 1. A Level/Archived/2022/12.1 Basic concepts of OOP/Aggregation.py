# Aggregation (also known as **containment) is a specialised form of association.
# It defines a one-way relationship that specifies a 'has-a' relationship between two classes.
# For example, you can say that a team has players. However, the player does not need a team in order to exist,
# so the relationship is one-way. In a football management game, if you deleted the team,
# the player would continue to exist.

class player:
    def __init__(self, fname, surname, rating, shirtNumber):
        self.fname = fname
        self.surname = surname
        self.ability=rating
        self.shirtNumber = shirtNumber

    def get_ability(self):
       return (self.ability * 12)

    def get_name(self):
       return self.fname+" "+self.surname

class team:
    def __init__(self,name,stadium,wealth):
        self.name=name
        self.stadium=stadium
        self.wealth=wealth
        self.players = [] # players will be aggregated here

    def sign_player(self,player):
        self.players.append(player)

Ronaldo=player("Cristian","Ronaldo",100,"7") # Ronaldo will continue to exist even if man utd is destroyed
man_utd=team("Manchester United","Old Trafford",257000000)
man_utd.sign_player(Ronaldo) # The two classes are associated by Aggregation. Man utd contain ronaldo
print("Man utd have just signed", man_utd.players[0].get_addess())

