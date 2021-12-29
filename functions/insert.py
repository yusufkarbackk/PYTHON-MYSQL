import functions.mysqlconnected as mysqlconnected


def insert_mahasiswa(nama, email, destinasi, tanggal_pesan, status, pembayaran):

    db = mysqlconnected.connect_sql()
    cursor = db.cursor()

    sql = "INSERT INTO transaksi_travel (nama, email, destinasi, tanggal_pesan, status_pembayaran) VALUES (%s, %s, %s,%s, %s)"
    val = (nama, email, destinasi, tanggal_pesan, status, pembayaran)

    cursor.execute(sql, val)

    db.commit()

    print("{} data ditambahkan".format(cursor.rowcount))


'selasa, 28 desember => membuat tabel mahasiswa dan fungsi CRUD untuk tabel mahasiswa'
