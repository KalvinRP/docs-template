---
title: "🚀 Getting Started"
---

<div data-theme-preset="sapphire">


### Prerequisites
Sebelum memulai, pastikan perangkat kamu sudah terinstal:
* **Node.js** `>= v18.0.0`
* **npm** `>= v9.0.0`
* **PostgreSQL** `>= v14`
* **Redis** (Opsional, untuk caching)

### Installation
1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/kasirku-api.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd kasirku-api
   ```
3. Install semua dependensi:
   ```bash
   npm install
   ```

### Configuration
Salin file `.env.example` menjadi `.env` lalu sesuaikan nilainya:
```bash
cp .env.example .env
```

Isi berkas `.env` dengan kredensial milikmu:
```env
PORT=3000
DATABASE_URL="postgresql://user:password@localhost:5432/kasirku_db?schema=public"
JWT_SECRET="super-secret-key-change-this"
REDIS_URL="redis://localhost:6379"
```

### Running Locally
Jalankan migrasi database lalu nyalakan server *development*:
```bash
# Jalankan migrasi Prisma
npx prisma migrate dev

# Jalankan server lokal
npm run dev
```
Server akan berjalan di `http://localhost:3000`.

---

</div>