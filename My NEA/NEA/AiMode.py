from ticTacBoard import TicTacBoard, State, symbol
from p5 import *
import math


class AiBot():
    def __init__(self):
        self.ticTacBoard = None
        self.SIZE = 300
        self.playAs = symbol.X
        self.aiPlayer = symbol.X if self.playAs is symbol.O else symbol.O


    # def to set up the board
    def setup(self):
        size(300, 300)
        self.ticTacBoard = TicTacBoard(self.SIZE)


    # sub that draws the board
    def draw(self):
        # sets the colour off the background of the P5 interface
        background(13, 166, 234)
        # draw the board
        self.ticTacBoard.draw()
        # if the game is not ongoing then exit the sub
        if self.ticTacBoard.get_state() is not State.ONGOING:
            return
        # if the current turn is the AI player then apply minimax
        if (self.ticTacBoard.get_turn_to_play() is self.aiPlayer):
            # sets the best score to negative infinity and the best move to none
            bestScore = -math.inf
            bestMove = None
            # loops through every possible move that can be made
            for move in self.ticTacBoard.get_possible_moves():
                # makes the move
                self.ticTacBoard.make_move(move)
                # sets the score as what is returned from the minimax algorithm
                score = self.minimax(False, self.aiPlayer, self.ticTacBoard)
                # undoes the new move so we can do all the rest of the moves
                self.ticTacBoard.undo()
                # if the score for the current move is greater than the previous best score
                if (score > bestScore):
                    # sets the new best move and score as what is currently being tested
                    bestScore = score
                    bestMove = move
            #once we have looped through all of the possible moves and found the best move
            self.ticTacBoard.make_move(bestMove)
        else:
            if mouse_is_pressed:
                self.ticTacBoard.make_ui_move(mouse_x, mouse_y)


    def minimax(self, isMaxTurn, maximizerMark, board):
        state = board.get_state()
        if (state is State.DRAW):
            return 0
        elif (state is State.OVER):
            return 1 if board.get_winner() is maximizerMark else -1

        scores = []
        for move in board.get_possible_moves():
            board.make_move(move)
            scores.append(self.minimax(not isMaxTurn, maximizerMark, board))
            board.undo()
            if (isMaxTurn and max(scores) == 1) or (not isMaxTurn and min(scores) == -1):
                break

        return max(scores) if isMaxTurn else min(scores)

    def execute(self):
        self.setup()
        self.draw()

        run()



if __name__ == "__main__":
    x = AiBot()
    x.execute()


