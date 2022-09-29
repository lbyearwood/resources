class secondPlayer():

    def __init__(self):
        self.Dictionary = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }
    def checkWinAndDraw(self):
        Xwin = False
        Owin = False
        draw = True
        # checks each row for a win
        for i in range (1,10,3):
            if self.Dictionary[i] == "X" and self.Dictionary[i+1] == "X" and self.Dictionary[i+2] == "X":
                Xwin = True
            if self.Dictionary[i] == "O" and self.Dictionary[i+1] == "O" and self.Dictionary[i+2] == "O":
                Owin = True
        #checks each column for a win
        for i in range (1,4):
            if self.Dictionary[i] == "X" and self.Dictionary[i+3] == "X" and self.Dictionary[i+6] == "X":
                Xwin = True
            if self.Dictionary[i] == "O" and self.Dictionary[i+3] == "O" and self.Dictionary[i+6] == "O":
                Owin = True
        #checks diagnol wins
        if self.Dictionary[1] == "X" and self.Dictionary[5] == "X" and self.Dictionary[9] == "X":
            Xwin = True
        if self.Dictionary[3] == "X" and self.Dictionary[5] == "X" and self.Dictionary[7] == "X":
            Xwin = True
        if self.Dictionary[1] == "O" and self.Dictionary[5] == "O" and self.Dictionary[9] == "O":
            Owin = True
        if self.Dictionary[3] == "O" and self.Dictionary[5] == "O" and self.Dictionary[7] == "O":
            Owin = True
        if Owin == False and Xwin == False:
            for i in range(1,10):
                if self.Dictionary[i] == "":
                    draw = False
        #retunrs the winner to the main game class
        if Owin:
            return "O"
        if Xwin:
            return "X"
        if draw:
            return "draw"




    # def checkDraw(self,Owin,Xwin):
    #     if Owin == False and Xwin == False:
    #         draw = True
    #         for i in range(1,10):
    #             if self.Dictionary[i] == "":
    #                 draw = False
    #     return draw

    def updateDictionary(self, btnNum,symbol):
        if self.Dictionary[btnNum] != "":
            print("button already pressed")
            print(self.Dictionary)
            return False
        else:
            self.Dictionary.update({btnNum:symbol})
            return True
        print(self.Dictionary)


