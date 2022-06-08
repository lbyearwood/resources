from enum import Enum
from p5 import *

# this is the font that will be used for the text going forward
FONT = create_font("fonts/SigmarOne-Regular.ttf", 0)


# class used to represent the symbols using numeric values
class symbol(Enum):
    X = 2
    O = 4
    EMPTY = 8


# class used to represent the states of the game as numeric values
class gameStatus(Enum):
    DRAW = 1
    ONGOING = 2
    OVER = 3


class gameBoard:
    def __init__(self, size):
        self.size = size  # sets the size of the board which is passed as an argument
        self.gridSquareSize = size / 3  # size of each squeare in the grid is a third of the entire board
        # creates a 3d list of values for the game and sets each value as empty using the symbol class
        self.boardItems = [[symbol.EMPTY.value for x in range(3)] for y in range(3)]
        self.currentTurn = symbol.X  # current player is X
        self.symbolSize = int(self.gridSquareSize / 2)  # size of the symbols are set to half the size of the grid
        self.winningSymbolsCoordinate = []  # new list of winning symbols
        self.status = gameStatus.ONGOING  # sets the state of the game as ongoing
        self.winner = None  # current winner set as no one
        self.moves = []  # list that stores all the moves

    # sub routine that draws the board
    def draw(self):
        self.drawGrid()
        self.drawGameState()

    # returns whose turn it is currently
    def getCurrentTurn(self):
        return self.currentTurn

    # returns the current state of the game
    def getGameState(self):
        return self.status

    # returns the winner of the game
    def getWinner(self):
        return self.winner

    # returns the game dictionary
    def getBoardItems(self):
        return self.boardItems

    # returns all the possible moves
    def getPossibleMoves(self):
        possibleMoves = []
        # loops through the dictionary
        for x in range(0, 3):
            for y in range(0, 3):
                # if the node is empty then add to the list of empty moves
                if self.boardItems[x][y] is symbol.EMPTY.value:
                    possibleMoves.append((x, y))
        return possibleMoves

    # draws the background of the board
    def drawGrid(self):
        # sets the width of the stroke for lines and is measured by numbers of pixels
        stroke_weight(5)
        # sets the colour as an RGB
        stroke(18, 245, 245)
        # draws the 4 lines to make the grid
        # draws a line from 2 point (X-coordinate of start point, Y co ordinate of start,X of end, Y of end)
        line(self.gridSquareSize, 0, self.gridSquareSize, self.size)
        line(self.gridSquareSize * 2, 0, self.gridSquareSize * 2, self.size)
        line(0, self.gridSquareSize, self.size, self.gridSquareSize)
        line(0, self.gridSquareSize * 2, self.size, self.gridSquareSize * 2)

    # draws the symbols in the grid
    def drawGameState(self):
        # loops through the dictionary
        for x in range(3):

            for y in range(3):
                # sets the state to whatever the symbol is at that Position in the list
                state = symbol(self.boardItems[x][y])
                # if the current state is not an empty position
                if state is not symbol.EMPTY:
                    # sets the font of the text
                    text_font(FONT)
                    # sets the size of the text
                    text_size(self.symbolSize)
                    # if that symbol is one of the winning symbols then change its colour
                    if (x, y) in self.winningSymbolsCoordinate:
                        fill(18, 245, 63)
                    # else set to the default colour
                    elif self.status == gameStatus.DRAW:
                        fill(0,255,0)
                    else:
                        fill(255)

                    text(state.name, (self.gridSquareSize * x + self.gridSquareSize / 2 - self.symbolSize / 2,
                                      self.gridSquareSize * y + self.gridSquareSize / 2 - self.symbolSize))

    # sub routine to handle the User's move
    def humanPlayerMove(self, mouse_x, mouse_y):
        # if the game is over then no need for the UI to make a move so exit the sub
        if self.status is gameStatus.OVER:
            return
        # The X coordinate is set as he mouseclick location dvidied by the size of the squere
        x = int(mouse_x / self.gridSquareSize)
        # same for the Y co-ordinate
        y = int(mouse_y / self.gridSquareSize)
        # makes a move at said co-ordinate
        self.makeMove((x, y))

    # sub to make the players move
    # passes a list of co-ordinates as the argument
    def makeMove(self, coordinates):
        x = coordinates[0]  # sets the x co-ordinate
        y = coordinates[1]  # sets the y co-ordinate
        if (self.boardItems[x][y] == symbol.EMPTY.value):  # checks that that node is empty else do nothing
            self.boardItems[x][y] = self.currentTurn.value  # sets the list value to the symbol of the current player
            # switch current player
            self.switchTurn()
            # updates the state of the board
            self.evaluateBoardStatus()
            # adds the coordinates to the list of moves made
            self.moves.append(coordinates)

    # undoes the last move
    def undo(self):
        # removes the last move from the list of moves made
        lastMove = self.moves.pop()
        if lastMove:
            # sets the value of the last move as empty in he board list
            self.boardItems[lastMove[0]][lastMove[1]] = symbol.EMPTY.value
            # switches players
            self.switchTurn()
            # updates the board
            self.evaluateBoardStatus()

    def evaluateBoardStatus(self):
        # evaluates the state of the board and returns a win or draw and the symbol that has won
        board_eval = self.checkWin()
        # the current state of the board is set
        self.status = board_eval[0]
        self.winningSymbolsCoordinate = []
        self.winner = None
        # if the state of the game is over (someone has won)
        if (self.status is gameStatus.OVER):
            # the winning co ordinates are stored in a list
            self.winningSymbolsCoordinate = board_eval[2:]
            # the winning symbol is set as a variable
            self.winner = board_eval[1]

    def switchTurn(self):
        self.currentTurn = symbol.X if self.currentTurn is symbol.O else symbol.O

    # checks for a win and draw and returns
    # (state of game, current symbol, winning coordinate 1, co ordinate 2, co ordinate 3)
    def checkWin(self):
        draw = True
        for x in range(3):
            for y in range(3):
                currentPlayerSymbol = symbol(self.boardItems[x][y])
                if currentPlayerSymbol is symbol.EMPTY:
                    draw = False
                    continue
                else:
                    # checks for horizontal wins
                    try:
                        if (currentPlayerSymbol.value | self.boardItems[x + 1][y] | self.boardItems[x + 2][
                            y]) == currentPlayerSymbol.value:
                            return (gameStatus.OVER, currentPlayerSymbol, (x, y), (x + 1, y), (x + 2, y))
                    except:
                        pass

                    # checls for vertical win
                    try:
                        if (currentPlayerSymbol.value | self.boardItems[x][y + 1] | self.boardItems[x][
                            y + 2]) == currentPlayerSymbol.value:
                            return (gameStatus.OVER, currentPlayerSymbol, (x, y), (x, y + 1), (x, y + 2))
                    except:
                        pass

                    # checls for diagonal wins
                    if x == 0 and y == 0 and (
                            currentPlayerSymbol.value | self.boardItems[x + 1][y + 1] | self.boardItems[x + 2][
                        y + 2] == currentPlayerSymbol.value):
                        return (gameStatus.OVER, currentPlayerSymbol, (x, y), (x + 1, y + 1), (x + 2, y + 2))
                    elif x == 0 and y == 2 and (
                            currentPlayerSymbol.value | self.boardItems[x + 1][y - 1] | self.boardItems[x + 2][
                        y - 2] == currentPlayerSymbol.value):
                        return (gameStatus.OVER, currentPlayerSymbol, (x, y), (x + 1, y - 1), (x + 2, y - 2))
                # returns a draw or ongoign if the game hasnt finished yet
        return [gameStatus.DRAW if draw else gameStatus.ONGOING]