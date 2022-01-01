import mysqlconnected as mysql


def show_data():
    # koneksi ke database
    db = mysql.connect_sql()
    cursor = db.cursor()

    # melakukan query read/show semua field
    sql = "SELECT * FROM transaksi_travel"
    cursor.execute(sql)

    # mengambil data yang berhasil di query
    results = cursor.fetchall()

    # menampilkan data
    print("Data Transaksi Travel :\n")
    for data in results:
        print("Id = ", data[0], )
        print("Name = ", data[1])
        print("Email  = ", data[2])
        print("Destinasi  = ", data[3])
        print("Tanggal Pesan  = ", data[4])
        print("Status Pembayaran  = ", data[5], "\n")


def search_data(input):
    db = mysql.connect_sql()
    cursor = db.cursor()
    sql = "SELECT * FROM transaksi_travel WHERE id LIKE %s OR nama LIKE %s OR destinasi LIKE %s OR status_pembayaran LIKE %s"
    val = ("%{}%".format(input), "%{}%".format(input),
           "%{}%".format(input), "%{}%".format(input))
    cursor.execute(sql, val)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print("Id = ", data[0], )
            print("Name = ", data[1])
            print("Email  = ", data[2])
            print("Destinasi  = ", data[3])
            print("Tanggal Pesan  = ", data[4])
            print("Status Pembayaran  = ", data[5], "\n")
