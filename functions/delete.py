import functions.mysqlconnected as mysqlconnected
import mysql.connector


def hapus_data_transaksi(id):
    try:
        db = mysqlconnected.connect_sql()
        cursor = db.cursor()
        print("Connected to MYSQL")

        delete = "DELETE FROM transaksi_travel WHERE id = %s"

        cursor.execute(delete, (id, ))
        db.commit()
        print("Hapus Data Sukses")

        cursor.close()

    except mysql.connector.Error as error:
        print("gagal terkoneksi ke tabel", error)
    finally:
        if (db):
            db.close()
            print("koneksi mysql Selesai")
