---
title: "📡 API Reference"
---

<div data-theme-preset="crimson">


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

</div>