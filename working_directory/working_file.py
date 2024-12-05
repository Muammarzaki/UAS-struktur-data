"""
nama:
nim:
unit: unit-hari
dosen:
waktu pengerjaan:
"""

##################DATA GLOBAL#######################
produk_data = [

]
antrian_data = []
transaksi_data = []
penjualan_data = {}


####################################################
def fitur_pengelolaan_data_produk():
    produk = []

    def tambah_produk(nama, stok, harga):
        pass

    def cari_produk(nama_produk):
        return produk[0]

    def urutkan_produk(sort_berdasarkan):
        pass

    return tambah_produk, cari_produk, urutkan_produk


tambah_produk, cari_produk, urutkan_produk = fitur_pengelolaan_data_produk()


def fitur_sistem_antrian_pelangan():
    antrian = antrian_data

    def tambah_pelanggan(nama):
        return antrian

    def layani_pelanggan():
        return pelanggan

    return tambah_pelanggan, layani_pelanggan


tambah_pelanggan, layani_pelanggan = fitur_sistem_antrian_pelangan()


def fitur_simulasi_transaksi():
    transaksi = transaksi_data

    def simpan_transaksi(nama_pelanggan, nama_produk, jumlah) -> list:
        return transaksi

    def undo_transaksi() -> dict:
        return transaksi[0]

    return simpan_transaksi, undo_transaksi


simpan_transaksi, undo_transaksi = fitur_simulasi_transaksi()


def fitur_laporan_penjualan():
    def update_penjualan(nama_produk, jumlah):
        pass

    def produk_terlaris():
        return penjualan_data[0]

    def stok_kritis():
        return produk_data[:3]  # Top 3 lowest stock

    return update_penjualan, produk_terlaris, stok_kritis


update_penjualan, produk_terlaris, stok_kritis = fitur_laporan_penjualan()


####################################################

def main():
    global pelanggan
    while True:
        print("\n### Sistem Manajemen Toko ###")
        print("1. Pengelolaan Data Produk")
        print("2. Sistem Antrian Pelanggan")
        print("3. Simulasi Transaksi")
        print("4. Laporan Penjualan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            print("\n-- Pengelolaan Data Produk --")
            print("1. Tambah Produk")
            print("2. Cari Produk")
            print("3. Urutkan Produk")
            sub_pilihan = input("Pilih opsi (1-3): ")

            if sub_pilihan == "1":
                nama = input("Nama produk: ")
                stok = int(input("Stok produk: "))
                harga = int(input("Harga produk: "))
                tambah_produk(nama, stok, harga)
                print(f"Produk {nama} berhasil ditambahkan.")
            elif sub_pilihan == "2":
                nama = input("Nama produk yang dicari: ")
                hasil = cari_produk(nama)
                print("Hasil pencarian:", hasil if hasil else "Produk tidak ditemukan.")
            elif sub_pilihan == "3":
                sort_by = input("Urutkan berdasarkan (nama/stock/harga): ")
                urutkan_produk(sort_by)
                print("Produk setelah diurutkan:", produk_data)
            else:
                print("Opsi tidak valid.")

        elif pilihan == "2":
            print("\n-- Sistem Antrian Pelanggan --")
            print("1. Tambah Pelanggan ke Antrian")
            print("2. Layani Pelanggan")
            sub_pilihan = input("Pilih opsi (1-2): ")

            if sub_pilihan == "1":
                nama = input("Nama pelanggan: ")
                tambah_pelanggan(nama)
                print(f"Pelanggan {nama} berhasil ditambahkan ke antrian.")
            elif sub_pilihan == "2":
                pelanggan = layani_pelanggan()
                print(f"" if pelanggan else "Tidak ada pelanggan dalam antrian.")
            else:
                print("Opsi tidak valid.")

        elif pilihan == "3":
            print("\n-- Simulasi Transaksi --")
            print("1. Simpan Transaksi")
            print("2. Undo Transaksi Terakhir")
            sub_pilihan = input("Pilih opsi (1-2): ")

            if sub_pilihan == "1":
                try:
                    nama_pelanggan = pelanggan
                    print(f"Pelanggan saat ini :{nama_pelanggan}")
                    nama_produk = input("Nama produk: ")
                    if cari_produk(nama_produk) is None:
                        raise ValueError("Nama produk tidak terdaftar")
                    jumlah = int(input("Jumlah: "))
                    simpan_transaksi(nama_pelanggan, nama_produk, jumlah)
                    update_penjualan(nama_produk, jumlah)
                    print(f"Transaksi pelanggan {nama_pelanggan} berhasil disimpan.")
                except NameError:
                    print("Tidak ada pelanggan yang siap di layani")
                except ValueError as e:
                    print(e)

            elif sub_pilihan == "2":
                transaksi = undo_transaksi()
                print("Transaksi terakhir berhasil di-undo:",
                      transaksi if transaksi else "Tidak ada transaksi untuk di-undo.")
            else:
                print("Opsi tidak valid.")

        elif pilihan == "4":
            print("\n-- Laporan Penjualan --")
            print("1. Produk Terlaris")
            print("2. Stok Kritis")
            sub_pilihan = input("Pilih opsi (1-2): ")

            if sub_pilihan == "1":
                terlaris = produk_terlaris()
                print("Produk terlaris:", terlaris if terlaris else "Belum ada penjualan.")
            elif sub_pilihan == "2":
                kritis = stok_kritis()
                print("Produk dengan stok kritis:", kritis)
            else:
                print("Opsi tidak valid.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan Sistem Manajemen Toko!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == '__main__':
    main()
