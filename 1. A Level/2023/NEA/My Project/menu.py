from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector

class menu_form(QMainWindow):
    def __init__(self): # child constructor
        super().__init__() # parent constructor
        self.session_id = None
        self.setWindowTitle("Menu")
        self.setObjectName("menuForm")
        width = 900
        height = 850
        self.setFixedSize(width,height)
        self.setAutoFillBackground(True)

        # Window Title
        self.login_label = QLabel(self)
        self.login_label.setText("Menu")
        self.login_label.setFont(QFont('Arial', 12, 800, False)) # (family-font,size,weight,italic)
        self.login_label.adjustSize()
        self.login_label.setObjectName("menuLabel")
        self.login_label.move(100, 30)



if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = menu_form() # create an instance (object)
        window.show()
        app.exec()
    except Exception as e:
        print(e)
