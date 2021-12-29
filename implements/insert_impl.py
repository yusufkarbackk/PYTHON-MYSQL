import datetime


def insert_transaksi():
    # input yang dibutuhkan untuk insert data
    nama = input('masukan nama: ')
    email = (input('masukan email: '))
    destinasi = input('masukan prodi: ')
    tanggal_pesan = datetime.datetime.now()

    # panggil fungsi insert_transaksi
    insert_transaksi(nama, email, destinasi, tanggal_pesan)
insert_transaksi()