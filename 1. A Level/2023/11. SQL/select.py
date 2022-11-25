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

def _select():
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        SQL = f"""
                SELECT username, password, active
                FROM yearwood.users
                WHERE active = 1
        """
        myCursor.execute(SQL)
        response = myCursor.fetchall()
        if response != []:
            for record in response:
                print(record)
        else:
            print("None found")


        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

if __name__=="__main__":
    _select()