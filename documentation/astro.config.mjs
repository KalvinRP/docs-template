// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { readFileSync } from 'node:fs';

// Judul & deskripsi situs diambil dari README.md (sumber tunggal), sama seperti
// halaman depan. Override eksplisit: <!-- TITLE: ... --> / <!-- DESCRIPTION: ... -->,
// jika tidak ada pakai H1 pertama dan blockquote (>) pertama.
function readReadmeMeta() {
  try {
    const readme = readFileSync(new URL('../README.md', import.meta.url), 'utf-8');
    const title =
      readme.match(/<!--\s*TITLE:\s*(.+?)\s*-->/)?.[1] ??
      readme.match(/^#\s+(.+)$/m)?.[1];
    const description =
      readme.match(/<!--\s*DESCRIPTION:\s*(.+?)\s*-->/)?.[1] ??
      readme.match(/^>\s+(.+)$/m)?.[1];
    return { title: title?.trim(), description: description?.trim() };
  } catch {
    return {};
  }
}

const meta = readReadmeMeta();

// GitHub Pages project site berada di sub-path (misal /docs-template), jadi Astro
// perlu tahu `site` + `base` agar URL aset (_astro/*.css) tidak menunjuk ke root
// domain. Nilainya diturunkan dari GITHUB_REPOSITORY ("owner/repo") supaya
// template ini tetap benar saat di-fork tanpa perlu diedit manual.
function readPagesUrls() {
  const [owner, repo] = (process.env.GITHUB_REPOSITORY ?? '').split('/');
  if (!owner || !repo) return {};
  const isUserSite = repo.toLowerCase() === `${owner.toLowerCase()}.github.io`;
  return {
    site: `https://${owner.toLowerCase()}.github.io`,
    base: isUserSite ? undefined : `/${repo}`,
  };
}

export default defineConfig({
  ...readPagesUrls(),
  integrations: [
    starlight({
      title: meta.title || 'Dokumentasi',
      description: meta.description,
      customCss: [
        './docs/src/styles/preset.css',
      ],
    }),
  ],
});
