import mysqlconnected as mysql_connection


def delete_data(id):
    try:
        # koneksi ke database
        db = mysql_connection.connect_sql()
        cursor = db.cursor()
        print("Connected to MYSQL")

        # menjalankan query delete
        delete = "DELETE FROM transaksi_travel WHERE id = %s"

        cursor.execute(delete, (id, ))
        db.commit()
        if cursor.rowcount <= 0:
            print('maaf id yang dimasukan salah')
            print("{} data diubah".format(cursor.rowcount))
        else:
            print('Hapus data sukses')
            print("{} data diubah".format(cursor.rowcount))

        cursor.close()

    # error handling jika terjadi error
    except mysql_connection.mysql_error() as error:
        print("gagal terkoneksi ke tabel", error)
    finally:
        if (db):
            db.close()
            print("koneksi mysql Selesai")
