# Mini_Project_1_Mirza Asra Ataya

Nama: Mirza Asra Ataya 

NIM: 2609116043

Kelas B 26'

# 1. Gambar Flowchart
<img width="1159" height="3382" alt="Flowchart Mini Project 1 DDP Mirza drawio" src="https://github.com/user-attachments/assets/6e3770a4-f026-4830-a853-3f12569c85e4" />


# 2. Penjelasan Program
Di Mini Project 1 ini saya membuat sebuah sistem peminjaman ruangan FT UNMUL, saya terinspirasi membuat sistem ini dari E-Room. Pada sistem yang saya buat memungkinkan user untuk 1) melihat jadwal ruangan yang telah dipinjam (READ), 2) menambah ruangan dan jadwal yang ingin dipinjam (CREATE), 3) mengubah ruangan dan jadwal yang telah dipinjam (UPDATE), serta 4) Membatalkan (menghapus) data ruangan dan jadwal yang telah dipinjam sebelumnya (DELETE). Alasan saya menaruh READ di bagian awal karena biasanya saat kita ingin meminjam suatu ruangan, kita akan terlebih dahulu melihat ruangan dan jadwal yang sudah diambil sebelumnya untuk menghindari bentrok. Tapi, walau begitu sistem yang saya buat ini tetap bisa mendeteksi jika user memasukkan ruangan dan jadwal yang telah diambil sebelumnya, sehingga user akan disuruh untuk memilih ulang ruangan dan jadwal yang tersedia. Berikut adalah penjelasan ketika user memilih masing-masing menu di sistem peminjaman ruangan FT UNMUL:

1) Penjelasan ketika user memilih menu 1 (Lihat Jadwal Ruangan yang Telah Dipinjam
   <img width="491" height="197" alt="Screenshot 2026-09-12 170533" src="https://github.com/user-attachments/assets/abfd9fd8-f43e-41bb-98d1-620b2e93da72" />
   
Jadi, menu pertama ini adalah fitur melihat jadwal ruangan yang sudah dipinjam sebelumnya.

2) Penjelasan ketika user memilih menu 2 (Tambah Peminjaman Ruangan)
   <img width="480" height="330" alt="gambar" src="https://github.com/user-attachments/assets/eff12326-e9d0-4b9f-a5aa-4ab409d6ce36" />
   
Menu kedua ini adalah fitur untuk menambah ruangan yang mau dipinjam, pada fitur ini terdapat perulangan while True (sebagai perulangan jika ID telah digunakan dan kalau ada jadwal yang bentrok), for (untuk mengecek setiap data yang ada di data list peminjaman), dan conditional sentence if else. Sistem bekerja dimulai dengan menginput ID, jika ID sudah pernah dipakai sebelumnya, maka user akan disuruh untuk input ulang ID yang berbeda. Jika ID belum pernah digunakan, maka user akan lanjut untuk menginput nama, kode ruangan, tanggal, dan waktu peminjaman ruangan. Setelah user menginput data data tadi, sistem akan memeriksa, apakah jadwalnya bentrok atau tidak. jika bentrok, maka outputnya akan seperti gambar di bawah ini.
<img width="458" height="117" alt="Screenshot 2026-09-12 172109" src="https://github.com/user-attachments/assets/5c5fb93b-4a63-4d39-bbfb-5246271bc244" />

Kemudian data tersebut akan masuk ke dalam list peminjaman dengan menggunakan perintah .append

3) Penjelasan ketika user memilih menu 3 (Ubah Peminjaman Ruangan)

Menu ketiga ini adalah fitur untuk mengubah ruangan yang mau dipinjam, mekanismenya kurang lebih sama seperti menu kedua hanya saja karena menu ketiga ini untuk mengubah jadi ada sedikit yang membedakan, yaitu adanya baris index_data = 0 yang fungsinya untuk menentukan posisi awal data dalam list dan index_data = index_data + 1 yang fungisinya untuk menambah posisi tersebut setiap kali data yang diperiksa belum sesuai, sampai ID yang dicari ditemukan dengan perulangan for. Dibawah ini adalah output ketika sebelum dan sesudah ada perubahan jadwal.

<img width="287" height="111" alt="Screenshot 2026-09-12 173712" src="https://github.com/user-attachments/assets/5c9c7285-aa7a-4aab-aa53-06d755cb88cc" /> 
Sebelum Perubahan Jadwal

<img width="411" height="260" alt="gambar" src="https://github.com/user-attachments/assets/c446995c-6dc7-4cb3-91a2-c0d4a34f0a40" /> 
Setelah perubahan jadwal


4) Penjelasan ketika user memilih menu 4 (Batalkan Peminjaman Ruangan)
<img width="372" height="225" alt="Screenshot 2026-09-12 161733" src="https://github.com/user-attachments/assets/51e450ca-8ff2-4cf2-92f6-b7ce8868ecee" />

Menu keempat ini adalah fitur untuk membatalkan (menghapus ruangan yang telah dipinjam). Pada menu ini saya menggunakan perintah .pop untuk menghapus data yang ada di dalam list peminjaman.

5) Penjelasan ketika user memilih menu 5 (Keluar)

Menu kelima atau yang terakhir ini akan mengakhiri perulangan while True utama dalam sistem yang kemudian user akan keluar dari sistem (SELESAI).




   


