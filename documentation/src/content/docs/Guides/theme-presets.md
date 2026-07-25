---
title: "Theme Presets"
---

<div data-theme-preset="sapphire">


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

</div>