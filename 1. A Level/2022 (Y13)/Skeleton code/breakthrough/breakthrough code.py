# Skeleton Program code for the AQA A Level Paper 1 Summer 2022 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.9 programming environment

import random
import os


def Main():
    ThisGame = Breakthrough()
    ThisGame.PlayGame() # call the playgame


class Breakthrough():
    def __init__(self):
        self.__Deck = CardCollection("DECK")
        self.__Hand = CardCollection("HAND")
        self.__Sequence = CardCollection("SEQUENCE")
        self.__Discard = CardCollection("DISCARD")
        self.__Score = 0
        self.__Locks = []
        self.__GameOver = False
        self.__CurrentLock = Lock()
        self.__LockSolved = False
        self.__LoadLocks()
        self.__MulliganUsed = False # solution4 - set default value for mMlliganUsed
        self.bonusCounter = 0 # solution9 - create a bonus counter

    def PlayGame(self):
        if len(self.__Locks) > 0: # if there are locks left to complete
            self.__SetupGame() # complete
            while not self.__GameOver:
                self.__LockSolved = False
                while not self.__LockSolved and not self.__GameOver:
                    print()
                    print("Current score:", self.__Score) # print the score
                    print(self.__CurrentLock.GetLockDetails(self.__Sequence)) # solution8 pass through sequence # gets the locks details and print its
                    print(self.__Sequence.GetCardDisplay()) # get the card sequence and print it
                    print(self.__Hand.GetCardDisplay()) # need to double check the separator
                    MenuChoice = self.__GetChoice() # explored
                    if MenuChoice == "D":
                        print(self.__Discard.GetCardDisplay()) # explored
                    elif MenuChoice == "P": # solution2 handle peek choice option
                        if not self.__CurrentLock.GetPeekUsed(): # prevent user double selecting P
                            print("Peek option executed")
                            print("The top three cards in the deck are")
                            for i in range(3):
                                print(f"{i+1}.",self.__Deck.GetCardDescriptionAt(i)) # print the card descriptions
                            self.__CurrentLock.SetPeekUsed() # set peek used to true
                    elif MenuChoice == "M":  # solution4 handle mulligan choice option
                        if not(self.__MulliganUsed):
                            for count in range(self.__Hand.GetNumberOfCards()): # solution4 - iterate through the hand collection
                                self.__MoveCard(self.__Hand,self.__Deck, self.__Hand.GetCardNumberAt(0)) # move card to deck
                            for count in range(self.__Sequence.GetNumberOfCards()): # solution4 - iterate through the hand collection
                                self.__MoveCard(self.__Sequence,self.__Deck, self.__Sequence.GetCardNumberAt(0)) # move card to deck
                            for count in range(self.__Discard.GetNumberOfCards()): # solution4 - iterate through the hand collection
                                self.__MoveCard(self.__Discard,self.__Deck, self.__Discard.GetCardNumberAt(0)) # move card to deck
                            self.__Deck.Shuffle() # shuffle the deck
                            self.__MulliganUsed = True
                            for i  in range(5): # move 5 cards back in to the playe's hand
                                while self.__Deck.GetCardDescriptionAt(0) == "Diff": # check if the card is a diff card
                                    self.__MoveCard(self.__Deck,self.__Discard, self.__Deck.GetCardNumberAt(0)) # move move from deck to discard
                                self.__MoveCard(self.__Deck,self.__Hand, self.__Deck.GetCardNumberAt(0)) # move card into player's hand
                            print("Mulligan Complete. All cards were recollected, shuffled and redistributed") # update the user
                    elif MenuChoice == "U":
                        self.bonusCounter +=1 # solution9 increment by one when the user's uses
                        CardChoice = self.__GetCardChoice() # if choice out of range program will crash
                        DiscardOrPlay = self.__GetDiscardOrPlayChoice() # should return D or P
                        if DiscardOrPlay == "D": #  if the user has chosen to discard the card
                                    # (fromCollection , toCollection, Card number to be moved)
                            self.__MoveCard(self.__Hand, self.__Discard, self.__Hand.GetCardNumberAt(CardChoice - 1))
                            self.__GetCardFromDeck(CardChoice)
                        elif DiscardOrPlay == "P": #  if the user has chosen to play the card
                            self.__PlayCardToSequence(CardChoice) # explored
                    if self.__CurrentLock.GetLockSolved():
                        if self.bonusCounter >= 20: # solution9
                            print("You have received 0 bonus points")
                        else:
                            print(f"You have received {20 - self.bonusCounter} bonus points")
                            self.__Score += (20 - self.bonusCounter)
                        self.__LockSolved = True # set lock status to True
                        self.__ProcessLockSolved() # process the locked being solved

                    if MenuChoice == "Q": # solution5
                        self.__GameOver = True # set game over are True to exit the loop
                        self.__Score += self.__Deck.GetNumberOfCards() # add the number of cards in the deck to the players score
                        print("Final score:", self.__Score) # print score
                        print("Game over")
                    else:
                        self.__GameOver = self.__CheckIfPlayerHasLost()
        else:
            print("No locks in file.")

    # explored and complete
    def __ProcessLockSolved(self):
        self.__Score += 10 # add 10 to score for solving the lock
        print("Lock has been solved.  Your score is now:", self.__Score)
        while self.__Discard.GetNumberOfCards() > 0: # while there are discarded cards

            # move the top card from the discard collection to the deck
            self.__MoveCard(self.__Discard, self.__Deck, self.__Discard.GetCardNumberAt(0))

        # solution7 - adding multi tool kit cards
        NewCard = ToolCard("P", "m")
        self.__Deck.AddCard(NewCard)
        NewCard = ToolCard("K", "m")
        self.__Deck.AddCard(NewCard)
        NewCard = ToolCard("F", "m")
        self.__Deck.AddCard(NewCard)
        if random.randint(1,4) == 2: # solution10 - create a 25% chance that the sub is called
            self.___AddGeniusCardToDeck()

        self.__Deck.Shuffle() # shuffle the cards again
        self.__CurrentLock = self.__GetRandomLock() # generate a new lock object

    def __CheckIfPlayerHasLost(self):
        #  check if there are no more cards in the deck
        if self.__Deck.GetNumberOfCards() == 0:
            print("You have run out of cards in your deck.  Your final score is:", self.__Score)
            return True
        else:
            return False

    def __SetupGame(self):
        Choice = input("Enter L to load a game from a file, anything else to play a new game:> ").upper()
        if Choice == "L": # if choice is to load a game
            if not self.__LoadGame("game1.txt"): # pass through game1.txt as an argument
                self.__GameOver = True # if the text file does not exist the game is over
        else:
            self.__CreateStandardDeck() # generate the deck
            self.__Deck.Shuffle() # shuffle the cards

            for count in range(5): # iterate to give the user 5 cards
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))





            self.__AddDifficultyCardsToDeck() #  add 5 diff cards to the deck
            self.__Deck.Shuffle() # shuffle the deck again
            self.__CurrentLock = self.__GetRandomLock() # generate a random lock

    def __PlayCardToSequence(self, CardChoice):
        # solution7 check if the card is a multi tool card
        if "m" in self.__Hand.GetCardDescriptionAt(CardChoice - 1):
            while True:
                toolkit = input("Pick a tool kit [a]cute, [b]asic or [c]rude").lower()
                if toolkit == "a" or toolkit == "b" or toolkit == "c":
                    break
                else:
                    print("Invalid choice, try again")
            self.__Hand.SetCardToolKit(CardChoice - 1,toolkit) # swap card


        # if the sequence collection has at least one card
        if self.__Sequence.GetNumberOfCards() > 0:
            # if the TootlType is not the same as the previous card play
            # explained
            if self.__Hand.GetCardDescriptionAt(CardChoice - 1)[0] != self.__Sequence.GetCardDescriptionAt(self.__Sequence.GetNumberOfCards() - 1)[0]:
                self.__Score += self.__MoveCard(self.__Hand, self.__Sequence,self.__Hand.GetCardNumberAt(CardChoice - 1))
                self.__GetCardFromDeck(CardChoice) # get another card from the deck
        else: # if there are no cards in the sequence to compare then
            # move the card from the hand collection to the sequence collection and update the score for playing a card
            self.__Score += self.__MoveCard(self.__Hand, self.__Sequence, self.__Hand.GetCardNumberAt(CardChoice - 1))
            self.__GetCardFromDeck(CardChoice) #get another card from the deck collection

        if self.__CheckIfLockChallengeMet():
            print()
            print("A challenge on the lock has been met.")
            print()
            self.__Score += 5 # if a challenge within the lock has been met add 5 to the score

    def __CheckIfLockChallengeMet(self):
        SequenceAsString = "" # empty string
        # loop through sequence collection backwards
        for Count in range(self.__Sequence.GetNumberOfCards() - 1, max(0, self.__Sequence.GetNumberOfCards() - 3) - 1,-1):
            if len(SequenceAsString) > 0: # if the sequence is not empty
                SequenceAsString = ", " + SequenceAsString # add a separator between

            # get the card description of every sequence card that has been played and append it to SequenceAsString
            SequenceAsString = self.__Sequence.GetCardDescriptionAt(Count) + SequenceAsString

            if self.__CurrentLock.CheckIfConditionMet(SequenceAsString): # check if any challenge has been met
                return True # return true if the challenge for the current lock has been met
        return False

    def __SetupCardCollectionFromGameFile(self, LineFromFile, CardCol):
        if len(LineFromFile) > 0:
            SplitLine = LineFromFile.split(",")
            for Item in SplitLine:
                # if the has 5 characters
                if len(Item) == 5:
                    CardNumber = int(Item[4]) # assign the card number if single digit
                else:
                    CardNumber = int(Item[4:6])# assign the card number if double digit

                if Item[0: 3] == "Dif": # if it is a difficulty card
                    CurrentCard = DifficultyCard(CardNumber)
                    CardCol.AddCard(CurrentCard)
                else:
                    CurrentCard = ToolCard(Item[0], Item[2], CardNumber)
                    CardCol.AddCard(CurrentCard)

    def __SetupLock(self, Line1, Line2):
        SplitLine = Line1.split(";") # create a list of conditions (symbols)
        for Item in SplitLine:
            # split the list item using the (,) as a delimeter
            Conditions = Item.split(",")
            # access the current lock and add each condition (card symbol)
            self.__CurrentLock.AddChallenge(Conditions)
        # create a list of statuses
        SplitLine = Line2.split(";")
        for Count in range(0, len(SplitLine)):
            # if the challenge has been met i.e. = Y
            if SplitLine[Count] == "Y":
                # Set the challenge as True for this lock
                self.__CurrentLock.SetChallengeMet(Count, True)

    def __LoadGame(self, FileName): # game.txt
        try:
            with open(FileName) as f:
                LineFromFile = f.readline().rstrip() # read the score
                self.__Score = int(LineFromFile)
                LineFromFile = f.readline().rstrip() # load the past lock challenges
                LineFromFile2 = f.readline().rstrip() # load the past success rate for each challenge
                self.__SetupLock(LineFromFile, LineFromFile2) # set up a lock
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Hand) # completed
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Sequence)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Discard)
                LineFromFile = f.readline().rstrip()
                self.__SetupCardCollectionFromGameFile(LineFromFile, self.__Deck)
                return True
        except:
            print("File not loaded")
            return False

    def __LoadLocks(self):
        FileName = "locks.txt"
        self.__Locks = []
        try:
            with open(FileName) as f:
                LineFromFile = f.readline().rstrip()
                while LineFromFile != "": # while there is something to read do the following
                    Challenges = LineFromFile.split(";") # create a list of challenges
                    LockFromFile = Lock() # create a lock for the list of challenges
                    for C in Challenges:
                        Conditions = C.split(",") # create a list of conditions for the challenge
                        LockFromFile.AddChallenge(Conditions) # add the challenge to the lock and add the conditions to the challenge
                    self.__Locks.append(LockFromFile) # append the lock to the list of locks
                    LineFromFile = f.readline().rstrip() # read the next line and start the price again
        except:
            print("File not loaded")

    # select a random lock from the list of locks
    def __GetRandomLock(self):
        return self.__Locks[random.randint(0, len(self.__Locks) - 1)]

    # this sub is used to moved a card from the deck to the players hand
    def __GetCardFromDeck(self, CardChoice):#
        # check that the deck is not empty
        if self.__Deck.GetNumberOfCards() > 0:
            # get the card decripton to the top card in the deck, if it is a Difficulty card then
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0)) # remove Dif card from the deck
                print()
                print("Difficulty Card encountered!") # inform the user
                print(self.__Hand.GetCardDisplay()) # display the user's hand
                self.__Deck.DisplayStats() # solution6  display the stats
                print("To deal with this you need to either lose a key ", end='') # user instuction given
                Choice = input("(enter 1-5 to specify position of key) or (D)iscard five cards from the deck:> ")
                print()
                self.__Discard.AddCard(CurrentCard) # add the dif card to the discard collection

                CurrentCard.Process(self.__Deck, self.__Discard, self.__Hand, self.__Sequence, self.__CurrentLock,Choice, CardChoice)

            elif self.__Deck.GetCardDescriptionAt(0) == "Gen": #solution10
                CurrentCard = self.__Deck.RemoveCard(self.__Deck.GetCardNumberAt(0))  # remove Dif card from the deck
                print()
                print("Genius Card encountered!")  # inform the user
                print(self.__Hand.GetCardDisplay())  # display the user's hand
                numChallenges = self.__CurrentLock.GetNumberOfChallenges()

                choice = input(f"Choose a challenge 1 to {numChallenges} to solve or [d]iscard and reshuffle").lower()

                if choice == "d":
                    self.__Discard.AddCard(CurrentCard) # add the card
                else:
                    # pass the arguments needed to solve / process the challenge in a lock
                    CurrentCard.Process(self.__CurrentLock,choice,numChallenges)

        # while the user has less than 5 cards and there cards still in the deck
        while self.__Hand.GetNumberOfCards() < 5 and self.__Deck.GetNumberOfCards() > 0:
            if self.__Deck.GetCardDescriptionAt(0) == "Dif":
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))
                print("A difficulty card was discarded from the deck when refilling the hand.")
            elif self.__Deck.GetCardDescriptionAt(0) == "Gen":
                self.__MoveCard(self.__Deck, self.__Discard, self.__Deck.GetCardNumberAt(0))
                print("A genius card was discarded from the deck when refilling the hand.")
            else:
                self.__MoveCard(self.__Deck, self.__Hand, self.__Deck.GetCardNumberAt(0))
        if self.__Deck.GetNumberOfCards() == 0 and self.__Hand.GetNumberOfCards() < 5:
            self.__GameOver = True

    # explored
    def __GetCardChoice(self):
        Choice = None # set to none
        while Choice is None: # while none
            try:
                Choice = int(input("Enter a number between 1 and 5 to specify card to use:> "))
            except:
                pass
        return Choice # return a value between 1 and 5

    # explored
    def __GetDiscardOrPlayChoice(self):
        Choice = input("(D)iscard or (P)lay?:> ").upper()
        return Choice # should return D or P

    # explored
    def __GetChoice(self):
        print()
        options = "(D)iscard inspect, (U)use card"
        if not (self.__CurrentLock.GetPeekUsed()): # solution2 - add peek option to user menu
            options += ", (P)eek"
        if not (self.__MulliganUsed): # solution4 - add Mulligan option to user menu
            options += ", (M)ulligan"

        options += ", (Q)uit:>"
        Choice = input(options).upper()
        return Choice

    def __AddDifficultyCardsToDeck(self):
        for Count in range(5):
            self.__Deck.AddCard(DifficultyCard()) # add a difficulty card to the deck of cards

    # explored
    def __CreateStandardDeck(self):
        # solution7 - adding multi tool kit cards
        NewCard = ToolCard("P", "m")
        self.__Deck.AddCard(NewCard)
        NewCard = ToolCard("K", "m")
        self.__Deck.AddCard(NewCard)
        NewCard = ToolCard("F", "m")
        self.__Deck.AddCard(NewCard)

        for Count in range(5):
                            #( Tooltype, kit)
            # each kit will have 5 picks worth 1 point
            NewCard = ToolCard("P", "a") # object toolCard inherits abstract class card
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("P", "c")
            self.__Deck.AddCard(NewCard)
        for Count in range(3):
            # each kit will have 3 files worth 2 points
            NewCard = ToolCard("F", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("F", "c")
            self.__Deck.AddCard(NewCard)
            # each kit will have 3 keys worth 3 points
            NewCard = ToolCard("K", "a")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "b")
            self.__Deck.AddCard(NewCard)
            NewCard = ToolCard("K", "c")
            self.__Deck.AddCard(NewCard)

    def __MoveCard(self, FromCollection, ToCollection, CardNumber):
        Score = 0 # set the default card score to 0
        # if the card is being moved from the hand collection to the sequence collection
        if FromCollection.GetName() == "HAND" and ToCollection.GetName() == "SEQUENCE":
            CardToMove = FromCollection.RemoveCard(CardNumber) # return the card object and pop it from the collection
            if CardToMove is not None: # if cardToMove is not empty
                ToCollection.AddCard(CardToMove) # add the card to the new collection
                Score = CardToMove.GetScore() # update the score
        else: # does the same as above minus updating the score
            CardToMove = FromCollection.RemoveCard(CardNumber)
            if CardToMove is not None:
                ToCollection.AddCard(CardToMove)
        return Score # return the score as 0 or ...

    def ___AddGeniusCardToDeck(self): #solution10
        NewCard = GenuisCard()
        self.__Deck.AddCard(NewCard) # add the card to the deck



