import functions.delete as delete
import show_impl


def delete_impl():
    show_impl()

    id = int(input('masukan id transaksi: '))

    delete.hapus_data_transaksi(id)
