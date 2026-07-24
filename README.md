<!-- PRESET: sapphire -->

<!-- DELETE_IN_DOCS_START -->
<p align="center">
  👉 <b><a href="[https://username.github.io/kasirku-api](https://username.github.io/kasirku-api)">Buka Versi Dokumentasi Interaktif (GitHub Pages)</a></b>
</p>
<hr />
<!-- DELETE_IN_DOCS_END -->

<!-- H1 pertama wajib ada, jadi title di index.md -->
# 🚀 KasirKu API

<!-- Tagline pertama wajib ada, jadi description di index.md -->
> Modern, lightweight, and high-performance Point of Sale (POS) backend API built for micro & small businesses.

---

## 📌 Project Overview

* **Project Title:** KasirKu API
* **Description:** API RESTful modular untuk mengelola inventaris produk, transaksi kasir real-time, serta pencatatan laporan keuangan otomatis untuk usaha ritel.
* **Problem Solved:** Aplikasi POS tradisional sering kali terlalu rumit, berat, dan memerlukan biaya lisensi mahal. KasirKu API hadir sebagai solusi *open-source* yang cepat, ringan, dan mudah diintegrasikan dengan aplikasi web maupun mobile.
* **Tech Stack:**
  * **Language:** TypeScript / Node.js
  * **Framework:** Express.js
  * **Database:** PostgreSQL (Prisma ORM)
  * **Cache:** Redis
  * **Testing:** Jest

---

## 🚀 Getting Started

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

## 💻 Usage & Examples

### Basic Example
Berikut cara melakukan autentikasi dan mengambil token JWT lewat terminal:

```bash
curl -X POST http://localhost:3000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@kasirku.com", "password": "password123"}'
```

### Common Use Cases
Membuat transaksi baru dari sisi klien / frontend (JavaScript):

```javascript
const createTransaction = async (cartItems, token) => {
  const response = await fetch('http://localhost:3000/api/v1/transactions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ items: cartItems, paymentMethod: 'CASH' })
  });
  
  return await response.json();
};
```

### Screenshots / Demo
<p align="center">
  <img src="[https://i.imgur.com/example-dashboard.png](https://i.imgur.com/example-dashboard.png)" alt="Tampilan Dashboard KasirKu" width="600" />
</p>

---

## 📡 API Reference

### Endpoints
| HTTP Method | Endpoint | Auth Required | Deskripsi |
|---|---|---|---|
| `POST` | `/api/v1/auth/login` | ❌ No | Login pengguna & dapatkan token |
| `GET` | `/api/v1/products` | ✅ Yes | Mengambil daftar semua produk |
| `POST` | `/api/v1/transactions` | ✅ Yes | Membuat transaksi penjualan baru |

### Request Parameters (`POST /api/v1/transactions`)
* **Headers:** `Authorization: Bearer <token>`
* **Body (JSON):**
  * `items` *(Array, Required)*: Daftar produk (`productId`, `qty`).
  * `paymentMethod` *(String, Required)*: `CASH`, `QRIS`, atau `CREDIT`.

### Response Format

**✅ Success Response (`201 Created`):**
```json
{
  "success": true,
  "message": "Transaction completed successfully",
  "data": {
    "transactionId": "trx_987654321",
    "totalAmount": 150000,
    "status": "PAID",
    "createdAt": "2026-07-25T05:00:00.000Z"
  }
}
```

**❌ Failure Response (`400 Bad Request`):**
```json
{
  "success": false,
  "error": "INSUFFICIENT_STOCK",
  "message": "Product ID 123 is out of stock"
}
```

---

## 🧪 Testing

### Test Commands
Jalankan pengujian unit (*unit testing*) dan pengujian integrasi:
```bash
# Jalankan seluruh test
npm run test

# Jalankan test dalam mode watch (saat ngoding)
npm run test:watch
```

### Coverage
Untuk melihat laporan cakupan kode (*test coverage*):
```bash
npm run test:coverage
```
Laporan HTML dapat dibuka di folder `coverage/lcov-report/index.html`.

---

## 🛠️ Deployment

### Build Step
Kompilasi kode TypeScript ke JavaScript matang untuk produksi:
```bash
npm run build
```
File hasil *build* akan tersimpan di dalam folder `dist/`.

### Environment Specs
* **Staging Server:** `[https://staging-api.kasirku.com](https://staging-api.kasirku.com)`
* **Production Server:** `[https://api.kasirku.com](https://api.kasirku.com)`
* **Node.js Runtime:** Minimal v18.x di lingkungan Linux LTS (Ubuntu 22.04 LTS diprioritaskan).

---

## 🤝 Contributing

### Code Style
* Gunakan ESLint dan Prettier yang sudah terpasang.
* Jalankan *linter* sebelum melakukan commit:
  ```bash
  npm run lint
  ```

### Workflow
1. *Fork* repositori ini.
2. Buat branch fitur baru (`git checkout -b feature/fitur-baru`).
3. Lakukan commit perubahan (`git commit -m "feat: tambah integrasi QRIS"`).
4. *Push* ke branch milikmu (`git push origin feature/fitur-baru`).
5. Buat **Pull Request (PR)** ke branch `main`.

---

## 📜 License & Contact

### License
Didistribusikan di bawah lisensi **MIT License**. Lihat `LICENSE` untuk informasi selengkapnya.

### Support
* **Email:** support@kasirku.com
* **GitHub Issues:** [Laporkan Bug / Masalah](https://github.com/username/kasirku-api/issues)
* **Community:** [Join Discord Server Kami](https://discord.gg/kasirku)