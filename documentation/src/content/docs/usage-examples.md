---
title: "💻 Usage & Examples"
---

<div data-theme-preset="sapphire">


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

</div>