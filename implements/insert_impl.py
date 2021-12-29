import functions.insert as insert
import datetime


def insert_impl():
    # input yang dibutuhkan untuk insert data
    nama = input('masukan nama: ')
    email = int(input('masukan nim: '))
    destinasi = input('masukan prodi: ')
    tanggal_pesan = input('masukan judul buku: ')

    #panggil fungsi insert_transaksi
    insert.insert_transaksi(nama, email, destinasi, tanggal_pesan)
