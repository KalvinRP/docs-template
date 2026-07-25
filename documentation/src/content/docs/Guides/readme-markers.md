---
title: "README Markers"
---

<div data-theme-preset="sapphire">


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

</div>