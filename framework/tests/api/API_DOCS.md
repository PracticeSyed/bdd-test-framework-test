# Practice Software Testing - API Documentation

## Base URL
```
https://api.practicesoftwaretesting.com
```

## Discovered Endpoints

### 📦 Products
- `GET /products` - Get all products (paginated)
- `GET /products/{id}` - Get single product by ID
- `GET /products?q={search}` - Search products by name
- `GET /products?by_category={category_id}` - Filter by category
- `GET /products?page={page}` - Pagination

**Response Example:**
```json
{
  "data": [
    {
      "id": "01KVQ5GFQ4S61JH2SSYKD60ET8",
      "name": "Combination Pliers",
      "price": 14.15,
      "category_id": "...",
      "brand_id": "..."
    }
  ],
  "total": 50
}
```

### 📂 Categories
- `GET /categories` - Get all categories

**Response Example:**
```json
[
  {
    "id": "...",
    "name": "Hand Tools"
  },
  {
    "id": "...",
    "name": "Power Tools"
  }
]
```

### 🏷️ Brands
- `GET /brands` - Get all brands

**Response Example:**
```json
[
  {
    "id": "...",
    "name": "ForgeFlex Tools"
  },
  {
    "id": "...",
    "name": "MightyCraft Hardware"
  }
]
```

### 👤 Users (Requires Authentication)
- `POST /users/login` - User login (401 without credentials)
- `POST /users/register` - User registration (401 without data)
- `GET /users` - Get user info (401 without auth)

## Test Coverage

✅ Get all products
✅ Get single product
✅ Get categories
✅ Get brands
✅ Search products
✅ Filter by category
✅ Pagination
✅ Error handling (404)
