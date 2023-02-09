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
        myCursor = db.cursor()
        print(myCursor)
        myCursor.close()
        db.disconnect()

    except Exception as e:
        print(e)

def verified_user(username,password):
        db = connect_to_database()
        try:
            SQL = f"""
                SELECT username,password,active
                FROM yearwood.user
                WHERE username = '{username}' AND password = '{password}'
                """
            myCursor = db.cursor()
            myCursor.execute(SQL)
            response = myCursor.fetchall()
            db.commit()
            if len(response) == 0:
                print("Invalid credentials, try again")
            else:
                print("Welcome")

                # load the window
            myCursor.close()
            db.disconnect()
        except Exception as e:
            print(e)


if __name__=="__main__":
    verified_user("test","test")