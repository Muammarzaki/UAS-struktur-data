import unittest

# Import semua fungsi dari program utama
from working_directory.working_file import (
    fitur_pengelolaan_data_produk,
    fitur_sistem_antrian_pelangan,
    fitur_simulasi_transaksi,
    fitur_laporan_penjualan,
    produk_data,
    antrian_data,
    transaksi_data,
    penjualan_data,
)

# Ambil fungsi untuk diuji
tambah_produk, cari_produk, urutkan_produk = fitur_pengelolaan_data_produk()
tambah_pelanggan, layani_pelanggan = fitur_sistem_antrian_pelangan()
simpan_transaksi, undo_transaksi = fitur_simulasi_transaksi()
update_penjualan, produk_terlaris, stok_kritis = fitur_laporan_penjualan()


class TestSistemManajemenToko(unittest.TestCase):
    def test_bentuk_data_produk(self):
        for produk in produk_data:
            # Periksa apakah setiap produk memiliki kunci yang sesuai
            self.assertIn("nama", produk)
            self.assertIn("stock", produk)
            self.assertIn("harga", produk)

            # Periksa tipe data dari setiap field
            self.assertIsInstance(produk["nama"], str)
            self.assertIsInstance(produk["stock"], int)
            self.assertIsInstance(produk["harga"], int)

    def test_bentuk_data_antrian(self):
        for pelanggan in antrian_data:
            # Setiap item dalam antrian harus berupa string (nama pelanggan)
            self.assertIsInstance(pelanggan, str)

    def test_bentuk_data_transaksi(self):
        for transaksi in transaksi_data:
            # Periksa apakah setiap transaksi memiliki kunci yang sesuai
            self.assertIn("nama_pelanggan", transaksi)
            self.assertIn("produk", transaksi)
            self.assertIn("jumlah", transaksi)

            # Periksa tipe data dari setiap field
            self.assertIsInstance(transaksi["nama_pelanggan"], str)
            self.assertIsInstance(transaksi["produk"], str)
            self.assertIsInstance(transaksi["jumlah"], int)

    def test_bentuk_data_penjualan(self):
        for nama_produk, jumlah_terjual in penjualan_data.items():
            # Periksa apakah kunci adalah string dan nilai adalah integer
            self.assertIsInstance(nama_produk, str)
            self.assertIsInstance(jumlah_terjual, int)

    #######################
    # Pengelolaan Produk #
    #######################
    def test_tambah_produk(self):
        tambah_produk("test_produk", 10, 5000)
        self.assertEqual(cari_produk("test_produk")["nama"], "test_produk")

        # Test duplikasi produk
        with self.assertRaises(ValueError):
            tambah_produk("test_produk", 20, 10000)

    def test_cari_produk(self):
        self.assertIsNotNone(cari_produk("indomie"))
        self.assertIsNone(cari_produk("tidak_ada"))

    def test_urutkan_produk(self):
        tambah_produk("z_produk", 15, 2000)
        urutkan_produk("nama")
        produk = [p["nama"] for p in produk_data]
        self.assertEqual(produk, sorted(produk))

        urutkan_produk("harga")
        harga = [p["harga"] for p in produk_data]
        self.assertEqual(harga, sorted(harga))

    ########################
    # Sistem Antrian Pelanggan #
    ########################
    def test_tambah_pelanggan(self):
        antrian_awal = len(antrian_data)
        tambah_pelanggan("test_pelanggan")
        self.assertEqual(len(antrian_data), antrian_awal + 1)

    def test_layani_pelanggan(self):
        tambah_pelanggan("test_pelanggan_1")
        pelanggan = layani_pelanggan()
        self.assertEqual(pelanggan, "test_pelanggan_1")

        # Test antrian kosong
        with self.assertRaises(ValueError):
            layani_pelanggan()

    ###################
    # Simulasi Transaksi #
    ###################
    def test_simpan_transaksi(self):
        transaksi_awal = len(transaksi_data)
        simpan_transaksi("pelanggan_test", "indomie", 3)
        self.assertEqual(len(transaksi_data), transaksi_awal + 1)
        self.assertEqual(transaksi_data[-1]["nama_pelanggan"], "pelanggan_test")

    def test_undo_transaksi(self):
        simpan_transaksi("pelanggan_undo", "indomie", 5)
        transaksi_terakhir = undo_transaksi()
        self.assertEqual(transaksi_terakhir["nama_pelanggan"], "pelanggan_undo")

    #################
    # Laporan Penjualan #
    #################
    def test_update_penjualan(self):
        update_penjualan("indomie", 5)
        self.assertEqual(penjualan_data["indomie"], 5)

        update_penjualan("indomie", 2)
        self.assertEqual(penjualan_data["indomie"], 7)

    def test_produk_terlaris(self):
        update_penjualan("produk_1", 10)
        update_penjualan("produk_2", 15)
        terlaris = produk_terlaris()
        self.assertEqual(terlaris, "produk_2")

    def test_stok_kritis(self):
        kritis = stok_kritis()
        self.assertTrue(len(kritis) <= 3)
        stok = [p["stock"] for p in kritis]
        self.assertEqual(stok, sorted(stok))


if __name__ == "__main__":
    unittest.main()
