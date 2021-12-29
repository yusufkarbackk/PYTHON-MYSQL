import functions.insert as insert
import datetime


def insert_impl():
    nama = input('masukan nama: ')
    nim = int(input('masukan nim: '))
    prodi = input('masukan prodi: ')
    nama_buku = input('masukan judul buku: ')
    tanggal_pinjam = datetime.datetime.now()

    insert.insert_mahasiswa(nama, nim, prodi, nama_buku, tanggal_pinjam)
