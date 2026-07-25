<!-- PRESET: sapphire -->

<!-- DELETE_IN_DOCS_START -->
<p align="center">
  👉 <b><a href="https://kalvinrp.github.io/template">Lihat README ini setelah jadi situs dokumentasi</a></b><br/>
  <sub>Situs itu dibangun 100% dari berkas <code>README.md</code> di root.</sub><br/>
  <sub>Gunakan command <code>npx degit kalvinrp/template nama-project</code> untuk memulai project dengan sistem dokumentasi ini.</sub>
</p>
<hr />
<!-- DELETE_IN_DOCS_END -->

<!-- H1 pertama wajib ada, jadi title di index.md -->
# 📘 Docs Template

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

## 🩹 Motivation

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

## 🚀 Getting Started

### Prerequisites

Untuk memakainya kamu **tidak perlu apa pun selain browser** — semua build berjalan di
GitHub Actions. Yang berikut hanya diperlukan bila ingin *preview* lokal:

* **Python** `>= 3.8` (untuk `dev-build.py`; hanya modul standar, tanpa dependensi)
* **Node.js** `>= 20` (CI memakai Node 24)

### Installation

1. Klik *Use this template* pada repositori ini atau degit pada local:

    ```bash
    npx degit kalvinrp/template nama-project
    ```

2. Kembangkan project pada root kemudian push jika masih lokal.
3. Tulis dokumentasi proyekmu di `README.md` (ganti seluruh isi berkas ini). Gambar dan aset lokal lain disimpan di `documentation/public/assets/` — lihat **Guides → Page Structure**.
4. Aktifkan GitHub Pages: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
5. Commit dan push ke `main`:

   ```bash
   git add README.md
   git commit -m "docs: tulis dokumentasi proyek"
   git push origin main
   ```

Workflow `Auto Update Docs` akan jalan sendiri, dan situs dokumentasi terbit di
`https://<username>.github.io/<nama-repo>`.

### Configuration

Tidak ada berkas konfigurasi yang wajib kamu sentuh. `base` dan `site` Astro diturunkan
otomatis dari variabel `GITHUB_REPOSITORY`, jadi hasil *fork* langsung benar tanpa
mengedit `astro.config.mjs` — termasuk bila repomu bernama `<username>.github.io`.

Satu-satunya "konfigurasi" yang lazim diubah ada di baris pertama README, yaitu penanda
preset tema. Lihat **Guides → Theme Presets**.

### Running Locally

```bash
# 1. Pecah README.md menjadi halaman-halaman docs
python3 documentation/dev-build.py

# 2. Jalankan dev server Astro
cd documentation
npm install
npm run dev
```

Buka `http://localhost:4321`. Ulangi langkah 1 setiap kali README berubah — skrip itulah
yang menerjemahkan README menjadi halaman.

Untuk mengecek hasil produksi persis seperti di Pages:

```bash
npm run build && npm run preview
```

---

## ⚙️ How It Works

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

## Guides: Page Structure

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

## Guides: README Markers

Selain heading, ada beberapa penanda berbentuk komentar HTML yang mengatur perilaku build.
Semuanya ditulis satu baris, dibuka dengan `<!--` dan ditutup `-->`.

| Marker | Fungsi | Default bila tak ada |
|---|---|---|
| `PRESET: <nama>` | Menentukan tema seluruh situs | Tema bawaan Starlight |
| `TITLE: <teks>` | Menimpa judul situs dari H1 | H1 pertama |
| `DESCRIPTION: <teks>` | Menimpa deskripsi situs dari tagline | Blockquote pertama |
| `DELETE_IN_DOCS_START` … `DELETE_IN_DOCS_END` | Membuang blok di antaranya dari situs docs | — |

### GitHub-Only Blocks

Sebagian isi README hanya berguna di GitHub: badge, tombol menuju situs docs, catatan
untuk kontributor repo. Bungkus bagian itu di antara penanda `DELETE_IN_DOCS_START` dan
`DELETE_IN_DOCS_END`, dan ia akan lenyap dari situs sambil tetap tampil di GitHub.

Repo ini memakainya untuk banner tautan di paling atas README — itulah sebabnya kamu tidak
melihat banner tersebut di situs ini.

### Caveat When Documenting Markers

