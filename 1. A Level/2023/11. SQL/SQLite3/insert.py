import sqlite3
connection = sqlite3.connect("test1.db")
cursor = connection.cursor()

try:
    SQL = """
        INSERT INTO user (username, 
        password,
        firstname, 
        surname,
        dob,
        email,
        active)
        VALUES ("test","test","test","test","01/01/2001","test.test@test.com",1)
    """
    cursor.execute(SQL)
    connection.commit()
    cursor.close()
    connection.close()
except Exception as e:
    print(e)