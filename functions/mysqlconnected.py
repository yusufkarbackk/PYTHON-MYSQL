import mysql.connector


def connect_sql():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=8889,
        database='travel'

    )


    print(db)
    return db
