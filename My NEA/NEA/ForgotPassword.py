from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import re

import mysql.connector

class resetPassWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.setWindowTitle("Reset Password")

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
        self.setStyleSheet(
            """QMainWindow{
            background-color:#13A6EA
            }
            """
        )

        ##Sub title label (same comments as above)
        self.label_registration = QLabel(self)
        self.label_registration.setText("Reset Password")
        self.label_registration.setFont(QFont("Arial", 11, 81, False))
        self.label_registration.adjustSize()
        self.label_registration.setObjectName("Register Title Label")
        self.label_registration.move(140, 40)

        ##email label
        self.label_email = QLabel(self)
        self.label_email.setText("Email:")
        self.label_email.setFont(QFont("Arial", 15, 81, False))
        self.label_email.adjustSize()
        self.label_email.setObjectName("email Label")
        self.label_email.move(30, 80)

        ##password label
        self.label_password = QLabel(self)
        self.label_password.setText("New Password:")
        self.label_password.setFont(QFont("Arial", 15, 81, False))
        self.label_password.adjustSize()
        self.label_password.setObjectName("password Label")
        self.label_password.move(30, 150)

        #confirm password label
        self.label_confirmPassword = QLabel(self)
        self.label_confirmPassword.setText("Confirm password:")
        self.label_confirmPassword.setFont(QFont("Arial", 15, 81, False))
        self.label_confirmPassword.adjustSize()
        self.label_confirmPassword.setObjectName("confirmPassword Label")
        self.label_confirmPassword.move(30, 220)

        #wrong email label
        self.label_wrongEmail = QLabel(self)
        self.label_wrongEmail.setText("Email not Found")
        self.label_wrongEmail.setFont(QFont("Arial", 12, 81, False))
        self.label_wrongEmail.adjustSize()
        self.label_wrongEmail.setObjectName("wrong email")
        self.label_wrongEmail.move(120,300)
        self.label_wrongEmail.setHidden(True)

        # Invalid password label(same comments as above)
        self.label_invalidPassword = QLabel(self)
        self.label_invalidPassword.setText("Password is not valid!")
        self.label_invalidPassword.setFont(QFont("Arial", 12, 81, False))
        self.label_invalidPassword.adjustSize()
        self.label_invalidPassword.setObjectName("invalidPassword Label")
        self.label_invalidPassword.move(120, 315)
        self.label_invalidPassword.setHidden(True)

        # password dont match label
        self.label_passwordsNotMatch = QLabel(self)
        self.label_passwordsNotMatch.setText("Passwords dont match")
        self.label_passwordsNotMatch.setFont(QFont("Arial", 12, 81, False))
        self.label_passwordsNotMatch.adjustSize()
        self.label_passwordsNotMatch.setObjectName("passwordsNotMatch Label")
        self.label_passwordsNotMatch.move(120, 315)
        self.label_passwordsNotMatch.setHidden(True)

        # email textbox
        self.Textbox_email = QLineEdit(self)
        self.Textbox_email.setGeometry(30, 110, 280, 30)
        self.Textbox_email.setObjectName("Textbox_email")

        # password textbox
        self.Textbox_password = QLineEdit(self)
        self.Textbox_password.setGeometry(30, 180, 280, 30)
        self.Textbox_password.setObjectName("Textbox_password")

        # confirm password textbox
        self.Textbox_ConfirmPassword = QLineEdit(self)
        self.Textbox_ConfirmPassword.setGeometry(30, 250, 280, 30)
        self.Textbox_ConfirmPassword.setObjectName("Textbox_ConfirmPassword")

        ##Back to login button
        self.Button_Back = QPushButton(self)
        self.Button_Back.setGeometry(QRect(310, 340, 80, 50))
        font = QFont()
        font.setPointSize(10)
        self.Button_Back.setFont(font)
        self.Button_Back.setText("Back to login")
        self.Button_Back.setObjectName("BackButton")
        self.Button_Back.clicked.connect(self.BackToLogin)

        ##submit button
        self.Button_Submit = QPushButton(self)
        self.Button_Submit.setGeometry(QRect(30, 300, 80, 50))
        font = QFont()
        font.setPointSize(10)
        self.Button_Submit.setFont(font)
        self.Button_Submit.setText("Submit")
        self.Button_Submit.setObjectName("BackButton")
        self.Button_Submit.clicked.connect(self.submit)

        #hides the window so that when we call it from login it shows
        self.hide()


    #hides the window to return it to login
    def BackToLogin(self):
        self.hide()

    #sub routine to handle the submit button event
    def submit(self):
        #sets the email to whats in the textbox
        email = self.Textbox_email.text()
        # connects to the database
        database = self.connect_database()
        try:  # execute the following SQL statment
            sql_statement = f"""
                          SELECT username, password, win, draw, loss
                          FROM tic_db.user
                          WHERE email = '{email}'
                          """
            myCursor = database.cursor()
            myCursor.execute(sql_statement)
            response = myCursor.fetchall()
            # if we dont get a response from the database(means the credentials entered do not match the database)
            userDetails = None
            if len(response) == 0:
                # show the wrong email label
                self.label_wrongEmail.setHidden(False)
                #clears the email textbox
                self.Textbox_email.clear()
            else:
                self.label_wrongEmail.setHidden(True)
                #goes on to validate password
                self.validatePassword(email)




            database.commit()
            myCursor.close()
            database.disconnect()
        except Exception as e:
            print(e)

    #subroutine to add the new password to the database
    def addToDatabase(self,password,email):
        #connects to the database
        database = self.connect_database()
        #execute following sql statment
        try:
            #updates the password associsated with the email
            sql = f"""
        UPDATE tic_db.user
        SET password = '{password}'
        WHERE email = '{email}'
        """
            myCursor = database.cursor()
            myCursor.execute(sql)
        except Exception as e:
            print(e)
        #sub to email the user to confirm password change
        self.emailUser()
        #hides window as password has been updated
        self.hide()

    def emailUser(self):
        print("emailing user")


    #subrouine to connect to database
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

    #validates the password and checks if passwords match
    def validatePassword(self,email):
        # variable password set to whats in the password textbox
        email = email
        password = self.Textbox_password.text()
        confirmPassword = self.Textbox_ConfirmPassword.text()
        if password == confirmPassword:
            if self.passwordFormatcheck(password) == True:
                self.label_invalidPassword.setHidden(True)
                self.label_passwordsNotMatch.setHidden(True)
                self.addToDatabase(password,email)

        # if password is valid then set the validPassword label as not hidden and hide the invalid label and vice versa
            else:
                self.label_invalidPassword.setHidden(False)
                self.label_passwordsNotMatch.setHidden(True)
                self.Textbox_password.clear()
                self.Textbox_ConfirmPassword.clear()
        else:
            self.label_passwordsNotMatch.setHidden(False)
            self.label_invalidPassword.setHidden(True)
            self.Textbox_password.clear()
            self.Textbox_ConfirmPassword.clear()

    #checks the format of the password
    def passwordFormatcheck(self, password):
        pattern = "^.*(?=.{8,15})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=.]).*$"
        password = password
        result = re.findall(pattern, password)
        if result:
            print("Valid password")
            return True
        else:
            print("Password not valid")





if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # converts code into correct format
    resetWindow = resetPassWindow()  # instantiates window class
    resetWindow.show()  # shows all the widgets
    app.exec()
