from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class menuForm(QMainWindow):  # inherit the parent class
    def __init__(self):  # define the child class constructor
        super().__init__()  # make use of the parent class constructor
        formWidth = 300
        formHeight = 350

        self.setFixedSize(formWidth, formHeight)
        self.setAutoFillBackground(True)
        self.setWindowTitle("Menu")
        self.setObjectName("menuForm")
        # Menu form title
        self.label = QLabel(self)
        self.label.setText("menu")
        self.label.setFont(QFont("Arial",24,87,False))
        self.label.adjustSize() # auto resize the label
        self.label.setObjectName("formTitle")
        self.label.move(100,30) # X, Y

        # submit button
        self.submitButton = QPushButton(self)
        self.submitButton.setText('Submit')
        self.submitButton.setGeometry(QRect(85, 270, 130, 40))  # (x,y,w,h)
        self.submitButton.setObjectName("submitButton")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.submitButton.setFont(font)
        self.submitButton.clicked.connect(self.buttonEventHandler)




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
        window = menuForm()  # create an instance (an object) of the class
        window.show()
        app.exec()
    except Exception as e:
        print(e)