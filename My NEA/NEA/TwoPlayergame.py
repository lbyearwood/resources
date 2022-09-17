from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from TwoPlayerBot import secondPlayer
import mysql.connector

class gameWindow(QMainWindow):
    def __init__(self, userDetails):
        #inherits the PYQT5 class
        super().__init__()
        #instantiates the second player class
        self.secondPlayer = secondPlayer()
        self.userDetails = userDetails
        #sets the window size
        self.resize(500, 500)
        #sets the window title
        self.setWindowTitle("Tic-Tac-Toe: 2 Player")
        #sets the symbol as O who is the first Player
        self.symbol = "O"
        #vairable that states the game is active
        self.activeGame = True
        #creats a list of buttons
        self.buttons = []
        #sets an X cordinate variable
        self.x = 120
        #sets a Y co ordinate variable
        self.y = 100
        #sets the button size as a variabke
        self.buttonSize = 80
        self.PlayerGameStatus = None
        #sets the background color
        self.setStyleSheet(
            """QMainWindow{
            background-color:#13A6EA
            }
            """
        )
        #label that says if a button has already been pressed
        self.alreadyPressedLabel = QLabel(self)
        self.alreadyPressedLabel.setText("Space Already Taken")
        self.alreadyPressedLabel.setFont(QFont("Ariel", 14, 60, False))
        self.alreadyPressedLabel.adjustSize()
        self.alreadyPressedLabel.setObjectName("label_form_password")
        self.alreadyPressedLabel.move(30, 30)
        self.alreadyPressedLabel.setHidden(True)
        #Label for when player O has won
        self.OwinnerLabel = QLabel(self)
        self.OwinnerLabel.setText("Player O has won!!")
        self.OwinnerLabel.setFont(QFont("Ariel", 36, 60, False))
        self.OwinnerLabel.adjustSize()
        self.OwinnerLabel.setObjectName("label_form_Owin")
        self.OwinnerLabel.move(50, 30)
        self.OwinnerLabel.setHidden(True)
        #label for when Player X wins
        self.XwinnerLabel = QLabel(self)
        self.XwinnerLabel.setText("Player X has won!!")
        self.XwinnerLabel.setFont(QFont("Ariel", 36, 60, False))
        self.XwinnerLabel.adjustSize()
        self.XwinnerLabel.setObjectName("label_form_Xwin")
        self.XwinnerLabel.move(50, 30)
        self.XwinnerLabel.setHidden(True)
        #label for when X wins
        self.drawLabel = QLabel(self)
        self.drawLabel.setText("Its a draw!!")
        self.drawLabel.setFont(QFont("Ariel", 36, 60, False))
        self.drawLabel.adjustSize()
        self.drawLabel.setObjectName("label_form_Draw")
        self.drawLabel.move(125, 30)
        self.drawLabel.setHidden(True)
        #label that states the current player
        self.currentPlayerLabel = QLabel(self)
        self.currentPlayerLabel.setText("Current Player:O")
        self.currentPlayerLabel.setFont(QFont("Ariel", 32, 60, False))
        self.currentPlayerLabel.adjustSize()
        self.currentPlayerLabel.setObjectName("label_form_CurrentPlayer")
        self.currentPlayerLabel.move(80, 400)
        #for loop that creats the 9 buttons for the grid
        for i in range(1, 10):
            #creats the button
            self.NodeButton = QPushButton(self)
            #sets the geometry of the button with the pre defined variables
            self.NodeButton.setGeometry(QRect(self.x, self.y, self.buttonSize, self.buttonSize))
            #sets the font and text size
            self.NodeButton.setFont(QFont("Ariel", 12, 70, False))
            #sets the object name as the number of the button
            self.NodeButton.setObjectName(f'{i}')
            #sets the color and border style
            self.NodeButton.setStyleSheet("""background-color:#15E9EC;
            border-style: solid""")
            #when clicked connect to the sub routine
            self.NodeButton.clicked.connect(self.buttonClicked)
            #adds to the button list
            self.buttons.append(self.NodeButton)
            #if the button is the 3rd button or 6th (end of the row) then move y down by 90 ansd set x back to the start
            if i == 3 or i == 6:
                self.x = 120
                self.y = self.y + 90
            #else move the button along by 90
            else:
                self.x += 90
        self.currentPlayerHuman = True

        newGame = QAction("&New",self)
        newGame.triggered.connect(self.newGame)
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QMenu("&Main Menu", self)
        fileMenu.addAction(newGame)
        menuBar.addMenu(fileMenu)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Restart")
        helpMenu = menuBar.addMenu("&Quit")

        self.hide()


    def newGame(self):
        for i in range (1,10):
            self.secondPlayer.Dictionary[i] = ""



    #sub routine for when the button is clicked
    def buttonClicked(self):
        #if the game is still running
        if self.activeGame == True:
            #gets the name of the button clicked
            sender = self.sender()
            name = int(sender.objectName())
            validMove = self.secondPlayer.updateDictionary(name, self.symbol)
            if validMove:
                self.alreadyPressedLabel.setHidden(True)
                if self.currentPlayerHuman:
                    sender.setFont(QFont("Ariel",64,64,False))
                    sender.setText("O")
                    self.currentPlayerHuman = False
                    self.symbol = "X"
                else:
                    sender.setFont(QFont("Ariel", 64, 64, False))
                    sender.setText("X")
                    self.currentPlayerHuman = True
                    self.symbol = "O"
            else:
                self.alreadyPressedLabel.setHidden(False)
            winner = self.secondPlayer.checkWinAndDraw()
            if self.currentPlayerHuman:
                self.symbol = "O"
                self.currentPlayerLabel.setText("Current Player:O")
                self.currentPlayerLabel.repaint()

            else:
                self.symbol = "X"
                self.currentPlayerLabel.setText("Current Player:X")
                self.currentPlayerLabel.repaint()

            if winner == "O":
                self.PlayerGameStatus = "win"

                self.OwinnerLabel.setHidden(False)
                self.activeGame = False
                self.currentPlayerLabel.setText("Game ended")
                self.currentPlayerLabel.repaint()
                self.addScoreDatabase()

            if winner == "X":
                self.PlayerGameStatus = "loss"

                self.XwinnerLabel.setHidden(False)
                self.activeGame = False
                self.currentPlayerLabel.setText("Game ended")
                self.currentPlayerLabel.repaint()
                self.addScoreDatabase()
            if winner == "draw":
                self.PlayerGameStatus = "draw"

                self.drawLabel.setHidden(False)
                self.activeGame = False
                self.currentPlayerLabel.setText("Game ended")
                self.currentPlayerLabel.repaint()
                self.addScoreDatabase()
        else:
            pass

    def connect_database(self):
        try:
            db = mysql.connector.connect(
                host='10.170.140.46',
                user='javed',
                port='3306',
                password='javed1234',
                database="tic_db",
                auth_plugin="mysql_native_password"
            )
            return db
        except Exception as e:
            print(e)
            exit()

    def addScoreDatabase(self):
        username,_,win,draw,loss = self.userDetails
        print("Adding to Database")
        database = self.connect_database()
        try:
            sql = ""
            if self.PlayerGameStatus == "win":
                win = int(win) + 1
                sql = f"""
        UPDATE tic_db.user
                    SET win = {win}
                    WHERE username = '{username}'
    """
            elif self.PlayerGameStatus == "loss":
                loss = int(loss) + 1
                sql = f"""
        UPDATE tic_db.user
                    SET loss = {loss}
                    WHERE username = '{username}'
    """
            elif self.PlayerGameStatus == "draw":
                draw = int(draw) + 1
                sql = f"""
                    UPDATE tic_db.user
                    SET draw = {draw}
                    WHERE username = '{username}'
                """
            myCursor = database.cursor()
            myCursor.execute(sql)
        except Exception as e:
            print(e)














if __name__ == "__main__":  # if this is the main module then run the following code
    try:
        app = QApplication(sys.argv)  # converts code into correct format
        window = gameWindow("s")  # instantiates window class
        window.show()  # shows all the widgets
        app.exec()
    except Exception as e:
        print(e)