class Challenge():
    def __init__(self):
        self._Met = False
        self._Condition = []

    def GetMet(self):
        return self._Met

    def GetCondition(self):
        return self._Condition

    def SetMet(self, NewValue):
        self._Met = NewValue

    # assign the condition attribute with a new condition
    def SetCondition(self, NewCondition):
        self._Condition = NewCondition


class Lock():
    def __init__(self):
        self._Challenges = []
        self.__PeekUsed = False # solution2 - set PeekUsed to default False

    ### Covered
    # pass through the challenge conditions to pass the challenge
    def AddChallenge(self, Condition):
        C = Challenge() # create a challenge object
        C.SetCondition(Condition) # add the conditions to the challenge
        self._Challenges.append(C) # add the challenge object to the list of challenges

    def __ConvertConditionToString(self, C):
        ConditionAsString = "" # empty string
        for Pos in range(0, len(C) - 1): # loop through the list of conditions
            ConditionAsString += C[Pos] + ", " # append the separator
        ConditionAsString += C[len(C) - 1] # append the condition
        return ConditionAsString # return the string of conditions for the challenge

    # explored
    def GetLockDetails(self, sequence): # solution8 pass through sequence
        LockDetails = "\n" + "CURRENT LOCK" + "\n" + "------------" + "\n"
        for C in self._Challenges:
            if C.GetMet(): # if the challenge has been met
                LockDetails += "Challenge met: "# append this string
            else:  # if the challenge has NOT been met
                condition = C.GetCondition()
                if len(condition) == 3: # solution8 - handle cards
                    seqLen = sequence.GetNumberOfCards()
                    if seqLen > 0: # make sure the user has played a card before comparing
                        if (sequence.GetCardDescriptionAt(seqLen-1) == condition[0]) or (sequence.GetCardDescriptionAt(seqLen-2) == condition[0] and sequence.GetCardDescriptionAt(seqLen-1) == condition[1]):
                            LockDetails += "Challenge Partially met:"
                        else:
                            LockDetails += "Not met:"
                    else:
                        LockDetails += "Not met:"
                else:
                    LockDetails += "Not met:"
            #  append the challenge conditions
            LockDetails += self.__ConvertConditionToString(C.GetCondition()) + "\n" #
        LockDetails += "\n" # append a newline
        return LockDetails # return the string

    def GetLockSolved(self):
        # loop through every challenge in the lock
        for C in self._Challenges:
            if not C.GetMet():
                return False
        return True


    def CheckIfConditionMet(self, Sequence):
        # for every challenge in the list of challenges
        for C in self._Challenges:
            #  if the challenge has not yet been met and the sequence is the same as the conditions
            if not C.GetMet() and Sequence == self.__ConvertConditionToString(C.GetCondition()):
                C.SetMet(True) # if sequence and the conditions match set the status of the challenge as True
                return True # then return True
        return False # otherwise return false

    # index the object in the list and set the success criteria to TRue
    def SetChallengeMet(self, Pos, Value):
        self._Challenges[Pos].SetMet(Value)

    def GetChallengeMet(self, Pos):
        return self._Challenges[Pos].GetMet()

    def GetNumberOfChallenges(self):
        return len(self._Challenges)

    def GetPeekUsed(self): # solution2 Create getter for peekUsed
        return self.__PeekUsed

    def SetPeekUsed(self): # solution2 Create setter for peekUsed
        self.__PeekUsed = True


