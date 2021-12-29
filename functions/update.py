import functions.mysqlconnected as mysqlconnected


def update_data(status, id):
    #koneksi ke database
    db = mysqlconnected.connect_sql()
    cursor = db.cursor()

    #melakukan query update untuk field status_pembayaran
    sql = "UPDATE transaksi_travel SET status_pembayaran=%s WHERE id=%s"
    val = (status, id)
    cursor.execute(sql, val)

    db.commit()

    print("{} data diubah".format(cursor.rowcount))
