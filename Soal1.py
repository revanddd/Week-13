n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

print("Data Aplikasi per Kategori:", data_aplikasi)

daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print("Daftar Aplikasi (setiap kategori):", daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print("Aplikasi yang muncul di semua kategori:", hasil)

aplikasi_hanya_di_satu_kategori = set()
semua_aplikasi = set()
aplikasi_lebih_dari_satu_kategori = set()

for aplikasi_set in daftar_aplikasi_list:
    for aplikasi in aplikasi_set:
        if aplikasi in semua_aplikasi:
            aplikasi_lebih_dari_satu_kategori.add(aplikasi)
        semua_aplikasi.add(aplikasi)

for aplikasi_set in daftar_aplikasi_list:
    aplikasi_hanya_di_satu_kategori.update(aplikasi_set - aplikasi_lebih_dari_satu_kategori)

print("Aplikasi yang hanya muncul di satu kategori:", aplikasi_hanya_di_satu_kategori)

from collections import Counter

counter = Counter()
for aplikasi_set in daftar_aplikasi_list:
    counter.update(aplikasi_set)

aplikasi_di_dua_kategori = {app for app, count in counter.items() if count == 2}

print("Aplikasi yang muncul tepat di dua kategori:", aplikasi_di_dua_kategori)