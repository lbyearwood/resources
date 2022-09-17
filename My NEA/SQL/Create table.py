import mysql.connector  # install and import the sql library


def connect_database():
    try:
        db = mysql.connector.connect(
            host='10.170.140.46',
            user='javed',
            port='3306',
            password='javed1234',
            database="tic_db",
            auth_plugin="mysql_native_password"
        )
        return db
    except Exception as e:
        print(e)


def createTable():
    db = connect_database()
    try:
        mycursor = db.cursor()  #tool to manipulate the database
        sql_statment = """
        CREATE TABLE user(
        Username VARCHAR(12) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        Password VARCHAR(15) NOT NULL,
        PRIMARY KEY(Username)
        )"""
        mycursor.execute(sql_statment)
        db.commit()
        mycursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

createTable()