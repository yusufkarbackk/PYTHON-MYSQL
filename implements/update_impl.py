import functions.update as update
import show_impl


def update_impl():
    show_impl()

    id = int(input('masukan id transaksi: '))
    status = input('masukan status pembayaran: ')

    update.update_data(status, id)
