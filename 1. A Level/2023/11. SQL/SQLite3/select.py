import sqlite3
connection = sqlite3.connect("test1.db")
cursor = connection.cursor()

SQL = """
    SELECT * FROM user
"""

records = cursor.execute(SQL).fetchall()

for record in records:
    print(record)

    userid,username, password,firstname,surname,dob,email,active = record

print(email)
cursor.close()
connection.close()