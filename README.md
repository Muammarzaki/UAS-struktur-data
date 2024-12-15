## Deskripsi Soal

---

### **1. `createAListsTest`**

**Deskripsi:**
Selesaikan metode `createAListsTest` untuk mengembalikan sebuah list yang berisi 10 sublist. Setiap sublist harus memiliki 2 elemen string, di mana kedua elemen tersebut berbeda dan unik di seluruh list.

**Nilai Uji:**

- Pastikan list memiliki ukuran 10.
- Pastikan setiap elemen adalah sublist dengan 3 elemen string.
- Pastikan nilai dalam sublist unik di seluruh list.

---

### **2. `sortTest`**

**Deskripsi:**
Selesaikan metode `sortTest` untuk mengurutkan list of list berdasarkan elemen kedua pada sublist secara alfabetis.

**Bentuk Data yang Akan Diurutkan:**
```java
List<List<String>> dataBiodata = List.of(
    List.of("udin", "petani"),
    List.of("saiful", "guru"),
    List.of("amir", "pemancing"),
    List.of("budi", "dokter"),
    List.of("andika", "insinyur"),
    List.of("siti", "perawat"),
    List.of("rahma", "pengusaha"),
    List.of("ferdi", "programmer"),
    List.of("lisa", "desainer"),
    List.of("andi", "pengacara"),
    List.of("nina", "dosen"),
    List.of("yusuf", "sopir"),
    List.of("hadi", "koki"),
    List.of("rani", "penulis"),
    List.of("fitri", "jurnalis"),
    List.of("toni", "arsitek"),
    List.of("fajar", "tukang kayu"),
    List.of("dewi", "seniman"),
    List.of("agung", "musisi"),
    List.of("sari", "penjahit")
);
```

**Nilai Uji:**

- Pastikan elemen dalam list diurutkan berdasarkan elemen kedua pada sublist secara alfabetis.
- Pastikan ukuran list tetap sama setelah diurutkan.

---

### **3. `stackTest`**

**Deskripsi:**
Selesaikan metode `stackTest` untuk menerima sebuah string dan mengembalikannya dalam kondisi terbalik menggunakan konsep stack.

**Contoh Input:**

```java
String data = "stack";
```

**Contoh Output:**

```java
"kcats"
```

**Nilai Uji:**

- Pastikan string terbalik dengan benar.
- Gunakan stack untuk implementasi.

---

### **4. `queueTest`**

**Deskripsi:**
Selesaikan metode `queueTest` yang menerima sebuah list angka yang merepresentasikan waktu layanan pelanggan di dua kasir. Metode harus mengembalikan sebuah list dengan dua elemen yang merepresentasikan waktu total layanan di setiap kasir.

**Contoh Input:**

```java
List<Integer> waktuPelanggan = List.of(5, 3, 8, 2, 6);
```

**Proses:**

- Pelanggan pertama (5 detik) -> Kasir 1.
- Pelanggan kedua (3 detik) -> Kasir 2.
- Pelanggan ketiga (8 detik) -> Kasir 2 (karena Kasir 2 selesai lebih cepat).
- Pelanggan keempat (2 detik) -> Kasir 1, dst.

**Contoh Output:**

```java
List<Integer> hasil = List.of(14, 10);
```

**Nilai Uji:**

- Pastikan waktu total layanan di kedua kasir dihitung dengan benar.
- Kasir yang selesai lebih dulu melayani pelanggan berikutnya.

---

## Validasi

Untuk menjalankan validasi pada kode Anda, gunakan perintah berikut:

```shell
mvn test
```

