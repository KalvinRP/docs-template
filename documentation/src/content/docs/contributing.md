---
title: "🤝 Contributing"
---

<div data-theme-preset="sapphire">


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

</div>