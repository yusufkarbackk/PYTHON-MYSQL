import functions.mysqlconnected as mysql


def show_data():
  db = mysql.connect_sql()
  cursor = db.cursor()

  sql = "SELECT * FROM transaksi_travel"
  cursor.execute(sql)

  results = cursor.fetchall()

  print("Data Transaksi Travel :\n")
  for data in results:
    print(data)
