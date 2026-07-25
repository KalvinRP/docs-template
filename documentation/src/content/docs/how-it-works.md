---
title: "⚙️ How It Works"
---

<div data-theme-preset="sapphire">


Seluruh pipeline hanya tiga lompatan, dan tak ada satu pun yang perlu kamu jalankan
manual saat produksi:

```text
README.md                          ← satu-satunya berkas yang kamu tulis
    │
    │  python3 documentation/dev-build.py
    │  · buang blok DELETE_IN_DOCS
    │  · ambil title dari H1, description dari tagline
    │  · terjemahkan path aset lokal jadi URL situs
    │  · pecah tiap "##" jadi satu halaman + frontmatter
    │  · bungkus konten dengan penanda preset tema
    ▼
documentation/src/content/docs/*.md
    │
    │  npm run build   (Astro + Starlight + Pagefind)
    ▼
documentation/dist/  ──▶  GitHub Pages
```

### Project Structure

| Path | Peran |
|---|---|
| `README.md` | Sumber tunggal seluruh isi dokumentasi |
| `documentation/public/assets/` | Gambar dan aset lokal yang dirujuk README |
| `documentation/dev-build.py` | Pemecah README → halaman Markdown ber-frontmatter |
| `documentation/astro.config.mjs` | Konfigurasi Starlight; membaca judul & deskripsi dari README |
| `documentation/docs/src/styles/preset.css` | Definisi seluruh preset tema |
| `.github/workflows/deploy-docs.yaml` | Build & deploy otomatis saat push ke `main`/`master` |

### Why Not a Plain `docs/` Folder?

Karena begitu ada folder `docs/`, ia menjadi berkas yang harus dirawat. `documentation/src/content/docs/`
di repo ini **hasil generate** — skrip build menghapusnya lebih dulu setiap kali jalan,
bersama cache `.astro`. Konsekuensinya penting untuk diingat: **jangan pernah mengedit
berkas di dalam folder itu**, karena perubahanmu akan hilang pada build berikutnya. Semua
suntingan dilakukan di README.

### What This Setup Provides

Bagian ini gratis begitu kontenmu masuk: pencarian *full-text* via Pagefind, toggle
gelap/terang, daftar isi per halaman dari heading `###`, navigasi halaman sebelumnya /
berikutnya, sidebar yang otomatis tersusun dari struktur folder, *syntax highlighting*
lewat Expressive Code, dan sitemap untuk mesin pencari.

---

</div>