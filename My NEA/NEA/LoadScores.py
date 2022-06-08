from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class scoreWindow(QMainWindow):
    def __init__(self, details):
        super().__init__()  # inheriting the QMain Window
        # resizes the window (X and Y)
        self.resize(400, 400)
        # sets a title to the form
        self.setWindowTitle("Load Scores")
        self.userDetails = details
        self.username, _, self.win, self.loss, self.draw = self.userDetails
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
        self.label_title.setFont(QFont("Arial", 20, 70, True))
        # adjusts the size of text according to length of text
        self.label_title.adjustSize()
        # sets the unique identifier for the title
        self.label_title.setObjectName("Title Label")
        # sets the X and Y coordinates of the title
        self.label_title.move(100, 10)

        ##Sub title label (same comments as above)
        self.label_registration = QLabel(self)
        self.label_registration.setText("Player's Scores")
        self.label_registration.setFont(QFont("Arial", 11, 81, True))
        self.label_registration.adjustSize()
        self.label_registration.setObjectName("SubTitle Label")
        self.label_registration.move(140, 60)

        ###Username Label
        # same process as above label
        self.label_username = QLabel(self)
        self.label_username.setText(self.username)
        self.label_username.setFont(QFont("Arial", 24, 50, False))
        self.label_username.adjustSize()
        self.label_username.setObjectName("label_form_username")
        self.label_username.move(100, 90)
        self.label_username.setStyleSheet("color: blue")

        ###wins label
        # same process as login label
        self.label_wins = QLabel(self)
        self.label_wins.setText("Wins:" + str(self.win))
        self.label_wins.setFont(QFont("Ariel", 16, 65, False))
        self.label_wins.adjustSize()
        self.label_wins.setObjectName("label_form_wins")
        self.label_wins.move(20, 180)
        self.label_wins.setStyleSheet("color: green")

        ###draw label
        # same process as login label
        self.label_draw = QLabel(self)
        self.label_draw.setText("Draws:" + str(self.draw))
        self.label_draw.setFont(QFont("Ariel", 16, 65, False))
        self.label_draw.adjustSize()
        self.label_draw.setObjectName("label_form_draw")
        self.label_draw.move(20, 270)
        #self.label_draw.setStyleSheet("color: green")

        ###loss label
        # same process as login label
        self.label_loss = QLabel(self)
        self.label_loss.setText("loss:" + str(self.loss))
        self.label_loss.setFont(QFont("Ariel", 16, 65, False))
        self.label_loss.adjustSize()
        self.label_loss.setObjectName("label_form_loss")
        self.label_loss.move(20, 360)
        self.label_loss.setStyleSheet("color: red")

        ##Back to login button
        self.Button_Back = QPushButton(self)
        self.Button_Back.setGeometry(QRect(295, 415, 200, 80))
        font = QFont()
        font.setPointSize(10)
        self.Button_Back.setFont(font)
        self.Button_Back.setText("Back to menu")
        self.Button_Back.setObjectName("BackButton")
        self.Button_Back.clicked.connect(self.BackToLogin)
        self.hide()

    def BackToLogin(self):
        self.hide()






if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # converts code into correct format
    window = scoreWindow(["Javed1234","password","2","1","3"])  # instantiates window class
    window.show()  # shows all the widgets
    app.exec()  # executes the code