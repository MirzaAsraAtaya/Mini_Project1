buku = ("Tentang Kamu", "Atomic Habits",  "Filosofi Teras", "5 Cm", "Laut Bercerita", "Seporsi Mie Ayam", "Hujan", "Sisi Tergelap Surga", "3726 MDPL", "Tutorial Jadi Engineer Sukses")
pinjaman = []

print("==========Selamat datang di Perpustakaan FT!==========")
print("============Mau minjam buku apa hari ini?=============")
print(" ")
print("Berikut adalah daftar buku yang tersedia di perpustakaan FT:")
for i, judul in enumerate(buku, start=1):    
    print(f"{i}. {judul}") #f disebut dengan f-string yang digunakan untuk memasukkan nilai variabel ke dalam teks.

while True:

    nama_buku = input("Masukkan nama buku (perhatikan huruf besar kecilnya yaa) yang ingin dipinjam dan ketik 'selesai' jika sudah selesai: ")

    if nama_buku in buku:
        pinjaman.append(nama_buku)
        print(f"Buku '{nama_buku}' berhasil ditambahkan ke daftar pinjaman.")

    if nama_buku == "selesai":
        break

    if nama_buku not in buku:
        print(f"Buku '{nama_buku}' tidak tersedia di perpustakaan FT. Silakan pilih buku lain yap!.") 

print("Ini adalah list buku yang kamu pinjam saat ini: ")
for i, pinjeman in enumerate(pinjaman, start=1):
    print(f"{i}. {pinjeman}")

hapus = input("Sebelum menyelesaikan peminjaman, apakah ada salah satu buku yang mau kamu hapus dari list? (ya/tidak) ")

if hapus == "ya":
    buku_dihapus = input("Buku apa yang mau dihapus dari list peminjaman? ")

    if buku_dihapus in pinjaman:
       pinjaman.remove(buku_dihapus)
       print(f'"{buku_dihapus}" berhasil dihapus dari daftar pinjaman.')

    else:
        print("Buku tersebut tidak ada dalam daftar pinjaman.")

else:
    print("Okee tidak ada yang mau dihapus, berarti kamu mau minjam semua yap")

print("Ini adalah list buku yang kamu pinjam dari Perpustaakan FT: ")
for i, list_pinjaman in enumerate(pinjaman, start=1):
    print(f"{i}. {list_pinjaman}")

print(" ")
print("=======Selamat Membaca dan Jangan Lupa Mengembalikannya!======")





