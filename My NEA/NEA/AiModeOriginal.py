from ticTacBoard import gameBoard, gameStatus, symbol
from p5 import *
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
            #makes the users move
            ticTacBoard.humanPlayerMove(mouse_x, mouse_y)


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


run()

