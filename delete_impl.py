import show_impl
import delete


def delete_transaksi():
    # panggil function show_impl() untuk menampilkan data
    show_impl.show_transaksi()

    # input id yang akan di delete
    id = int(input('masukan id transaksi: '))

    # panggil fungsi hapus_data_transaksi dari folder functions
    delete.delete_data(id)
