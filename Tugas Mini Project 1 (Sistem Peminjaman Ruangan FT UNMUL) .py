ruangan = ("C401", "C402", "C403", "C404", "C405", "C406", "C407", "C408") #Tuple buat menyediakan ruangan yang tersedia di FT UNMUL
peminjaman = [] #List untuk menambah/mengurangi data jadwal ruangan yang dipinjam


print("==========================================================")
print("====== Selamat Datang di Sistem Peminjaman Ruangan =======")
print("======================== FT UNMUL ========================")
print("==========================================================")
print("")
print("Mau ngapain nih hari ini?:")
print("1. Lihat Jadwal Ruangan yang Telah Dipinjam")
print("2. Tambah Peminjaman Ruangan")
print("3. Ubah Peminjaman Ruangan")
print("4. Batalkan Peminjaman Ruangan")
print("5. Keluar")

while True:

    pilihan = int(input("Pilih menu yang ingin dilakukan (1/2/3/4/5): "))

    #Proses Menu Pilihan 1
    if pilihan == 1:
        print(" ")
        print("=== Jadwal Peminjaman Ruangan ===")

        if len(peminjaman) == 0: #len disini berfungsi untuk menghitung jumlah item atau elemen yang ada di dalam list peminjaman. Jika peminjaman == 0 maka belum ada jadwal yang massuk
            print("Belum ada data ruangan yang dipinjam")
            print(" ")

        else:
            print("ID      Nama     Ruangan     Tanggal      Waktu")

        for data in peminjaman:
            print(data[0],"  ", data[1],"  ", data[2],"      ", data[3]," ", data[4])
            print("")

    #Proses Menu pIlihan 2
    elif pilihan == 2:
        print("Tambah Peminjaman Ruangan")

        while True:
            id_peminjaman = input("Masukkan ID peminjaman (Contoh: P001, P002, dst.): ")

            id_ditemukan = False

            for data in peminjaman:
                if data[0] == id_peminjaman:
                    id_ditemukan = True
                    break

            if id_ditemukan:
                print(f"ID '{id_peminjaman}' sudah digunakan, silahkan gunakan ID lain.")
            else:
                break

        nama_mahasiswa = input("Masukkan nama mahasiswa yang ingin meminjam ruangan: ")

        while True:
            kode_ruangan = input("Masukkan kode ruangan yang ingin dipinjam (Tersedia ruangan C401 - C408): ")

            if kode_ruangan not in ruangan:
                print(f"Ruangan '{kode_ruangan}' tidak tersedia, pilih ulang ruangan yang disediakan (C401 - C408)")
                continue

            tanggal = input("Masukkan tanggal peminjaman ruangan (Contoh: 12/09/2026): ")
            waktu = input("Masukkan waktu peminjaman ruangan (Contoh: 13:00): ")

            #Mengecek jadwalnya bentrok atau tidak
            jadwal_bentrok = False

            for data in peminjaman:
                if data[2] == kode_ruangan and data[3] == tanggal and data[4] == waktu:
                    jadwal_bentrok = True

            if jadwal_bentrok == True:
                print("Maaf, jadwal yang anda pilih sudah digunakan orang lain")
                print(" ")

            else:
                break

        data_baru = [id_peminjaman, nama_mahasiswa, kode_ruangan, tanggal, waktu]
        peminjaman.append(data_baru)
        print("Peminjaman ruangan telah berhasil dilakukan, silahkan ketik 1 jika ingin mengecek jadwal.")
        print(" ")

    #Proses Mengubah Jadwal Peminjaman Ruangan
    elif pilihan == 3:
        print("Ubah Peminjaman Ruangan")

        id_peminjaman = input("Masukkan ID peminjaman yang ingin diubah: ")

        id_ditemukan = False
        index_data = 0  #digunakan sebagai penanda posisi awal data dalam list.

        for data in peminjaman:
            if data[0] == id_peminjaman:
                id_ditemukan = True
                break

            index_data = index_data + 1 #Digunakan untuk menambah posisi tersebut setiap kali data yang diperiksa belum sesuai, sampai ID yang dicari ditemukan oleh perulangan for
        
        if id_ditemukan:
            print("Data peminjaman ditemukan.")

            while True:
        
                kode_ruangan_baru = input("Masukkan kode ruangan yang baru (C401 - C408): ")

                if kode_ruangan_baru not in ruangan:
                    print("Ruangan tidak tersedia, silahkan pilih C401 - C408.")
                    continue

                tanggal_baru = input("Masukkan tanggal peminjaman yang baru (Contoh: 12/09/2026): ")
                waktu_baru = input("Masukkan waktu peminjaman yang baru (Contoh: 13:00): ")

                #Mengecek apakah jadwalnya bentrok atau tidak
                jadwal_bentrok = False

                for data in peminjaman:
                    if data[0] != id_peminjaman:
                        if data[2] == kode_ruangan_baru and data[3] == tanggal_baru and data[4] == waktu_baru:
                            jadwal_bentrok = True
                            break

                if jadwal_bentrok == True:
                    print("Maaf, jadwal yang baru sudah digunakan orang lain.")
                    print(" ")
                    continue

                else:
                    peminjaman[index_data][2] = kode_ruangan_baru
                    peminjaman[index_data][3] = tanggal_baru
                    peminjaman[index_data][4] = waktu_baru

                print("Data peminjaman berhasil diubah, silahkan ketik 1 jika ingin mengecek.")
                print(" ")
                break

        else:
            print(f"ID '{id_peminjaman}' tidak ditemukan.")
            

    #Proses Pembatalan Jadwal Peminjaman Ruangan
    elif pilihan == 4:
        print("Batalkan Peminjaman Ruangan")

        id_peminjaman = input("Masukkan ID peminjaman yang ingin batalkan: ")
        
        id_ditemukan = False
        index_data = 0
        
        for data in peminjaman:
            if data[0] == id_peminjaman:
                id_ditemukan = True
                break

            index_data = index_data + 1

        if id_ditemukan:
            peminjaman.pop(index_data)
            print("Peminjaman berhasil dibatalkan.")
            print(" ")

        else:
            print(f"ID '{id_peminjaman}' tidak ditemukan.")
        
    #Proses jika kita sudah selesai mengakses sistem peminjaman ruangan FT UNMUL
    elif pilihan == 5:
        print("Sistem peminjaman ruangan telah selesai")
        break

    else:
        print("pilihan menu hanya tersedia 1/2/3/4/5, silahkan masukkan ulang pilihan menu!")
