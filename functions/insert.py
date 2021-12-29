import functions.mysqlconnected as mysqlconnected


def insert_transaksi(nama, email, destinasi, tanggal_pesan):

    #koneksi ke database
    db = mysqlconnected.connect_sql()
    cursor = db.cursor()

    #melakukan query insert
    sql = "INSERT INTO transaksi_travel (nama, email, destinasi, tanggal_pesan) VALUES (%s, %s, %s,%s)"
    val = (nama, email, destinasi, tanggal_pesan)

    cursor.execute(sql, val)

    db.commit()
    cursor.close()

    print("{} data ditambahkan".format(cursor.rowcount))


'selasa, 28 desember => membuat tabel mahasiswa dan fungsi CRUD untuk tabel mahasiswa'
