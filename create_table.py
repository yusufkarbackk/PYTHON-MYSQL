import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="daftar_buku"
)

cursor = db.cursor()
sql = """CREATE TABLE mahasiswa (
  mahasiswa_id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255),
  nim INT(20),
  prodi Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")