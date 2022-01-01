import show
import update


def update_transaksi():
    # panggil fungsi show_impl untuk menampilkan data
    show.show_data()

    # input id pada transaksi yang status nya akan diubah
    id = int(input('masukan id transaksi: '))
    status = input('masukan status pembayaran: ')

    # panggil fungsi update
    update.update_data(status, id)
