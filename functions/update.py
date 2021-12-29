import functions.mysqlconnected as mysqlconnected


def update_data(status, id):
    db = mysqlconnected.connect_sql()
    cursor = db.cursor()
    sql = "UPDATE tansaksi_travel SET status_pembayaran=%s WHERE id=%s"
    val = (status, id)
    cursor.execute(sql, val)

    db.commit()

    print("{} data diubah".format(cursor.rowcount))
