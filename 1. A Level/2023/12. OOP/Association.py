class player:
    def __init__(self,fname,sname,rating,shirtnumber):
        self.fname = fname
        self.sname = sname
        self.rating = rating
        self.shirtNumber = shirtnumber

class team:
    def __init__(self, name, stadium, wealth):
        self.teamName = name
        self.stadium = stadium
        self.wealth = wealth
        self.players = []


    def signPlayer(self,player):
        self.players.append(player)
        print(f"{self.teamName} have signed {player.fname} {player.sname}")


Ronaldo = player("Cristian","Ronaldo",92,"7")

manUtd = team("Manchester United", "Old Trafford", 333_000_000)
manUtd.signPlayer(Ronaldo)