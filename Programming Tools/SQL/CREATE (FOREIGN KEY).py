# https://www.w3schools.com/python/python_mysql_join.asp
import mysql.connector
from config import *
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host=host,
            user=userA,
            port=port,
            password=password_root,
            database=database,
            auth_plugin='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)
        exit()

def database_create_table():
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        sql_statement = """
            CREATE TABLE scores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            userid INT NOT NULL,
            score INT NOT NULL,
            date VARCHAR(40) NOT NULL,
            FOREIGN KEY (userid) REFERENCES user(id))
            """
        myCursor.execute(sql_statement)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)


database_create_table()