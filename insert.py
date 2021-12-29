from mysqlconnected import connect_sql


def insert_data(nama, email, destinasi, tanggal_pesan):

    # koneksi ke database
    db = connect_sql()
    cursor = db.cursor()

    # melakukan query insert
    sql = "INSERT INTO transaksi_travel (nama, email, destinasi, tanggal_pesan) VALUES (%s, %s, %s,%s)"
    val = (nama, email, destinasi, tanggal_pesan)

    cursor.execute(sql, val)

    db.commit()
    print("{} data ditambahkan".format(cursor.rowcount))

    cursor.close()


'selasa, 28 desember => membuat tabel mahasiswa dan fungsi CRUD untuk tabel mahasiswa'
