import mysql.connector
from config import *
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database,
            port = '3306',
            auth_plugin ='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)

def create_table():
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        SQL = """
                CREATE TABLE questions (
                question_id INT AUTO_INCREMENT PRIMARY KEY,
                user_number INT NOT NULL,
                FOREIGN KEY (user_number) REFERENCES users(user_id))
        """
        myCursor.execute(SQL)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

if __name__=="__main__":
    create_table()