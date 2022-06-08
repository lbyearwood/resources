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

def updateTable():
    db = connect_database()
    try:
        mycursor = db.cursor()  #tool to manipulate the database
        sql_statment1 = """
        ALTER TABLE user
        ADD win int(100)"""
        sql_statment2 = """
        ALTER TABLE user
        ADD draw int(100)"""
        sql_statement3 = """
        ALTER TABLE user
        ADD loss int(100)
        """
        mycursor.execute(sql_statment1)
        mycursor.execute(sql_statment2)
        mycursor.execute(sql_statement3)
        db.commit()
        mycursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

updateTable()