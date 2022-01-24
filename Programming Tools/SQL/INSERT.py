# https://www.w3schools.com/python/python_mysql_join.asp
import mysql.connector
from config import *
from datetime import datetime

scores_table = 'scores'
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host=host,
            user=userA,
            port='3306',
            password=password_root,
            database=database,
            auth_plugin='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)
        exit()

def database_create_table():
    timestamp = datetime.timestamp(datetime.now())
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        sql_statement = f"""
            INSERT INTO {database}.{scores_table}
            (userid,score,date) VALUES ({1},{108},{timestamp})
            """
        myCursor.execute(sql_statement)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)


database_create_table()