import sys
sys.path.append('/FIX PYTHON/implements')


print('''selamat datang di aplikasi peminjaman buku 
\n1. insert transaksi 
\n2.show transaksi 
\n3. update transaksi 
\n4.delete transaksi''')

# input sebagai pilihan user
pilihan_user = input('silahkan pilih aktifitas: ')

# cek menu apa yang dipilih user
if pilihan_user == '1':
    insert_transaksi()
elif pilihan_user == '2':
    # implements.show_data()
    pass
elif pilihan_user == '3':
    # implements.update_impl()
    pass
elif pilihan_user == '4':
    pass
    # implements.delete_impl()
