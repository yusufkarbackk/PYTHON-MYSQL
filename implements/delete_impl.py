import functions.delete as delete
import show_impl


def delete_impl():
    # panggil function show_impl() untuk menampilkan data
    show_impl()

    # input id yang akan di delete
    id = int(input('masukan id transaksi: '))

    # panggil fungsi hapus_data_transaksi dari folder functions
    delete.hapus_data_transaksi(id)
