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
        print("Hapus Data Sukses")

        cursor.close()

    # error handling jika terjadi error
    except mysql_connection.mysql_error() as error:
        print("gagal terkoneksi ke tabel", error)
    finally:
        if (db):
            db.close()
            print("koneksi mysql Selesai")
