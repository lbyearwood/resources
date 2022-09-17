from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import re


import mysql.connector


# To do:
# formatcheck functions using regex
# make GUI nicer with colours etc.
# wampserver  phpmyadmin  127.0.0.1

class registerWindow(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()
        # sets the size of the window
        self.resize(400, 400)
        # sets the title of the window
        self.setWindowTitle("registration")
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
        self.label_title.setObjectName("Registration Title Label")
        # sets the X and Y coordinates of the title
        self.label_title.move(120, 10)

        ##Sub title label (same comments as above)
        self.label_registration = QLabel(self)
        self.label_registration.setText("Create Account")
        self.label_registration.setFont(QFont("Arial", 11, 81, False))
        self.label_registration.adjustSize()
        self.label_registration.setObjectName("Register Title Label")
        self.label_registration.move(140, 40)

        ##Email Label (same comments as above)
        self.label_email = QLabel(self)
        self.label_email.setText("Email:")
        self.label_email.setFont(QFont("Arial", 11, 70, False))
        self.label_email.adjustSize()
        self.label_email.setObjectName("email Label")
        self.label_email.move(10,70)

        ##Username Label (same comments as above)
        self.label_username = QLabel(self)
        self.label_username.setText("Username:")
        self.label_username.setFont(QFont("Arial", 11, 70, False))
        self.label_username.adjustSize()
        self.label_username.setObjectName("username Label")
        self.label_username.move(10, 120)

        ##Password Label (same comments as above)
        self.label_password = QLabel(self)
        self.label_password.setText("Password:")
        self.label_password.setFont(QFont("Arial", 11,70, False))
        self.label_password.adjustSize()
        self.label_password.setObjectName("password Label")
        self.label_password.move(10, 170)

        ## Confirm Password Label (same comments as above)
        self.label_confirmPassword = QLabel(self)
        self.label_confirmPassword.setText("Confirm password:")
        self.label_confirmPassword.setFont(QFont("Arial", 11, 70, False))
        self.label_confirmPassword.adjustSize()
        self.label_confirmPassword.setObjectName("confirmPassword Label")
        self.label_confirmPassword.move(10, 220)

        ## Invalid email label
        self.label_invalidEmail = QLabel(self)
        self.label_invalidEmail.setText("Email is not valid! Please change!")
        self.label_invalidEmail.setFont(QFont("Arial", 12, 81, False))
        self.label_invalidEmail.adjustSize()
        self.label_invalidEmail.setObjectName("invalidEmail Label")
        self.label_invalidEmail.move(10, 320)
        # this label is hidden so that it can be set to be seen when neccaesary
        self.label_invalidEmail.setHidden(True)

        ## valid email label (same comments as above)
        self.label_validEmail = QLabel(self)
        self.label_validEmail.setText("Valid Email")
        self.label_validEmail.setFont(QFont("Arial", 12, 81, False))
        self.label_validEmail.adjustSize()
        self.label_validEmail.setObjectName("validEmail Label")
        self.label_validEmail.move(10, 320)
        self.label_validEmail.setHidden(True)

        # Invalid username label(same comments as above)
        self.label_invalidUsername = QLabel(self)
        self.label_invalidUsername.setText("Username is not valid! Please change!")
        self.label_invalidUsername.setFont(QFont("Arial", 12, 81, False))
        self.label_invalidUsername.adjustSize()
        self.label_invalidUsername.setObjectName("invalidUsername Label")
        self.label_invalidUsername.move(10, 340)
        self.label_invalidUsername.setHidden(True)

        # valid username label(same comments as above)
        self.label_validUsername = QLabel(self)
        self.label_validUsername.setText("Username valid")
        self.label_validUsername.setFont(QFont("Arial", 12, 81, False))
        self.label_validUsername.adjustSize()
        self.label_validUsername.setObjectName("validUsername Label")
        self.label_validUsername.move(10, 340)
        self.label_validUsername.setHidden(True)

        # Invalid password label(same comments as above)
        self.label_invalidPassword = QLabel(self)
        self.label_invalidPassword.setText("Password is not valid! Please change!")
        self.label_invalidPassword.setFont(QFont("Arial", 12, 81, False))
        self.label_invalidPassword.adjustSize()
        self.label_invalidPassword.setObjectName("invalidPassword Label")
        self.label_invalidPassword.move(10, 360)
        self.label_invalidPassword.setHidden(True)

        # valid password label(same comments as above)
        self.label_validPassword = QLabel(self)
        self.label_validPassword.setText("Password valid")
        self.label_validPassword.setFont(QFont("Arial", 12, 81, False))
        self.label_validPassword.adjustSize()
        self.label_validPassword.setObjectName("validPassword Label")
        self.label_validPassword.move(10, 360)
        self.label_validPassword.setHidden(True)

        # passwords do not match label
        self.label_passwordsNotMatch = QLabel(self)
        self.label_passwordsNotMatch.setText("Passwords dont match")
        self.label_passwordsNotMatch.setFont(QFont("Arial", 12, 81, False))
        self.label_passwordsNotMatch.adjustSize()
        self.label_passwordsNotMatch.setObjectName("passwordsNotMatch Label")
        self.label_passwordsNotMatch.move(10, 360)
        self.label_passwordsNotMatch.setHidden(True)


        ##information Label(same comments as above)
        self.label_info = QLabel(self)
        self.label_info.setText("""Please ensure:
       - Email in format:
         example@example.com
       - Username between 5
         and 15 characters
       - Password between 5
         and 15 characters
       - Password must contain:
       1) 1 lower case
       2) 1 upper case
       3) 1 number""")
        self.label_info.setFont(QFont("Arial", 12, 60, False))
        self.label_info.adjustSize()
        self.label_info.setObjectName("info Label")
        self.label_info.move(180, 65)

        ##Email Textbox
        # creats the textbox
        self.Textbox_email = QLineEdit(self)
        # sets the width height x an y coordinates
        self.Textbox_email.setGeometry(10, 90, 190, 25)
        # unique identifer for the textbox set
        self.Textbox_email.setObjectName("Textbox_email")

        ##Username Textbox (same comments as above)
        self.Textbox_Username = QLineEdit(self)
        self.Textbox_Username.setGeometry(10, 140, 190, 25)
        self.Textbox_Username.setObjectName("Textbox_Username")

        ##Password Textbox(same comments as above)
        self.Textbox_password = QLineEdit(self)
        self.Textbox_password.setGeometry(10, 190, 190, 25)
        self.Textbox_password.setObjectName("Textbox_password")

        ##Confirm Password Textbox(same comments as above)
        self.Textbox_confirmPassword = QLineEdit(self)
        self.Textbox_confirmPassword.setGeometry(10, 240, 190, 25)
        self.Textbox_confirmPassword.setObjectName("Textbox_confirmPassword")

        ##CreateAccountButton
        # creats a button
        self.Button_submit = QPushButton(self)
        # sets the x and y co ordinates and the length and height of a ractangle
        self.Button_submit.setGeometry(QRect(10, 270, 100, 40))
        # allows us to edit font
        font = QFont()
        # set font size
        font.setPointSize(10)
        # sets the font for the button
        self.Button_submit.setFont(font)
        # sets the text
        self.Button_submit.setText("Create Account")
        # sets the unique identifer of the button
        self.Button_submit.setObjectName("CreateAccountButton")
        # defines what happens when button is clicked
        self.Button_submit.clicked.connect(self.VerifyCredentials)


        ##Back to login button
        self.Button_Back = QPushButton(self)
        self.Button_Back.setGeometry(QRect(310, 340, 80, 50))
        font = QFont()
        font.setPointSize(10)
        self.Button_Back.setFont(font)
        self.Button_Back.setText("Back to login")
        self.Button_Back.setObjectName("BackButton")
        self.Button_Back.clicked.connect(self.BackToLogin)
        self.hide()

    def BackToLogin(self):
        self.hide()


    # function to check if email is valid and outputs appropiate message
    def validateEmail(self):
        # variable email set to whats in the email textbox
        email = self.Textbox_email.text()
        # status flag
        emailValid = False
        # if it is in the correct format then valid is true (format checked by format check function)
        if self.emailFormatcheck(email) == True:
            emailValid = True
        # if email is valid then set the validemail label to not be hidden and hide the invalid label and vice versa
        if emailValid == False:
            self.label_validEmail.setHidden(True)
            self.label_invalidEmail.setHidden(False)
            self.Textbox_email.clear()
        else:
            self.label_invalidEmail.setHidden(True)
            self.label_validEmail.setHidden(False)
            # returns the valid email or none if email is invalid
            return email

    # function to check if USERNAME is valid and outputs appropiate message
    def validateUsername(self):
        # variable username set to whats in the username textbox
        username = self.Textbox_Username.text()
        # status flag
        usernameValid = False
        # if it is in the correct format then valid is true (format checked by formatCheck function)
        if self.usernameFormatcheck(username) == True:
            usernameValid = True
        # if username is valid then set the validUsername label as not hidden and hide the invalid label and vice versa
        if usernameValid == False:
            self.label_validUsername.setHidden(True)
            self.label_invalidUsername.setHidden(False)
            self.Textbox_Username.clear()
        else:
            self.label_invalidUsername.setHidden(True)
            self.label_validUsername.setHidden(False)
            # returns the valid username or none if username is invalid
            return username

    # function to check if password is valid and outputs appropriate message
    def validatePassword(self):
        # variable password set to whats in the password textbox
        password = self.Textbox_password.text()
        confirmPassword = self.Textbox_confirmPassword.text()
        if password == confirmPassword:
            if self.passwordFormatcheck(password) == True:
                self.label_invalidPassword.setHidden(True)
                self.label_passwordsNotMatch.setHidden(True)
                self.label_validPassword.setHidden(False)
                return password
        # if password is valid then set the validPassword label as not hidden and hide the invalid label and vice versa
            else:
                self.label_validPassword.setHidden(True)
                self.label_invalidPassword.setHidden(False)
                self.label_passwordsNotMatch.setHidden(True)
                self.Textbox_password.clear()
                self.Textbox_confirmPassword.clear()
        else:
            self.label_passwordsNotMatch.setHidden(False)
            self.label_validPassword.setHidden(True)
            self.label_invalidPassword.setHidden(True)
            self.Textbox_password.clear()
            self.Textbox_confirmPassword.clear()

            # returns the valid password or none if password is invalid


    # function to check password is in the correct format
    def passwordFormatcheck(self, password):
        pattern = "^.*(?=.{8,15})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.]).*$"
        password = password
        result = re.findall(pattern, password)
        if result:
            print("Valid password")
            return True
        else:
            print("Password not valid")

    # function to check email is in the correct format
    def emailFormatcheck(self, email):
        return True

    # function to check username is in the correct format
    def usernameFormatcheck(self, username):
        username = username
        if len(username) > 15 or len(username) < 8:
            return False
        else:
            return True

    # function checks that email,username,password are valid and can be stored in the database
    def VerifyCredentials(self):
        email = self.validateEmail()
        username = self.validateUsername()
        password = self.validatePassword()
        print(email, username, password)
        if email is not None and username is not None and password is not None:
            self.addToDatabase(email, username, password)

    # adds the appropriate fields into the database
    def addToDatabase(self, email, username, password):
        print("Adding to Database")
        database = self.connect_database()
        try:
            sql = f"""
INSERT INTO tic_db.user
VALUES('{username}','{email}','{password}',0,0,0)
"""
            myCursor = database.cursor()
            myCursor.execute(sql)
        except Exception as e:
            print(e)
        self.hide()


    # connects to the database
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


if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # QApplication is written in C++ so this calls the constructer for it and yses the sys.arg argument to initialise the application so that it can be run with python
    window = registerWindow()  # instantiates window class
    window.show()  # shows all the widgets
    app.exec()  # executes the code
