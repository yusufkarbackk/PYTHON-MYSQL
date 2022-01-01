import show


def show_transaksi():
    # panggil fungsi show_data dari file show di folder functions
    user_input = input(
        'Masukan keyword yang ingin dicari (tekan enter jika ingin show seluruh data): ')

    if len(user_input) <= 0:
        show.show_data()
    else:
        show.search_data(user_input)
