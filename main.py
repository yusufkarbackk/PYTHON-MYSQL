import implements.insert_impl as insert
import implements.show_impl as show
import implements.delete_impl as delete
import implements.update_impl as update

print('''selamat datang di aplikasi peminjaman buku 
\n1. insert transaksi 
\n2.show transaksi 
\n3. update transaksi 
\n4.delete transaksi''')

pilihan_user = input('silahkan pilih aktifitas: ')

if pilihan_user == '1':
    insert.insert_pinjaman()
elif pilihan_user == '2':
    show.show_data()
elif pilihan_user == '3':
    update.update_impl()
elif pilihan_user == '4':
    delete.delete_impl()