class Card():

    _NextCardNumber = 0 # class variable

    def __init__(self):
        self._CardNumber = Card._NextCardNumber # set the card increment by 1
        Card._NextCardNumber += 1 # increment by 1
        self._Score = 0 # set default card score to zero

    def GetScore(self):
        return self._Score # return score to the calling code

    # override this sub in subclasses
    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        pass # potential problem to be solved

    def GetCardNumber(self):
        return self._CardNumber # return the card number

    def GetDescription(self):
        if self._CardNumber < 10: #  if the card num < 10
            return " " + str(self._CardNumber) # add a space and return the card number
        else:
            return str(self._CardNumber) # otherwise return the card number


class ToolCard(Card):
    def __init__(self, *args):
        self._ToolType = args[0] # tool type
        self._Kit = args[1] # kit
        if len(args) == 2: # starting a new game
            super(ToolCard, self).__init__() # use the parent class constructor
        elif len(args) == 3: # loading a game
            self._CardNumber = args[2] # assign the card number
        self.__SetScore()

    # explored
    def __SetScore(self):
        if self._ToolType == "K": # key tool
            self._Score = 3
        elif self._ToolType == "F": # file tool
            self._Score = 2
        elif self._ToolType == "P": # pick tool
            self._Score = 1
    # return the card description i.e. P a or K b
    def GetDescription(self):
        return self._ToolType + " " + self._Kit

    # solution7
    def SetCardToolKit(self,kit):
        self._Kit = kit


