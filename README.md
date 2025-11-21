# E-Commerce API Documentation

## Base URL
```
http://localhost:8000/api/
```

---

## Categories API

### 1. List All Categories
**Endpoint:** `GET /categories/`

**Description:** Retrieve a list of all categories.

**Response:** `200 OK`
```json
{
  "categories": [
    {
      "id": 1,
      "name": "Electronics",
      "description": "Electronic devices and gadgets",
      "created_at": "2025-01-15T10:30:00Z",
      "updated_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

---

### 2. Create Category
**Endpoint:** `POST /categories/`

**Description:** Create a new category.

**Request Body:**
```json
{
  "name": "Electronics",
  "description": "Electronic devices and gadgets"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "name": "Electronics",
  "description": "Electronic devices and gadgets",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

**Validation:**
- `name` - Required, unique, max 128 characters
- `description` - Optional

---

### 3. Get Category Detail
**Endpoint:** `GET /categories/{id}/`

**Description:** Retrieve details of a specific category.

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Electronics",
  "description": "Electronic devices and gadgets",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

**Error:** `404 Not Found` if category doesn't exist.

---

### 4. Update Category
**Endpoint:** `PUT /categories/{id}/`

**Description:** Update an existing category.

**Request Body:**
```json
{
  "name": "Consumer Electronics",
  "description": "Updated description"
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "Consumer Electronics",
  "description": "Updated description",
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T12:45:00Z"
}
```

---

### 5. Delete Category
**Endpoint:** `DELETE /categories/{id}/`

**Description:** Delete a category.

**Response:** `204 No Content`
```json
{
  "message": "Category deleted successfully"
}
```

---

## Products API

### 1. List All Products
**Endpoint:** `GET /products/`

**Description:** Retrieve a list of all products with related category and images.

**Response:** `200 OK`
```json
{
  "products": [
    {
      "id": 1,
      "name": "iPhone 15 Pro",
      "description": "Latest Apple smartphone",
      "price": "999.99",
      "stock": 50,
      "is_active": true,
      "category": "Electronics",
      "category_id": 1,
      "images": [
        {
          "id": 1,
          "url": "http://localhost:8000/media/product_pics/iphone.jpg",
          "alt_text": "iPhone front view"
        }
      ],
      "created_at": "2025-01-15T10:30:00Z",
      "updated_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

---

### 2. Create Product
**Endpoint:** `POST /products/`

**Description:** Create a new product.

**Request Body:**
```json
{
  "name": "iPhone 15 Pro",
  "description": "Latest Apple smartphone",
  "price": 999.99,
  "stock": 50,
  "category_id": 1,
  "is_active": true
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "description": "Latest Apple smartphone",
  "price": "999.99",
  "stock": 50,
  "is_active": true,
  "category": "Electronics",
  "category_id": 1,
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

**Validation:**
- `name` - Required, max 256 characters
- `price` - Required, decimal with 2 places
- `stock` - Required, positive integer
- `category_id` - Optional, must exist if provided
- `is_active` - Optional, defaults to true

---

### 3. Get Product Detail
**Endpoint:** `GET /products/{id}/`

**Description:** Retrieve details of a specific product with images.

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "iPhone 15 Pro",
  "description": "Latest Apple smartphone",
  "price": "999.99",
  "stock": 50,
  "is_active": true,
  "category": "Electronics",
  "category_id": 1,
  "images": [
    {
      "id": 1,
      "url": "http://localhost:8000/media/product_pics/iphone.jpg",
      "alt_text": "iPhone front view"
    }
  ],
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T10:30:00Z"
}
```

---

### 4. Update Product
**Endpoint:** `PUT /products/{id}/`

**Description:** Update an existing product.

**Request Body:**
```json
{
  "name": "iPhone 15 Pro Max",
  "price": 1199.99,
  "stock": 30,
  "category_id": 1,
  "is_active": true
}
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "name": "iPhone 15 Pro Max",
  "description": "Latest Apple smartphone",
  "price": "1199.99",
  "stock": 30,
  "is_active": true,
  "category": "Electronics",
  "category_id": 1,
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T14:20:00Z"
}
```

**Note:** You can set `category_id` to `null` to remove the category association.

---

### 5. Delete Product
**Endpoint:** `DELETE /products/{id}/`

**Description:** Delete a product (cascades to images).

**Response:** `204 No Content`
```json
{
  "message": "Product deleted successfully"
}
```

---

### 6. Search & Filter Products
**Endpoint:** `GET /products/search/`

**Description:** Search and filter products with multiple criteria.

**Query Parameters:**

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `search` | string | Search in name or description | `?search=laptop` |
| `category` | integer | Filter by category ID | `?category=1` |
| `is_active` | boolean | Filter by active status | `?is_active=true` |
| `min_price` | decimal | Minimum price | `?min_price=100` |
| `max_price` | decimal | Maximum price | `?max_price=1000` |
| `in_stock` | boolean | Only show products with stock > 0 | `?in_stock=true` |
| `order_by` | string | Sort results | `?order_by=-price` |

**Valid `order_by` values:**
- `name` - Name A-Z
- `-name` - Name Z-A
- `price` - Price low to high
- `-price` - Price high to low
- `created_at` - Oldest first
- `-created_at` - Newest first (default)
- `stock` - Stock low to high
- `-stock` - Stock high to low

**Example Request:**
```
GET /products/search/?search=iphone&category=1&min_price=500&max_price=2000&order_by=-price&is_active=true
```

**Response:** `200 OK`
```json
{
  "products": [
    {
      "id": 1,
      "name": "iPhone 15 Pro",
      "description": "Latest Apple smartphone",
      "price": "999.99",
      "stock": 50,
      "is_active": true,
      "category": "Electronics",
      "category_id": 1,
      "images": [
        {
          "id": 1,
          "url": "http://localhost:8000/media/product_pics/iphone.jpg",
          "alt_text": "iPhone front view"
        }
      ],
      "created_at": "2025-01-15T10:30:00Z",
      "updated_at": "2025-01-15T10:30:00Z"
    }
  ],
  "count": 1
}
```

**Use Cases:**
```
# Search for products containing "laptop"
GET /products/search/?search=laptop

