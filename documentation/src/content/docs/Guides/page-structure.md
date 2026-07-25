---
title: "Page Structure"
---

<div data-theme-preset="sapphire">


Aturannya sedikit, dan semuanya berlaku pada Markdown biasa.

### Title and Tagline Are Required

Heading `#` pertama menjadi **judul situs** dan judul halaman depan. Blockquote (`>`)
pertama menjadi **deskripsi situs** — dipakai sebagai meta description sekaligus subjudul
halaman depan. Keduanya dibaca dua kali: oleh skrip Python untuk halaman depan, dan oleh
`astro.config.mjs` untuk judul di header situs.

Segala isi setelah tagline hingga heading `##` pertama akan menjadi **badan halaman depan**.

### One `##` Heading Equals One Page

Heading `##` memulai halaman baru. Teks headingnya menjadi judul halaman dan label
sidebar, dan nama berkasnya di-*slugify* otomatis. Emoji di heading aman dipakai — ia
tampil di judul tapi dibuang dari URL.

Contoh: heading `🧪 Testing` menghasilkan halaman di `/testing/` dengan judul
"🧪 Testing".

### Nested Sidebar via Colon

Untuk mengelompokkan halaman ke dalam satu folder sidebar, pakai format
`Nama Folder: Judul Halaman`. Grup "Guides" yang sedang kamu baca ini dibuat begitu —
tiga heading berbeda berbagi awalan `Guides:`, dan template otomatis mengelompokkannya.

Satu hal yang perlu diperhatikan: karena tanda titik dua dipakai sebagai pemisah folder,
**hindari titik dua di heading `##` biasa** kalau kamu tidak ingin halaman itu masuk ke
dalam folder.

### Subheadings and Table of Contents

`###` ke bawah tetap berada di dalam halaman yang sama dan otomatis menjadi entri daftar
isi di sisi kanan. Pakai ini untuk membagi isi halaman, seperti bagian yang sedang kamu
baca sekarang.

### Local Images and Assets

Taruh gambar di `documentation/public/assets/`, lalu rujuk dengan path relatif dari root
repo — persis seperti yang GitHub harapkan:

```markdown
![Diagram Arsitektur](./documentation/public/assets/diagram.png)
```

Path itu memang terlihat panjang, dan itu disengaja: ia ditulis dalam bentuk yang benar
saat README dibaca **langsung di GitHub**. Situs docs punya titik nol yang berbeda —
akarnya `documentation/public/` ditambah `base` GitHub Pages — jadi `dev-build.py`
menerjemahkan rujukan tadi menjadi `/<nama-repo>/assets/diagram.png` saat build. Satu
path yang kamu tulis, benar di dua tempat, tanpa berkas yang perlu diduplikasi.

Yang perlu diingat:

* Berkasnya sudah berada di folder statis Astro, jadi tidak ada penyalinan — cukup
  tambahkan gambar ke folder itu dan rujuk dari README.
* Yang diterjemahkan hanya bentuk `./documentation/public/assets/…`. Path absolut
  (diawali `/`) dan URL eksternal dibiarkan apa adanya.
* Berlaku untuk sintaks Markdown maupun atribut `src` pada HTML, jadi `<img>` juga aman.
* Contoh di dalam *code block* dan *inline code* tidak ikut diterjemahkan — berbeda dari
  penanda `DELETE_IN_DOCS`, kamu bebas mendokumentasikan path aset tanpa efek samping.

### Limitations

Pemecahan halaman dilakukan dengan pencarian teks pada README mentah, bukan dengan
mem-parsing Markdown. Artinya:

* Baris yang dimulai `##` **tetap dianggap pemisah halaman walau berada di dalam code
  block.** Kalau perlu menampilkan contoh heading Markdown, beri satu spasi di depannya
  atau tulis inline seperti `## Judul`.
* README wajib berada di root repositori dengan nama `README.md`.
* Belum ada dukungan multi-bahasa dan komponen MDX Starlight (`<Card>`, `<Tabs>`, dan
  sejenisnya) — sengaja, supaya README tetap wajar dibaca langsung di GitHub.

---

</div>