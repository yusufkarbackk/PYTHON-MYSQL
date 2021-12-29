import functions.mysqlconnected as mysql


def show_data():
  #koneksi ke database
  db = mysql.connect_sql()
  cursor = db.cursor()

  #melakukan query read/show semua field
  sql = "SELECT * FROM transaksi_travel"
  cursor.execute(sql)

  #mengambil data yang berhasil di query
  results = cursor.fetchall()

  #menampilkan data
  print("Data Transaksi Travel :\n")
  for data in results:
    print(data)
