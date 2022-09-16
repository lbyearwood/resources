from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from config import *

class MainWindow(QMainWindow): # inherit QMainWindow
    def __init__(self): # constructor
        super().__init__()
        self.setAutoFillBackground(True)
        self.resize(300,350) # width , height
        self.setWindowTitle("Login Form")

        # Label - Form Title
        self.label_title = QLabel(self)
        self.label_title.setText("Login")
        self.label_title.setFont(QFont('Arial',24,87,False)) # font family,size,weight,italic
        self.label_title.adjustSize()
        self.label_title.setObjectName("Form_Title_Label")
        self.label_title.move(100,30) # position on form

        # Label - Username
        self.label_username = QLabel(self)
        self.label_username.setText("Username")
        self.label_username.setFont(QFont('Arial', 12, 81, False))  # font family,size,weight,italic
        self.label_username.adjustSize()
        self.label_username.setObjectName("Username_Label")
        self.label_username.move(20, 80)  # position on form

        # QLineEdit - Username
        self.QLineEdit_username = QLineEdit(self)
        self.QLineEdit_username.setGeometry(20,110,240,31) # (x,y,w,h) (left,top)
        self.QLineEdit_username.setObjectName("Username_QLineEdit")

        # Label - Password
        self.label_password = QLabel(self)
        self.label_password.setText("Password")
        self.label_password.setFont(QFont('Arial', 12, 81, False))  # font family,size,weight,italic
        self.label_password.adjustSize()
        self.label_password.setObjectName("Password_Label")
        self.label_password.move(20, 150)  # position on form

        # QLineEdit - Password
        self.QLineEdit_password = QLineEdit(self)
        self.QLineEdit_password.setGeometry(20, 180, 240, 31)  # (x,y,w,h) (left,top)
        self.QLineEdit_password.setObjectName("Password_QLineEdit")
        self.QLineEdit_password.setEchoMode(QLineEdit.Password)


        # Push Button - Submit
        self.pushButton_submit = QPushButton(self)
        self.pushButton_submit.setGeometry(QRect(85,280,131,40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setText('Submit')
        self.pushButton_submit.setObjectName('Submit_PushButton')
        self.pushButton_submit.clicked.connect(self.pushButton_submit_eventHandler)


        # error label
        self.label_login_message = QLabel(self)
        self.label_login_message.move(85,245)
        self.label_login_message.setText('Incorrect Credentials! Try again')
        self.label_login_message.setObjectName("label_login_message")
        self.label_login_message.setHidden(True)

        self.setStyleSheet("""
            QLabel#label_login_message{
            color:#ff0000;
            }
                   
        """        )

        self.show()

    def connect_to_database(self):  # passs through arguments to return connection and cursor ( to control)
        try:
            db = mysql.connector.connect(
                host=host,
                user=user,
                port=port,
                password=password,
                database=database,
                auth_plugin="mysql_native_password"
            )
            return db
        except Exception as e:
            print(e)

    def pushButton_submit_eventHandler(self):
         password = self.QLineEdit_password.text()
         username = self.QLineEdit_username.text()
         self.verify_user(username,password)

    def verify_user(self,username,password):
        db = self.connect_to_database()
        try:
            sql_statement = f"""
            SELECT * FROM {database}.{user_table}
            WHERE username = '{username}' AND password = '{password}'
            """
            myCursor = db.cursor()
            myCursor.execute(sql_statement)
            response = myCursor.fetchall()
            if len(response) == 0:
                self.label_login_message.setHidden(False)
                print("Incorrect credentials")
            else:
                print("Welcome")
            db.commit()
            myCursor.close()
            db.disconnect()
        except Exception as e:
            print(e)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainWindow() # instantiate the class (create an object)
    window.show()
    app.exec()