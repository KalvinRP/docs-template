---
title: "🚀 Getting Started"
---

<div data-theme-preset="sapphire">


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

</div>