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

def update():
    try:
        db = connect_to_database()
        myCursor = db.cursor()
        SQL = f"""
                UPDATE yearwood.users
                SET password = 'dfgdfgsdf'
                WHERE user_id = 2
        """
        myCursor.execute(SQL)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

if __name__=="__main__":
    update()