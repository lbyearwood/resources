import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # main window in window




class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__() # initialise the super class constructor
        formWidth = 300
        formHeight = 370
        self.setFixedSize(formWidth,formHeight)
        self.setWindowTitle("Login form")
        self.setObjectName("login_form")

        # main title
        self.label_title = QLabel(self) # pass through the object as an argument
        self.label_title.setText("Login")
        self.label_title.setFont(QFont('Arial',24,87,False)) # args (family-font,size,weight,italic)
        self.label_title.adjustSize()
        self.label_title.setObjectName("label_title")
        self.label_title.move(100,30) # x,y

        # username title
        self.label_username = QLabel(self) # pass through the object as an argument
        self.label_username.setText("Username:")
        self.label_username.setFont(QFont('Arial',14,10,False)) # args (family-font,size,weight,italic)
        self.label_username.adjustSize()
        self.label_username.setObjectName("label_title")
        self.label_username.move(30,100) # x,y

        # username textbox
        self.textBox_username = QLineEdit(self)
        self.textBox_username.setObjectName("textbox_username")
        self.textBox_username.setGeometry(30,140,230,30) # (x,y,w,h)

        # label password
        self.label_password = QLabel(self) # pass through the object as an argument
        self.label_password.setText("Password:")
        self.label_password.setFont(QFont('Arial',14,10,False)) # args (family-font,size,weight,italic)
        self.label_password.adjustSize()
        self.label_password.setObjectName("label_password")
        self.label_password.move(30,200) # x,y

        # password textbox
        self.textBox_password  = QLineEdit(self)
        self.textBox_password.setObjectName("textbox_password")
        self.textBox_password.setGeometry(30,240,230,30) # (x,y,w,h)


        # submit button
        self.submit_button  = QPushButton(self)
        self.submit_button.setObjectName("submit_button")#
        self.submit_button.setText("Submit")
        self.submit_button.setGeometry(70,300,130,40)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.submit_button.setFont(font)




        self.show()

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv) # convert to format for windows platform
        window = LoginForm()
        window.show()
        app.exec()
    except Exception as e:
        print(e)