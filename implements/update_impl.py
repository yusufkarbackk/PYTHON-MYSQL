import functions.update as update
import show_impl


def update_impl():
    #panggil fungsi show_impl untuk menampilkan data
    show_impl()

    #input id pada transaksi yang status nya akan diubah
    id = int(input('masukan id transaksi: '))
    status = input('masukan status pembayaran: ')

    #panggil fungsi update
    update.update_data(status, id)
