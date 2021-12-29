import datetime
import insert


def insert_transaksi():
    # input yang dibutuhkan untuk insert data
    nama = input('masukan nama: ')
    email = (input('masukan email: '))
    destinasi = input('masukan destinasi: ')
    tanggal_pesan = datetime.datetime.now()

    # panggil fungsi insert_transaksi
    insert.insert_data(nama, email, destinasi, tanggal_pesan)