# Get all products in category 1
GET /products/search/?category=1

# Get products between $100-$500
GET /products/search/?min_price=100&max_price=500

# Get only in-stock products, sorted by price (high to low)
GET /products/search/?in_stock=true&order_by=-price

# Complex query: Active electronics under $1000, sorted by name
GET /products/search/?category=1&is_active=true&max_price=1000&order_by=name
```

---

## Product Images API

### 1. List All Images
**Endpoint:** `GET /images/`

**Description:** Retrieve a list of all product images.

**Response:** `200 OK`
```json
{
  "images": [
    {
      "id": 1,
      "url": "http://localhost:8000/media/product_pics/iphone.jpg",
      "alt_text": "iPhone front view",
      "product_id": 1,
      "product_name": "iPhone 15 Pro",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

---

### 2. Upload Product Image
**Endpoint:** `POST /images/`

**Description:** Upload a new image for a product.

**Content-Type:** `multipart/form-data`

**Form Data:**
```
product_id: 1
alt_text: iPhone front view
image: [binary file]
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/api/images/ \
  -F "product_id=1" \
  -F "alt_text=iPhone front view" \
  -F "image=@/path/to/image.jpg"
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "url": "http://localhost:8000/media/product_pics/iphone.jpg",
  "alt_text": "iPhone front view",
  "product_id": 1,
  "product_name": "iPhone 15 Pro",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**Validation:**
- `product_id` - Required, must exist
- `image` - Required, valid image file
- `alt_text` - Optional, max 256 characters

---

### 3. Get Image Detail
**Endpoint:** `GET /images/{id}/`

**Description:** Retrieve details of a specific image.

**Response:** `200 OK`
```json
{
  "id": 1,
  "url": "http://localhost:8000/media/product_pics/iphone.jpg",
  "alt_text": "iPhone front view",
  "product_id": 1,
  "product_name": "iPhone 15 Pro",
  "created_at": "2025-01-15T10:30:00Z"
}
```

---

### 4. Update Image
**Endpoint:** `PUT /images/{id}/`

**Description:** Update image or alt text.

**Content-Type:** `multipart/form-data`

**Form Data:**
```
alt_text: Updated alt text
image: [binary file] (optional)
```

**Response:** `200 OK`
```json
{
  "id": 1,
  "url": "http://localhost:8000/media/product_pics/iphone_new.jpg",
  "alt_text": "Updated alt text",
  "product_id": 1,
  "product_name": "iPhone 15 Pro",
  "created_at": "2025-01-15T10:30:00Z"
}
```

---

### 5. Delete Image
**Endpoint:** `DELETE /images/{id}/`

**Description:** Delete an image.

**Response:** `204 No Content`
```json
{
  "message": "Image deleted successfully"
}
```

---

# Orders API Documentation

## Base URL
```
http://localhost:8000/api/orders/
```

---

## 📋 Endpoints

### 1. Create Order
**POST** `/orders/create/`

Create a new order directly from product IDs.

**Request:**
```json
{
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "+1234567890",
  "shipping_address": "123 Main St",
  "shipping_city": "New York",
  "shipping_state": "NY",
  "shipping_postal_code": "10001",
  "shipping_country": "USA",
  "items": [
    {"product_id": 1, "quantity": 2},
    {"product_id": 5, "quantity": 1}
  ],
  "notes": "Deliver after 5 PM"
}
```

**Response:** `201 Created`
```json
{
  "message": "Order created successfully",
  "order": {
    "id": 1,
    "order_number": "ORD-A1B2C3D4",
    "customer_name": "John Doe",
    "status": "pending",
    "items": [
      {
        "product_name": "iPhone 15 Pro",
        "quantity": 2,
        "price": "999.99",
        "total": "1999.98"
      }
    ],
    "subtotal": "2249.97",
    "total": "2249.97",
    "created_at": "2025-01-15T10:30:00Z"
  }
}
```

---

### 2. List My Orders
**GET** `/orders/`

Get all orders for logged-in user.

**Query Parameters:**
- `status` - Filter by status (optional)

**Response:** `200 OK`
```json
{
  "orders": [
    {
      "order_number": "ORD-A1B2C3D4",
      "customer_name": "John Doe",
      "status": "pending",
      "total": "2249.97",
      "created_at": "2025-01-15T10:30:00Z"
    }
  ]
}
```

---

### 3. Get Order Details
**GET** `/orders/{order_number}/`

Get full order details.

**Response:** `200 OK`
```json
{
  "order_number": "ORD-A1B2C3D4",
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "shipping_address": {
    "address": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postal_code": "10001",
    "country": "USA"
  },
  "status": "pending",
  "items": [
    {
      "product_name": "iPhone 15 Pro",
      "quantity": 2,
      "price": "999.99",
      "total": "1999.98"
    }
  ],
  "subtotal": "2249.97",
  "total": "2249.97",
  "notes": "Deliver after 5 PM",
  "created_at": "2025-01-15T10:30:00Z"
}
```

---

### 4. Update Order Status (Staff Only)
**PUT** `/orders/{order_number}/status/`

Update order status.

**Request:**
```json
{
  "status": "shipped",
  "notes": "Shipped via FedEx"
}
```

**Valid Status:**
- `pending` → `processing` → `shipped` → `delivered`
- `cancelled`

**Response:** `200 OK`
```json
{
  "message": "Order status updated",
  "order_number": "ORD-A1B2C3D4",
  "status": "shipped"
}
```

---

### 5. Cancel Order
**POST** `/orders/{order_number}/cancel/`

Cancel order and restore stock (only pending/processing orders).

**Response:** `200 OK`
```json
{
  "message": "Order cancelled successfully",
  "order_number": "ORD-A1B2C3D4"
}
```

---

## 🔄 Order Status Flow

```
pending → processing → shipped → delivered
   ↓
cancelled
```

---


## Common HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 204 | No Content - Resource deleted successfully |
| 400 | Bad Request - Invalid data provided |
| 404 | Not Found - Resource doesn't exist |
| 500 | Internal Server Error - Server error |

