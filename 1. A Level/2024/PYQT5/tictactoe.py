from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class tictactoe(QMainWindow):  # inherit the parent class
    def __init__(self):  # define the child class constructor
        super().__init__()  # make use of the parent class constructor
        formWidth = 300
        formHeight = 350

        self.setFixedSize(formWidth, formHeight)
        self.setAutoFillBackground(True)
        self.setWindowTitle("Tic Tac Toe")
        self.setObjectName("tictactoe")
        # Menu form title
        self.label = QLabel(self)
        self.label.setText("Tic Tac Toe")
        self.label.setFont(QFont("Arial",24,87,False))
        self.label.adjustSize() # auto resize the label
        self.label.setObjectName("formTitle")
        self.label.move(100,30) # X, Y
        cell = 60
        x = 30
        y = 100

        # submit button
        for i in range(9):
            self.cell = QPushButton(self)
            self.cell.setText('')
            self.cell.setGeometry(QRect(x, y, cell, cell))  # (x,y,w,h)
            x = x + 80
            if i % 4 == 0:
                x = 30
                y = y + 80

            self.cell.setObjectName(f"cell{i}")
            font = QFont()
            font.setPointSize(16)
            font.setBold(True)
            self.cell.setFont(font)
            self.cell.clicked.connect(self.buttonEventHandler)
        self.setStyleSheet("""
            QLabel {
                color:#ffffff;
            }
            QMainWindow {
                background-color:#000000;
            }
            #errorMessage {
                color:#ff0000;
            }
        """)

    def buttonEventHandler(self):
            ...

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = tictactoe()  # create an instance (an object) of the class
        window.show()
        app.exec()
    except Exception as e:
        print(e)