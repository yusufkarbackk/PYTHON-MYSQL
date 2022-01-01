import mysqlconnected as mysqlconnected


def update_data(status, id):
    # koneksi ke database
    db = mysqlconnected.connect_sql()
    cursor = db.cursor()

    # melakukan query update untuk field status_pembayaran
    sql = "UPDATE transaksi_travel SET status_pembayaran=%s WHERE id=%s"
    val = (status, id)
    cursor.execute(sql, val)

    db.commit()

    if cursor.rowcount <= 0:
        print('maaf id yang dimasukan salah')
        print("{} data diubah".format(cursor.rowcount))
    else:
        print('Update sukses')
        print("{} data diubah".format(cursor.rowcount))
