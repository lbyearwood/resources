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
        myCursor = db.cursor()
        print(myCursor)
        myCursor.close()
        db.disconnect()

    except Exception as e:
        print(e)

if __name__=="__main__":
    connect_to_database()