class DifficultyCard(Card): # inherits the card class
    # constructor
    def __init__(self, *args): # *args passing a list of arguments
        self._CardType = "Dif" # set the card type to a diff card
        if len(args) == 0: # if nothing is passed
            super(DifficultyCard, self).__init__() # use the parent class to generate a card number
        elif len(args) == 1:
            self._CardNumber = args[0] # if a diff card is loaded from a text file assign the card's number here

    def GetDescription(self):
        return self._CardType

    # over sub
    # when the user recieves the difficulty card they are asked if they would to discard a key or 5 cards from the deck
    # choice must be 1 to 5 or D
    def Process(self, Deck, Discard, Hand, Sequence, CurrentLock, Choice, CardChoice):
        ChoiceAsInteger = None
        try:
            ChoiceAsInteger = int(Choice) # convert the choice to an integer if the user hasn't select D
        except:
            pass
        if ChoiceAsInteger is not None: # if the user has select an option between 1 and 5
            if ChoiceAsInteger >= 1 and ChoiceAsInteger <= 5: # validate user choice
                if ChoiceAsInteger >= CardChoice: # handle for list
                    ChoiceAsInteger -= 1
                if ChoiceAsInteger > 0:
                    ChoiceAsInteger -= 1
                if Hand.GetCardDescriptionAt(ChoiceAsInteger)[0] == "K": # check that it is a key
                    CardToMove = Hand.RemoveCard(Hand.GetCardNumberAt(ChoiceAsInteger))
                    Discard.AddCard(CardToMove)
                    return # break out of the sub
        Count = 0
        # remove 5 cards from the deck
        while Count < 5 and Deck.GetNumberOfCards() > 0:
            CardToMove = Deck.RemoveCard(Deck.GetCardNumberAt(0))
            Discard.AddCard(CardToMove)
            Count += 1


