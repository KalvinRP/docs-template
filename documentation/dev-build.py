import re, os, shutil, sys

# Cegah error jika print emoji di Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Sesuaikan path karena skrip dipanggil dari root repo saat di CI/CD
readme_path = "README.md" if os.path.exists("README.md") else "../README.md"
output_dir = "documentation/src/content/docs" if os.path.exists("documentation/src/content/docs") else "src/content/docs"
astro_cache = "documentation/.astro" if os.path.exists("documentation/.astro") else ".astro"

# 🚀 1. HAPUS CACHE ASTRO & FOLDER DOCS LAMA
if os.path.exists(astro_cache):
    shutil.rmtree(astro_cache)

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)

os.makedirs(output_dir, exist_ok=True)

if not os.path.exists(readme_path):
    print("❌ README.md tidak ditemukan!")
    exit(1)

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# 🧹 1b. HAPUS BLOK KHUSUS README yang tak perlu tampil di situs docs
content = re.sub(
    r"<!--\s*DELETE_IN_DOCS_START\s*-->.*?<!--\s*DELETE_IN_DOCS_END\s*-->",
    "", content, flags=re.DOTALL,
)

# 📝 1c. JUDUL & DESKRIPSI HALAMAN DEPAN DIAMBIL DARI README
# Prioritas: override eksplisit <!-- TITLE: ... --> / <!-- DESCRIPTION: ... -->,
# lalu fallback ke H1 pertama dan blockquote (>) pertama.
title_match = re.search(r"<!--\s*TITLE:\s*(.+?)\s*-->", content) or re.search(r"^#\s+(.+)$", content, re.MULTILINE)
home_title = title_match.group(1).strip() if title_match else "Home"

desc_match = re.search(r"<!--\s*DESCRIPTION:\s*(.+?)\s*-->", content) or re.search(r"^>\s+(.+)$", content, re.MULTILINE)
home_desc = desc_match.group(1).strip() if desc_match else "Dokumentasi proyek."

def yaml_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

# 🖼️ 1d. ASET LOKAL: terjemahkan path documentation/public/assets/ jadi URL situs
# README dibaca dari dua titik nol berbeda: di GitHub relatif terhadap root repo, di
# situs relatif terhadap documentation/public/ ditambah base GitHub Pages. Penulis
# memakai bentuk yang benar di GitHub, dan bentuk itu diterjemahkan di sini — berkasnya
# sendiri tidak perlu disalin karena sudah berada di folder statis Astro.
# Perhitungan base mencerminkan readPagesUrls() di astro.config.mjs.
owner, _, repo = (os.environ.get("GITHUB_REPOSITORY") or "").partition("/")
base = "" if not owner or not repo or repo.lower() == f"{owner.lower()}.github.io" else f"/{repo}"
print(f"🖼️  Base URL aset: {base or '/'}")

def rewrite_asset_paths(text):
    # Code block dan inline code dilewati, supaya contoh sintaks di dokumentasi tidak
    # ikut diterjemahkan. re.split dengan grup penangkap menaruh potongan di luar code
    # pada indeks genap.
    parts = re.split(r"(```.*?```|`[^`\n]+`)", text, flags=re.DOTALL)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(
            # Hanya ubah path yang dimulai dengan ./documentation/public/assets/ atau documentation/public/assets/
            r'(\]\(|src=["\'])(?:\./)?documentation/public/assets/',
            lambda m: f"{m.group(1)}{base}/assets/",
            parts[i],
        )
    return "".join(parts)

content = rewrite_asset_paths(content)

# 🚀 2. BACA TEMA PRESET (Fitur dari preset-style.py)
match = re.search(r"<!--\s*PRESET:\s*(\w+)\s*-->", content)
preset = match.group(1).lower() if match else "default"
print(f"🎨 Tema terdeteksi: {preset}")

# Bungkus konten dengan penanda preset. Div ini dipakai preset.css lewat
# :root:has([data-theme-preset="..."]) untuk mewarnai SELURUH situs dari :root.
def apply_preset(text_content):
    if preset and preset != "default":
        return f'<div data-theme-preset="{preset}">\n\n{text_content}\n\n</div>'
    return text_content

# 🚀 3. PECAH CONTENT BERDASARKAN H2 (## )
sections = re.split(r"\n(?=## )", content)

# Section pertama (H1) -> index.md
first_section = sections[0].strip()
# H1 pertama sudah dipromosikan jadi title frontmatter → buang dari body biar tak dobel
first_body = re.sub(r"^#\s+.+$\n?", "", first_section, count=1, flags=re.MULTILINE).strip()
first_section_styled = apply_preset(first_body)

with open(f"{output_dir}/index.md", "w", encoding="utf-8") as f:
    f.write(
        f'---\ntitle: "{yaml_escape(home_title)}"\ndescription: "{yaml_escape(home_desc)}"\n---\n\n'
        + first_section_styled
    )

# Section H2 sisanya (Multi-page)
for section in sections[1:]:
    lines = section.strip().split("\n")
    raw_header = lines[0].replace("## ", "").strip()
    body = "\n".join(lines[1:])
    body_styled = apply_preset(body)

    if ":" in raw_header:
        folder_part, title_part = raw_header.split(":", 1)
        folder_name = folder_part.strip()
        
        file_name = re.sub(r"[^\w\s-]", "", title_part).strip().lower()
        file_name = re.sub(r"[-\s]+", "-", file_name) + ".md"
        
        target_dir = os.path.join(output_dir, folder_name)
        os.makedirs(target_dir, exist_ok=True)

        file_path = os.path.join(target_dir, file_name)
        doc_title = title_part.strip()
    else:
        file_name = re.sub(r"[^\w\s-]", "", raw_header).strip().lower()
        file_name = re.sub(r"[-\s]+", "-", file_name) + ".md"
        file_path = os.path.join(output_dir, file_name)
        doc_title = raw_header

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: \"{doc_title}\"\n---\n\n" + body_styled)

print("🧹 Folder docs dibersihkan, preset diterapkan, & README.md berhasil dipecah ulang!")