Penanda dicari di **seluruh isi README mentah**, termasuk di dalam code block. Jadi kalau
kamu menuliskan contoh penanda lengkap dengan tanda komentarnya di dalam sebuah code
block, penanda itu **benar-benar ikut aktif** — contoh `TITLE` akan mengubah judul situs,
dan sepasang penanda `DELETE_IN_DOCS` akan menghapus isi contohnya sendiri.

Karena itu, tabel di atas menuliskan nama penanda tanpa tanda komentar. Terapkan cara yang
sama bila kamu perlu mendokumentasikan penanda di README-mu.

---

## Guides: Theme Presets

Ganti tema seluruh situs — warna aksen, font, kelengkungan sudut, *letter-spacing*
heading — dengan mengedit **satu baris** penanda `PRESET` di paling atas README. Tidak ada
CSS yang perlu ditulis, dan tidak ada berkas lain yang perlu disentuh.

### Available Presets

| Nama | Karakter | Font | Sudut |
|---|---|---|---|
| `emerald` | Organic / Calm | Rounded | Sangat bulat |
| `sapphire` | Clean / Corporate | Sans-serif | Tegas |
| `indigo` | Modern / Techy | Sans-serif | Tegas |
| `violet` | Creative / Vivid | Sans-serif | Sedang |
| `crimson` | Editorial / Bold | Serif | Nyaris kotak |
| `rose` | Playful / Soft | Rounded | Bulat |
| `amber` | Warm / Friendly | Rounded | Sedang |
| `teal` | Fresh / Minimal | Sans-serif | Sedang |
| `slate` | Mono / Developer | Monospace | Nyaris kotak |

Menghapus penanda `PRESET` sepenuhnya akan mengembalikan tampilan ke tema bawaan Astro Starlight.

### How Presets Work

Semua preset berupa CSS murni tanpa dependensi dan memakai font sistem, jadi tak ada
permintaan jaringan tambahan. `dev-build.py` membungkus konten dalam sebuah `div`
bertanda preset, lalu `preset.css` memakai selektor `:root:has([data-theme-preset="..."])`
untuk memasang variabel di `:root`. Efeknya: **seluruh** situs ikut bertema — sidebar,
header, dan konten — bukan hanya badan artikel.

Menambah preset sendiri cukup dengan menyalin satu blok di
`documentation/docs/src/styles/preset.css` dan mengganti empat variabelnya.

---

## 🤝 Contributing

### Workflow

1. *Fork* repositori ini.
2. Buat branch fitur (`git checkout -b feature/nama-fitur`).
3. Commit perubahan (`git commit -m "feat: tambah preset ocean"`).
4. *Push* ke branch milikmu (`git push origin feature/nama-fitur`).
5. Buka **Pull Request** ke branch `main`.

### Before Opening a PR

Jalankan build lokal untuk memastikan README masih terpecah dengan benar dan situs tetap
bisa dibangun:

```bash
python3 documentation/dev-build.py
cd documentation && npm install && npm run build
```

Perlu diingat: `documentation/dist/` dan `documentation/.astro/` tidak ikut di-commit, dan
isi `documentation/src/content/docs/` selalu ditimpa ulang oleh skrip build. Bila
perubahanmu menyangkut isi dokumentasi, berkas yang kamu sunting seharusnya hanya
`README.md`.

### Roadmap

* Preset tema baru di `preset.css`.
* Dukungan multi-bahasa (`README.id.md`, `README.en.md`).
* Menerjemahkan sebagian sintaks Markdown ke komponen Starlight (misalnya blockquote
  bertanda `[!NOTE]` menjadi *Aside*).

---

## 📜 License & Contact

### License

Didistribusikan di bawah lisensi **MIT License**. Lihat `LICENSE` untuk keterangan lengkap.

### Support

* **Repositori:** [github.com/KalvinRP/docs-template](https://github.com/KalvinRP/docs-template)
* **GitHub Issues:** [Laporkan bug atau usulkan fitur](https://github.com/KalvinRP/docs-template/issues)

### Built With

[Astro](https://astro.build) · [Starlight](https://starlight.astro.build) ·
[Pagefind](https://pagefind.app) · GitHub Actions · GitHub Pages

![Gambar Penutup](./documentation/public/assets/marek-piwnicki-unsplash.jpg)
