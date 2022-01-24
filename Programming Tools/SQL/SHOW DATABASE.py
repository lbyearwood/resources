import mysql.connector
from config import *
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host=host,
            user=userA,
            port=port,
            password=password_root,
            auth_plugin='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)
        exit()


def show_databases():
    db = connect_to_database()
    try:
        sql_statement = "SHOW databases"
        myCursor = db.cursor()
        myCursor.execute(sql_statement)
        for database in myCursor:
            print(database)
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

show_databases()