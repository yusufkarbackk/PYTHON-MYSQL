import insert_impl
import show_impl
import update_impl
import delete_impl
import os


while(True):
    print('''selamat datang di aplikasi booking travel 
    \n1.insert transaksi 
    \n2.show transaksi 
    \n3.update transaksi 
    \n4.delete transaksi
    \n5.exit''')


# input sebagai pilihan user
    pilihan_user = input('silahkan pilih aktifitas: ')
    os.system('clear')

# cek menu apa yang dipilih user
    if pilihan_user == '1':
        insert_impl.insert_transaksi()
    elif pilihan_user == '2':
        show_impl.show_transaksi()
    elif pilihan_user == '3':
        update_impl.update_transaksi()
    elif pilihan_user == '4':
        delete_impl.delete_transaksi()
    elif pilihan_user == '5':
        break
    else:
        print('Maaf menu tidak ditemukan')
