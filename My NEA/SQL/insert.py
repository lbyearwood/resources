import mysql.connector  # install and import the sql library
database = "tic_db"

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

def insert():
    db = connect_database()
    try:
        insert_statment = f"""INSERT INTO {database}.user
(username,email,password,status) VALUES ('test', 'test@gmail','Pass', 'active')"""
        mycursor = db.cursor()
        mycursor.execute(insert_statment)
        db.commit()
        mycursor.close()
        db.disconnect()
    except Exception as e:
        print(e)

insert()