import mysql.connector
from config import *

def connect_to_database():
    try:
        db = mysql.connector.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)

def alter_table():
    db = connect_to_database()
    try:
        sql_statement = f"""
        ALTER TABLE {database}.{user_table} ADD testCol int(11)
            """
        myCursor = db.cursor()
        myCursor.execute(sql_statement)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

alter_table()