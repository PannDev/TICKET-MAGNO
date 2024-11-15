# Ticket QR Generator dan XY Click Tracker

Repositori ini berisi dua skrip Python untuk melacak klik mouse pada gambar (`cekXY.py`) dan menghasilkan gambar tiket yang dipersonalisasi dengan kode QR (`gambar.py`).

## Daftar Isi
- [Deskripsi](#deskripsi)
- [Dependensi](#dependensi)
- [Pengaturan](#pengaturan)
- [Penggunaan](#penggunaan)
  - [cekXY.py](#cekxypy)
  - [gambar.py](#gambarpng)
- [Mengatasi Error Umum](#mengatasi-error-umum)
- [Lisensi](#lisensi)

## Deskripsi

### cekXY.py
`cekXY.py` digunakan untuk melacak pergerakan dan klik mouse pada gambar. Skrip ini mencetak koordinat mouse saat bergerak dan mencatat koordinat klik beserta timestamp (tanggal dan waktu) ke dalam file teks (`XY/xy.txt`).

### gambar.py
`gambar.py` digunakan untuk menghasilkan gambar tiket yang dipersonalisasi dengan menambahkan kode QR dan kode unik (baik acak atau berurutan) ke gambar template. Skrip ini juga mendukung penambahan nama dari daftar ke gambar tiket dan dapat menyimpan gambar yang dihasilkan ke folder output yang ditentukan.

## Dependensi

Kedua skrip ini membutuhkan paket Python berikut:
- `opencv-python` (cv2)
- `Pillow` (PIL)
- `datetime`

Untuk menginstal dependensi yang dibutuhkan, jalankan perintah berikut:

```bash
pip install opencv-python pillow

```
### Text README.md, AI Generated, males ngetik hehehe
