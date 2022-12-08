from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from config import *
import mysql.connector

class login_form(QMainWindow): # inheritance
    def __init__(self): # child constructor
        super().__init__() # parent constructor
        self.session_id = None
        self.setWindowTitle("Login")
        self.setObjectName("loginForm")
        width = 300
        height = 350
        self.setFixedSize(width,height)
        self.setAutoFillBackground(True)

        # Window Title
        self.login_label = QLabel(self)
        self.login_label.setText("Login Form")
        self.login_label.setFont(QFont('Arial', 12, 800, False)) # (family-font,size,weight,italic)
        self.login_label.adjustSize()
        self.login_label.setObjectName("loginLabel")
        self.login_label.move(100, 30)

        # Username label
        self.username_label = QLabel(self)
        self.username_label.setText("Username")
        self.username_label.setFont(QFont('Arial', 12, 800, False)) # (family-font,size,weight,italic)
        self.username_label.adjustSize()
        self.username_label.setObjectName("usernameLabel")
        self.username_label.move(30, 80)

        # textbox
        self.username_textbox = QLineEdit(self)
        self.username_textbox.setObjectName("usernameTextBox")
        self.username_textbox.setGeometry(30, 110, 240, 30) # (x,y,w,h)

        # Password label
        self.password_label = QLabel(self)
        self.password_label.setText("Password")
        self.password_label.setFont(QFont('Arial', 12, 800, False)) # (family-font,size,weight,italic)
        self.password_label.adjustSize()
        self.password_label.setObjectName("usernameLabel")
        self.password_label.move(30, 170)

        # Password textbox
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setObjectName("usernameTextBox")
        self.password_textbox.setGeometry(30, 200, 240, 30) # (x,y,w,h)
        self.password_textbox.setEchoMode(QLineEdit.Password)


        self.show()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = login_form() # create an instance (object)
        window.show()
        app.exec()

    except Exception as e:
        print(e)


