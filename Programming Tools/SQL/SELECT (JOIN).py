import mysql.connector
from config import *
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host=host,
            user=userA,
            port=port,
            password=password_root,
            database=database,
            auth_plugin='mysql_native_password'
        )
        return db
    except Exception as e:
        print(e)
        exit()

def database_select_from_table():
    db = connect_to_database()
    try:
        sql_statement = f"""
        SELECT {user_table}.username, {score_table}.score,  {score_table}.date
        FROM {user_table}
        INNER JOIN scores ON {user_table}.id = {score_table}.userid
        """
        myCursor = db.cursor()
        myCursor.execute(sql_statement)
        response = myCursor.fetchall()
        for record in response:
            print(record)
        db.commit()
        myCursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

database_select_from_table()