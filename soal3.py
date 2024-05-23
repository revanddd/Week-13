def baca_kata_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi = file.read().lower()
            return set(isi.split())
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan atau tidak bisa dibaca.")
        return set()

nama_file1 = input("Masukkan nama file pertama: ")
nama_file2 = input("Masukkan nama file kedua: ")

kata_set1 = baca_kata_dari_file(nama_file1)
kata_set2 = baca_kata_dari_file(nama_file2)

kata_kedua_file = kata_set1 & kata_set2

if kata_kedua_file:
    print("Kata-kata yang muncul di kedua file:")
    print(kata_kedua_file)
else:
    print("Tidak ada kata yang muncul di kedua file.")