from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from menu import  menuForm

class LoginForm(QMainWindow): # inherit the parent class
    def __init__(self): # define the child class constructor
        self.m1 = menuForm()
        super().__init__()  # make use of the parent class constructor
        formWidth = 300
        formHeight = 350

        self.setFixedSize(formWidth,formHeight)
        self.setAutoFillBackground(True)
        self.setWindowTitle("Login Form")
        self.setObjectName("loginForm")

        # login form title
        self.label = QLabel(self)
        self.label.setText("Login")
        self.label.setFont(QFont("Arial",24,87,False))
        self.label.adjustSize() # auto resize the label
        self.label.setObjectName("labelTitle")
        self.label.move(100,30) # X, Y

        # username label
        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText("Enter username")
        self.usernameLabel.setFont(QFont("Arial", 12, 10, False))
        self.usernameLabel.adjustSize()  # auto resize the label
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.move(30, 90)  # X, Y

        # username textbox
        self.usernameTextbox = QLineEdit(self)
        self.usernameTextbox.setGeometry(30,120,240,30) # (x,y,w,h)
        self.usernameTextbox.setObjectName("usernameTextbox")

        # password label
        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText("Enter password")
        self.passwordLabel.setFont(QFont("Arial", 12, 10, False))
        self.passwordLabel.adjustSize()  # auto resize the label
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLabel.move(30, 170)  # X, Y

        # password textbox
        self.passwordTextbox = QLineEdit(self)
        self.passwordTextbox.setGeometry(30,200,240,30) # (x,y,w,h)
        self.passwordTextbox.setObjectName("passwordTextbox")
        self.passwordTextbox.setEchoMode(QLineEdit.Password)

        # submit button
        self.submitButton = QPushButton(self)
        self.submitButton.setText('Submit')
        self.submitButton.setGeometry(QRect(85,270,130,40)) # (x,y,w,h)
        self.submitButton.setObjectName("submitButton")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.submitButton.setFont(font)
        self.submitButton.clicked.connect(self.buttonEventHandler)

        # error message label
        self.errorLabel = QLabel(self)
        self.errorLabel.setText("Incorrect Credentials! Try again")
        self.errorLabel.setFont(QFont("Arial", 8, 10, False))
        self.errorLabel.adjustSize()  # auto resize the label
        self.errorLabel.setObjectName("errorMessage")
        self.errorLabel.move(30, 240)  # X, Y
        self.errorLabel.setHidden(True)

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

        self.show()

    def buttonEventHandler(self):
        username = self.usernameTextbox.text().lower()
        password = self.passwordTextbox.text()
        try:
            file = open(f"{username}.txt","r")
            getPassword = file.read()
            if password == getPassword:
                print(True)
                self.m1.show()
                self.close()
            else:
                print(False)
                self.errorLabel.setHidden(False)
        except Exception as e:
            print("username not found")
            self.errorLabel.setHidden(False)




if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = LoginForm() # create an instance (an object) of the class
        window.show()
        app.exec()
    except Exception as e:
        print(e)