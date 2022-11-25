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

def describe_table():
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        SQL = "DESCRIBE yearwood.users"
        myCursor.execute(SQL)
        for field in myCursor:
            print(field)
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

if __name__=="__main__":
    describe_table()