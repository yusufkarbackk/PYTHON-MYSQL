import mysql.connector

# fungsi untuk koneksi ke database


def connect_sql():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=8889,
        database='data_travel'

    )

    return db

# fungsi untuk mengambil error yang bisa terjadi


def mysql_error():
    return mysql.connector.Error


connect_sql()
