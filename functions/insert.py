import datetime
from mysqlconnected import connect_sql


def insert_transaksi(nama, email, destinasi, tanggal_pesan):

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


insert_transaksi('yusuf', 'yusuf@email.com', 'bali', datetime.datetime.now())


'selasa, 28 desember => membuat tabel mahasiswa dan fungsi CRUD untuk tabel mahasiswa'
