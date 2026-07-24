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

export default defineConfig({
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
