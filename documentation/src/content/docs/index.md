---
title: "📘 Docs Template"
description: "Tulis README sekali, dapat situs dokumentasi otomatis."
---

<div data-theme-preset="sapphire">

<!-- PRESET: sapphire -->



<!-- H1 pertama wajib ada, jadi title di index.md -->

<!-- Tagline pertama wajib ada, jadi description di index.md -->
> Tulis README sekali, dapat situs dokumentasi otomatis.

---

Dokumentasi hampir selalu jadi pekerjaan yang ditunda. Bukan karena developer malas
menulis, tapi karena **menerbitkannya** yang merepotkan: harus setup generator, atur
sidebar, urus routing, lalu mengurus dua berkas berbeda yang isinya mirip — `README.md`
untuk orang yang mampir ke repo, dan folder `docs/` untuk situsnya. Begitu keduanya mulai
berbeda, tak ada lagi yang bisa dipercaya.

Template ini menghapus salah satu sisi masalah itu: **`README.md` adalah satu-satunya
tempat kamu menulis.** Sisanya urusan pipeline.

* Setiap heading `##` otomatis jadi satu halaman beserta entri sidebar-nya.
* Judul dan deskripsi situs ditarik dari H1 dan tagline README.
* Tema seluruh situs diganti dengan mengedit satu baris komentar di paling atas.
* Push ke `main` → situs terbit ke GitHub Pages. Tidak ada langkah manual.

Yang kamu dapat bukan README panjang yang di-scroll, melainkan situs dokumentasi utuh:
pencarian *full-text* (Pagefind), mode gelap/terang, daftar isi per halaman, navigasi
prev/next, responsif di ponsel, plus sitemap.

**Halaman ini adalah contohnya sendiri.** Semua yang ada di sidebar
kiri lahir dari heading `##` di README repo ini.

---

</div>