class CardCollection():
    def __init__(self, N):
        self._Name = N
        self._Cards = []

        # soultion6 - add new attributes to calculate the stats for tools cards
        self.__NumPicks = 0
        self.__NumFiles = 0
        self.__NumKeys = 0
        self.__NumDiff = 0

    def GetName(self):
        return self._Name

    def GetCardNumberAt(self, X):
        return self._Cards[X].GetCardNumber()

    def GetCardDescriptionAt(self, X):
        return self._Cards[X].GetDescription()

    def AddCard(self, C):

        # solution 6 track the type of card generated
        if C.GetDescription()[0] == "F":
            self.__NumFiles +=1
        if C.GetDescription()[0] == "K":
            self.__NumKeys += 1
        if C.GetDescription()[0] == "P":
            self.__NumPicks += 1
        if C.GetDescription() == "Dif":
            self.__NumDiff += 1
        self._Cards.append(C) # add the object to the card collection

    def GetNumberOfCards(self):
        return len(self._Cards)

    # explored
    def Shuffle(self):
        for Count in range(10000): # loop 10,000 times
            RNo1 = random.randint(0, len(self._Cards) - 1) # select a random int
            RNo2 = random.randint(0, len(self._Cards) - 1) # select a random int
            TempCard = self._Cards[RNo1] # store one card in a temp variable
            # swap the cards around
            self._Cards[RNo1] = self._Cards[RNo2]
            self._Cards[RNo2] = TempCard

    def RemoveCard(self, CardNumber): # pass card number
        CardFound = False
        Pos = 0
        # ensure the loop doesn't pass the upperbound and end once the card found = true
        while Pos < len(self._Cards) and not CardFound:
            if self._Cards[Pos].GetCardNumber() == CardNumber: # if we've found the card
                CardToGet = self._Cards[Pos] # assign the card object
                CardFound = True # break the loop
                self._Cards.pop(Pos) # remove the object from this list


                # solution6 - remove the card from the counter
                if CardToGet.GetDescription()[0] == "F":
                    self.__NumFiles -=1
                if CardToGet.GetDescription()[0] == "K":
                    self.__NumKeys -=1
                if CardToGet.GetDescription()[0] == "P":
                    self.__NumPicks -=1
                if CardToGet.GetDescription() == "Dif":
                    self.__NumDiff -=1

            Pos += 1  # increment by one


        return CardToGet # return the object

    # create a line of dashes
    def __CreateLineOfDashes(self, Size):
        LineOfDashes = ""
        for Count in range(Size):
            LineOfDashes += "------"
        return LineOfDashes

    def GetCardDisplay(self):
        # append the title of the collection ie. deck, sequence, hand, discard
        CardDisplay = "\n" + self._Name + ":" # append the colon

        # if there are no cards in the colection print empty \n * 2
        if len(self._Cards) == 0:
            return CardDisplay + " empty" + "\n" + "\n"
        else: # otherwise
            CardDisplay += "\n" + "\n" # append\n * 2

        LineOfDashes = "" # empty string
        CARDS_PER_LINE = 10 # set to 10
        # if there are more than 10 cards
        if len(self._Cards) > CARDS_PER_LINE: # pass 10 and create dashes for up to 10 cards
            LineOfDashes = self.__CreateLineOfDashes(CARDS_PER_LINE)
        else: # otherwise create the line of dashes for the length of the cards
            LineOfDashes = self.__CreateLineOfDashes(len(self._Cards))
        CardDisplay += LineOfDashes + "\n" # add a new line
        Complete = False # set completion to false
        Pos = 0 # set pos to 0
        while not Complete:
            # append the vertical slash and get the card description at position
            CardDisplay += "| " + self._Cards[Pos].GetDescription() + " "
            Pos += 1 # incement by 1
            ## ??
            if Pos % CARDS_PER_LINE == 0:
                # append a separator between the conditions
                CardDisplay += "|" + "\n" + LineOfDashes + "\n"

            # if have processed all cards
            if Pos == len(self._Cards):
                Complete = True

        # if at the end of the cards  close the string with a vertical slash
        if len(self._Cards) % CARDS_PER_LINE > 0:
            CardDisplay += "|" + "\n"
            if len(self._Cards) > CARDS_PER_LINE:
                LineOfDashes = self.__CreateLineOfDashes(len(self._Cards) % CARDS_PER_LINE)
            CardDisplay += LineOfDashes + "\n" # append the lines and a newline
        return CardDisplay # return the string to be printed

    def DisplayStats(self):
        # solution6 - Calculate chance
        keyPercentage = self.__NumKeys / self.GetNumberOfCards() * 100
        PickPercentage = self.__NumPicks / self.GetNumberOfCards() * 100
        FilePercentage = self.__NumFiles / self.GetNumberOfCards() * 100
        DiffPercentage = self.__NumDiff / self.GetNumberOfCards() * 100
        # print probabilty to the user
        print(f"There is a {round(keyPercentage)}% chance that the next card will be a Key")
        print(f"There is a {round(PickPercentage)}% chance that the next card will be a Pick")
        print(f"There is a {round(FilePercentage)}% chance that the next card will be a File")
        print(f"There is a {round(DiffPercentage)}% chance that the next card will be a Diff")

    def SetCardToolKit(self,pos,kit):
        self._Cards[pos].SetCardToolKit(kit)

class GenuisCard(Card): # solution10
    def __init__(self):
        self._CardType = "Gen" # set attribute card type
        super().__init__() # initalise parent class constuctor

    def GetDescription(self):
        return self._CardType

    def Process(self, CurrentLock, Choice, numChal): # solution10
        ChoiceAsInteger = None
        try:
            ChoiceAsInteger = int(Choice) # convert the choice to an integer if the user hasn't select D
        except:
            pass
        if ChoiceAsInteger is not None: # if the user has select an option between 1 and 5
            if ChoiceAsInteger >= 1 and ChoiceAsInteger <= numChal: # validate user choice
                ChoiceAsInteger -= 1 # convert to an index
                CurrentLock.SetChallengeMet(ChoiceAsInteger,True)





if __name__ == "__main__":
    Main()