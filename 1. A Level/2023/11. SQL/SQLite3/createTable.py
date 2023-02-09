import sqlite3
connection = sqlite3.connect("test1.db")
cursor = connection.cursor()

SQL = """
    CREATE TABLE user (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        firstname TEXT,
        surname TEXT,
        dob TEXT,
        email TEXT,
        active INTEGER
    )
"""

cursor.execute(SQL)
cursor.close()
connection.close()