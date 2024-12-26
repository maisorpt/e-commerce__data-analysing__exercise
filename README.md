# Dashboard Analisis Penjualan dan Ulasan Produk

Proyek ini menganalisis penjualan produk, ulasan, dan berbagai atribut seperti harga dan kategori menggunakan visualisasi data. Dashboard ini memungkinkan pengguna untuk menjelajahi berbagai aspek penjualan dan ulasan produk, memberikan wawasan tentang bagaimana faktor-faktor ini saling terkait dan memengaruhi total penjualan.

## Daftar Isi

1. [Overview](#overview)
2. [Analisis Ulasan vs Penjualan](#analisis-ulasan-vs-penjualan)
3. [Penjualan Berdasarkan Kategori](#penjualan-berdasarkan-kategori)
4. [Analisis Harga vs Penjualan](#analisis-harga-vs-penjualan)
5. [Kesimpulan](#kesimpulan)

## Overview

Dashboard ini memberikan gambaran umum tentang dataset produk, termasuk statistik kunci seperti:

- Total penjualan untuk setiap produk.
- Rata-rata skor ulasan produk.
- Jumlah ulasan di setiap kategori produk.

Pengguna dapat menjelajahi data mentah dan statistik ringkas.

## Analisis Ulasan vs Penjualan

Bagian ini menjelajahi hubungan antara jumlah ulasan dan skor ulasan rata-rata di berbagai kategori produk. Kami menggunakan grafik sebar di mana:

- Sumbu x mewakili jumlah ulasan.
- Sumbu y mewakili rata-rata skor ulasan.
- Ukuran setiap titik mewakili total penjualan produk, dan warnanya mewakili jumlah ulasan.

Wawasan utama:
- Produk dengan jumlah ulasan lebih banyak cenderung memiliki variasi rating yang lebih besar.
- Kategori produk dengan ulasan lebih sedikit cenderung memiliki rating yang lebih tinggi dan lebih konsisten.

## Penjualan Berdasarkan Kategori

Pada bagian ini, kami menunjukkan 10 kategori produk teratas berdasarkan total penjualan. Diagram batang ini menggambarkan hubungan antara kategori produk dan total penjualan (dihitung sebagai `item_price * sold_count`).

Wawasan utama:
- Kategori tertentu, seperti "cool_stuff", menunjukkan penjualan yang jauh lebih tinggi meskipun harga produk tidak termasuk yang tertinggi.
- Analisis ini mengungkap kategori mana yang tampil paling baik berdasarkan total penjualan.

## Analisis Harga vs Penjualan

Bagian ini memvisualisasikan hubungan antara harga produk dan total penjualan (dalam jutaan). Grafik sebar menunjukkan:

- Sumbu x mewakili harga produk.
- Sumbu y mewakili total penjualan dalam juta.
- Ukuran titik menggambarkan jumlah ulasan, dan warna titik menggambarkan rata-rata skor ulasan.

Wawasan utama:
- Ada tren umum di mana produk dengan harga lebih tinggi cenderung memiliki penjualan total yang lebih tinggi.
- Namun, beberapa produk dengan harga lebih rendah juga dapat memiliki penjualan yang baik, mungkin karena faktor lain seperti rating dan ulasan pelanggan.

## Kesimpulan

Analisis ini memberikan beberapa temuan kunci:

1. **Jumlah Ulasan vs Skor Ulasan Rata-Rata**: Kategori dengan lebih banyak ulasan cenderung memiliki rentang rating yang lebih luas. Sebaliknya, kategori dengan lebih sedikit ulasan cenderung memiliki rating yang lebih tinggi dan konsisten.

2. **Faktor-faktor yang Mempengaruhi Total Penjualan**: Harga, jumlah ulasan, dan kategori produk memiliki pengaruh signifikan terhadap total penjualan. Beberapa kategori, seperti "cool_stuff", memiliki penjualan tinggi meskipun harga produk tidak terlalu tinggi.

3. **Kategori Produk dan Rating**: Kategori produk dengan lebih sedikit ulasan cenderung memiliki rating lebih tinggi, sedangkan kategori dengan lebih banyak ulasan menunjukkan variasi rating yang lebih besar.

## Persiapan dan Penggunaan

Untuk menjalankan dashboard secara lokal, ikuti langkah-langkah berikut:

1. Clone repository ini:
git clone https://github.com/username-anda/dashboard-analisis-penjualan.git


2. Install dependensi yang dibutuhkan:

3. Jalankan aplikasi Streamlit:
