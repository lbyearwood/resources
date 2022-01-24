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

def update_table():
    db = connect_to_database()
    try:
        sql_statement = f"""
        UPDATE {database}.{user_table}
        SET username = "Max", password = "sdkfh", active={0}
        WHERE id = 1
        """
        myCursor = db.cursor()
        myCursor.execute(sql_statement)
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)
update_table()