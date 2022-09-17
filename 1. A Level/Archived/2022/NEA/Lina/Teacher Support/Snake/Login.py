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
        self.setWindowTitle("Login form")

        # Label - Form Title
        self.label_title = QLabel(self)
        self.label_title.setText("Login")
        self.label_title.setFont(QFont('Arial', 24,81, False)) # font-family, size, weight, italic
        self.label_title.adjustSize()
        self.label_title.setObjectName("Label_Form_Title")
        self.label_title.move(100,30)

        # Label - username
        self.label_username = QLabel(self)
        self.label_username.setText("Username")
        self.label_username.setFont(QFont('Arial', 12,81, False)) # font-family, size, weight, italic
        self.label_username.adjustSize()
        self.label_username.setObjectName("Label_username")
        self.label_username.move(20,80)

        # QLineEdit - username
        self.QLineEdit_username = QLineEdit(self)
                                                            # left, top
        self.QLineEdit_username.setGeometry(20,120,240,31) # (x,y,w,h)
        self.QLineEdit_username.setObjectName("QLineEdit_username")


        # Label - password
        self.label_password = QLabel(self)
        self.label_password.setText("Password")
        self.label_password.setFont(QFont('Arial', 12,81, False)) # font-family, size, weight, italic
        self.label_password.adjustSize()
        self.label_password.setObjectName("Label_password")
        self.label_password.move(20,160)

        # QLineEdit - password
        self.QLineEdit_password = QLineEdit(self)
                                                            # left, top
        self.QLineEdit_password.setGeometry(20,190,240,31) # (x,y,w,h)
        self.QLineEdit_password.setObjectName("QLineEdit_password")
        self.QLineEdit_password.setEchoMode(QLineEdit.Password)

        # push button
        self.pushButton_submit = QPushButton(self)
        self.pushButton_submit.setGeometry(QRect(85,270,131,40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setText('Submit')
        self.pushButton_submit.setObjectName('pushButton_submit')
        self.pushButton_submit.clicked.connect(self.pushButton_submit_eventHandler)

        # error label
        self.label_login_message = QLabel(self)
        self.label_login_message.move(70, 245)
        self.label_login_message.setText('Incorrect credentials! Try again')
        self.label_login_message.adjustSize()
        self.label_login_message.setObjectName("label_login_message")
        self.label_login_message.setHidden(True)
        self.setStyleSheet("""
            QLabel#label_login_message{
            color:#ff0000;
            }
        
        """)




        self.show()

    def connect_to_database(self):
        try:
            db = mysql.connector.connect(
                host=host,
                user=user,
                port=port,
                password=password,
                database=database,
                auth_plugin='mysql_native_password'
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow() # instantiate the object
    window.show()
    app.exec()



