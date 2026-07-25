---
title: "🩹 Motivation"
---

<div data-theme-preset="sapphire">


### The Two-Source Problem

Pola yang lazim: README di root, lalu situs docs terpisah. Perubahan endpoint API dicatat
di salah satunya saja, dan enam bulan kemudian tak ada yang tahu mana yang benar. Di sini
tidak ada berkas kedua — folder `documentation/src/content/docs/` **dihapus dan dibuat
ulang** setiap build, jadi ia tak mungkin menyimpang dari README.

### Setup Costs More Than Writing

Memasang Astro, memilih tema, mengonfigurasi sidebar, dan menyetel deploy sering memakan
waktu lebih lama daripada menulis dokumentasinya. Untuk proyek kecil, kalkulasinya jelas
kalah — jadi dokumentasi tak pernah ada. Template ini sudah membawa semuanya; kontribusi
kamu cukup satu berkas Markdown.

### Sidebar and Routing Busywork

Menambah halaman biasanya berarti: buat berkas, isi frontmatter, daftarkan di konfigurasi
sidebar, tentukan urutan. Di sini menambah halaman = **menulis satu heading `##`**.
Urutannya mengikuti urutan di README.

### The README Must Still Read Well on GitHub

README yang ditulis khusus untuk generator biasanya jadi aneh saat dilihat di GitHub.
Karena itu template ini pakai Markdown biasa, tanpa sintaks eksklusif — dan menyediakan
blok `DELETE_IN_DOCS` untuk bagian yang hanya relevan di GitHub (misalnya tombol
"buka situs docs" di atas, yang tidak ikut tampil di situsnya).

---

</div>