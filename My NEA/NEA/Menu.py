from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from TwoPlayergame import gameWindow
from LoadScores import scoreWindow

class mainMenu(QMainWindow):
    def __init__(self, details):
        super().__init__()  # inheriting the QMain Window
        # resizes the window (X and Y)
        self.resize(400, 400)
        # sets a title to the form
        self.setWindowTitle("Main Menu")
        #assigns the list of user details passes as an argument to a variable (tuple)
        self.userDetails = details
        self.TwoPlayerWindow = gameWindow(self.userDetails)
        self.scores = scoreWindow(self.userDetails)
        self.setStyleSheet(
            """QMainWindow{
            background-color:#13A6EA
            }
            """
        )


        ## Creats the Title Label
        self.label_title = QLabel(self)
        # sets the text for the Title
        self.label_title.setText("Tic-Tac-Toe")
        # sets the font, size, how bold and if italics
        self.label_title.setFont(QFont("Arial", 25, 70, True))
        # adjusts the size of text according to length of text
        self.label_title.adjustSize()
        # sets the unique identifier for the title
        self.label_title.setObjectName("Registration Title Label")
        # sets the X and Y coordinates of the title
        self.label_title.move(100, 10)

        ##Sub title label (same comments as above)
        self.label_registration = QLabel(self)
        self.label_registration.setText("Main Menu")
        self.label_registration.setFont(QFont("Arial", 17, 81, False))
        self.label_registration.adjustSize()
        self.label_registration.setObjectName("Register Title Label")
        self.label_registration.move(130, 50)

        #two player mode button
        self.TwoPlayerButton = QPushButton(self)
        self.TwoPlayerButton.setGeometry(QRect(40, 110, 300, 50))
        font = QFont()
        font.setPointSize(10)
        self.TwoPlayerButton.setFont(font)
        self.TwoPlayerButton.setText("2 Player Mode")
        self.TwoPlayerButton.setObjectName("2 Player mode")
        #connects to the 2 player mode subroutine
        self.TwoPlayerButton.clicked.connect(self.TwoPlayerMode)
        self.TwoPlayerButton.setStyleSheet("color:blue")

        #creates the AI mode button
        self.AI_Mode = QPushButton(self)
        self.AI_Mode.setGeometry(QRect(40, 200, 400, 70))
        font = QFont()
        font.setPointSize(10)
        self.AI_Mode.setFont(font)
        self.AI_Mode.setText("AI Mode")
        self.AI_Mode.setObjectName("AiButton")
        #connects to the AiMode subroutine
        self.AI_Mode.clicked.connect(self.AiMode)
        self.AI_Mode.setStyleSheet("color:blue")

        #creates the load score button
        self.LoadScoresButton = QPushButton(self)
        self.LoadScoresButton.setGeometry(QRect(40, 290, 400, 70))
        font = QFont()
        font.setPointSize(10)
        self.LoadScoresButton.setFont(font)
        self.LoadScoresButton.setText("Load Scores")
        self.LoadScoresButton.setObjectName("Load Scores")
        #connect to the Loadscore sub
        self.LoadScoresButton.clicked.connect(self.LoadScores)
        self.LoadScoresButton.setStyleSheet("color:blue")
        self.hide()

    #subroutine to show the twoplayermode button
    def TwoPlayerMode(self):
        try:

            self.TwoPlayerWindow.show()
        except Exception as e:
            print(e)

    #subroutine to start the Aimode
    def AiMode(self):
        self.hide()
        execute()

    #subroutine to show the Loadscore window
    def LoadScores(self):
        try:

            self.scores.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # converts code into correct format
    window = mainMenu(["Javed1234","password","2","1","3"])  # instantiates window class
    window.show()  # shows all the widgets
    app.exec()  # executes the code

from ticTacBoard import gameBoard, gameStatus, symbol
from p5 import *
import time
import math

# this variable will be an instance of the gameBoard class and will act as the board for the game
ticTacBoard = None
# sets the width and height of the window
windowSize = 400
active = False
# sets what symbol the human player will be
humanPlayer = symbol.X
# sets the human player as the opposite of  the human player
if humanPlayer == symbol.O:
    aiPlayer = symbol.X
else:
    aiPlayer = symbol.O


# subroutine to set up the board
def setup():
    # sets tictacBoard as a global variable so that it can be accessed in other subs
    global ticTacBoard
    # resises the sketch window (length, height)
    size(windowSize, windowSize)
    # instantaites the gameboard
    ticTacBoard = gameBoard(windowSize)


# sub that draws the board
def draw():
    # sets the colour off the background of the P5 interface
    background(13, 166, 234)
    # draw the board
    ticTacBoard.draw()
    # if the game is not ongoing then exit the sub
    if ticTacBoard.getGameState() is not gameStatus.ONGOING:
        return
    # if the current turn is the AI player then apply minimax
    if (ticTacBoard.getCurrentTurn() is aiPlayer):
        # sets the best score to negative infinity and the best move to none
        bestScore = -math.inf
        bestMove = None
        # loops through every possible move that can be made
        for move in ticTacBoard.getPossibleMoves():
            # makes the move
            ticTacBoard.makeMove(move)
            # sets the score as what is returned from the minimax algorithm
            score = minimax(False, aiPlayer, ticTacBoard)
            # undoes the new move so we can do all the rest of the moves
            ticTacBoard.undo()
            # if the score for the current move is greater than the previous best score
            if (score > bestScore):
                # sets the new best move and score as what is currently being tested
                bestScore = score
                bestMove = move
        # once we have looped through all of the possible moves and found the best move

        ticTacBoard.makeMove(bestMove)

    else:
        if mouse_is_pressed:
            ticTacBoard.UiMove(mouse_x, mouse_y)



# subroutine that carries out the minimax algorithm
def minimax(isMaxTurn, maximizerMark, board):
    #gets the current state of the game
    gameStatus = board.getGameState()
    #if the game is a draw return a value of 0
    if gameStatus is gameStatus.DRAW:
        return 0
    elif (gameStatus is gameStatus.OVER):
        #returns a value of 1 for a win and -1 for a loss
        return 1 if board.getWinner() is maximizerMark else -1
    #create a list of scores
    scores = []
    #loops throigh all possible moves
    for move in board.getPossibleMoves():
        #carries out the moved
        board.makeMove(move)
        #appends the result of the minimax to the score
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        #undoes the move so it doesnt affect teh rest of th egame
        board.undo()
        #if the maximisin player reaxches the maximum score or vice versa for the minimiser then
        if (isMaxTurn and max(scores) == 1) or (not isMaxTurn and min(scores) == -1):
            #exit the loop
            break
    #returns the maximising score or the minimum score for the minimiser
    return max(scores) if isMaxTurn else min(scores)

def execute():
    run()

if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # converts code into correct format
    window = mainMenu(["javed","ff",0,3,5])  # instantiates window class
    window.show()  # shows all the widgets
    app.exec()  # executes the code