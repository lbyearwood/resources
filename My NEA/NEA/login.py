from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from register import registerWindow
from Menu import *
from ForgotPassword import resetPassWindow



# To Do set up buttons for forgot password and register

class loginWindow(QMainWindow):
    def __init__(self):  # constructor
        super().__init__() # inheriting the QMain Window
        self.regWindow = registerWindow()  # instantiates register window class
        self.ResetWindow = resetPassWindow() # instantiates the resetpassword class
        # sets the background colour to the default
        self.setAutoFillBackground(True)
        # resizes the window (X and Y)
        self.resize(500, 260)
        # sets a title to the form
        self.setWindowTitle("Login")
        self.setStyleSheet(
            """QMainWindow{
            background-color:#13A6EA
            }
            """
        )

        ###Login Label
        # instantiates a label object
        self.label_title = QLabel(self)
        # sets the text to login
        self.label_title.setText("""Welcome to Tic-Tac-Toe
       Please login""")
        # defines the font, size weight and weather we use italics
        self.label_title.setFont(QFont("Arial", 20, 81, False))
        # adjusts the size of the label according to text length
        self.label_title.adjustSize()
        #  sets the name of the label unique reference to the label
        self.label_title.setObjectName("label_form_title")
        # which co-ordinates is the label located  (X, Y)
        self.label_title.move(90, 10)

        ###Username Label
        # same process as above label
        self.label_username = QLabel(self)
        self.label_username.setText("Username:")
        self.label_username.setFont(QFont("Arial", 16, 70, False))
        self.label_username.adjustSize()
        self.label_username.setObjectName("label_form_username")
        self.label_username.move(20, 100)

        ###Password label
        # same process as login label
        self.label_password = QLabel(self)
        self.label_password.setText("Password:")
        self.label_password.setFont(QFont("Ariel", 16, 65, False))
        self.label_password.adjustSize()
        self.label_password.setObjectName("label_form_password")
        self.label_password.move(20, 130)

        ###ForgottenPassword Label
        # same process as above
        self.label_forgot_password = QLabel(self)
        self.label_forgot_password.setText("Forgotten Password?")
        self.label_forgot_password.setFont(QFont("Ariel", 13, 50, False))
        self.label_forgot_password.adjustSize()
        self.label_forgot_password.setObjectName("label_form_password")
        self.label_forgot_password.move(20, 160)

        ###unsuccesful login Label
        # same process as above
        self.label_unsuccessfulLogin = QLabel(self)
        self.label_unsuccessfulLogin.setText("Incorrect details!! Please Try Again")
        self.label_unsuccessfulLogin.setFont(QFont("", 14, 81, False))
        self.label_unsuccessfulLogin.adjustSize()
        self.label_unsuccessfulLogin.setObjectName("label_unsuccessfulLogin")
        self.label_unsuccessfulLogin.move(20, 200)
        # makes the label hidden until it is set as false if this message is required to be shown to the user
        self.label_unsuccessfulLogin.setHidden(True)

        ### Password Textbox
        self.Textbox_Password = QLineEdit(self)
        # sets the X Y and width and height of tex box
        self.Textbox_Password.setGeometry(130, 130, 250, 25)
        # unique reference to the textbox
        self.Textbox_Password.setObjectName("Textbox_Password")
        # hides text as it is a password
        self.Textbox_Password.setEchoMode(QLineEdit.Password)

        ### Username Textbox
        # same as above
        self.Textbox_Username = QLineEdit(self)
        self.Textbox_Username.setGeometry(130, 100, 250, 25)
        self.Textbox_Username.setObjectName("Textbox_Username")

        ### Submit Password button
        # creates a button
        self.Button_submit = QPushButton(self)
        # sets the x, y co ordinate and the length and height
        self.Button_submit.setGeometry(QRect(390, 100, 100, 58))
        # calls the font class
        font = QFont()
        # sets the size of the text
        font.setPointSize(16)
        # sets weather or not it is bold
        font.setBold(True)
        # sets the font as we have specified above
        self.Button_submit.setFont(font)
        # sets the text for the button
        self.Button_submit.setText("Submit")
        # sets a unique identifier for the button
        self.Button_submit.setObjectName("Submit Button")
        self.Button_submit.clicked.connect(self.submitButtonPressed)
        self.Button_submit.setStyleSheet("background-color : green")

        ###Forgotten Password Button
        self.resetPassButton = QPushButton(self)
        self.resetPassButton.setGeometry(QRect(180, 160, 100, 20))
        font = QFont()
        font.setPointSize(10)
        self.resetPassButton.setFont(font)
        self.resetPassButton.setText("Reset Password")
        self.resetPassButton.setObjectName("Reset Password Button")
        self.resetPassButton.clicked.connect(self.resetPassword)
        self.resetPassButton.setStyleSheet("background-color : red")

        ###create account button
        self.createAccountButton = QPushButton(self)
        self.createAccountButton.setGeometry(QRect(390, 200, 100, 50))
        fontA = QFont()
        fontA.setPointSize(12)
        self.createAccountButton.setFont(fontA)
        self.createAccountButton.setText("Register")
        self.createAccountButton.setObjectName("create account pass")
        self.createAccountButton.clicked.connect(self.createAccount)
        self.show()

    def resetPassword(self):
        try:

            self.ResetWindow.show()  # shows all the widgets

        except Exception as e:
            print(e)
    def createAccount(self):
        try:

            self.regWindow.show()  # shows all the widgets

        except Exception as e:
            print(e)

    # this is what happens when the submit button is pressed
    def submitButtonPressed(self):
        # sets the variable password to what the user inputted in the password textbox
        password = self.Textbox_Password.text()
        # does the same for username
        username = self.Textbox_Username.text()
        # calls the verifyUser procedure
        self.VerifyUser(username, password)

    # this connects to the database
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

    # verifies if the credentials entered by the user match what is in the database
    def VerifyUser(self, username, password):
        # connects to the database
        database = self.connect_database()
        try:  # execute the following SQL statment
            sql_statement = f"""
                  SELECT username, password, win, draw, loss
                  FROM tic_db.user
                  WHERE username = '{username}' AND password = '{password}'
                  """
            myCursor = database.cursor()
            myCursor.execute(sql_statement)
            response = myCursor.fetchall()
            # if we dont get a response from the database(means the credentials entered do not match the database)
            userDetails = None
            if len(response) == 0:
                #show the unsuccesful login label
                self.label_unsuccessfulLogin.setHidden(False)
                self.Textbox_Username.clear()
                self.Textbox_Password.clear()
            else:
                for record in response:
                    userDetails = record
                    print(record)
                #hide the logn window
                self.hide()
                #open the main menu window
                self.MenuWindow = mainMenu(userDetails)
                self.MenuWindow.show()
            database.commit()
            myCursor.close()
            database.disconnect()
        except Exception as e:
            print(e)



if __name__ == "__main__":  # if this is the main module then run the following code
    app = QApplication(sys.argv)  # converts code into correct format
    window = loginWindow()  # instantiates window class
    window.show()  # shows all the widgets
    app.exec()  # executes the code
