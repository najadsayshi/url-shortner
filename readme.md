# 🔗 FastAPI URL Shortener

A simple and efficient URL shortener API built with **FastAPI** and **SQLModel**.
It allows users to shorten URLs, create custom aliases, track clicks, and view analytics.

---

## 🚀 Features

* ✅ Shorten long URLs
* 🎯 Custom aliases for short links
* 🔁 Redirect to original URL
* 📊 Click tracking & analytics
* ⏳ Optional expiration support
* ⚡ Fast and lightweight (FastAPI)

---

## 🛠️ Tech Stack

* **FastAPI** – API framework
* **SQLModel** – ORM & database handling
* **SQLite / PostgreSQL** – Database (configurable)
* **Base62 Encoding** – Short code generation

---

## 📁 Project Structure

```
.
├── app
│   ├── routes.py        # API endpoints
│   ├── models.py        # Database models
│   ├── schemas.py       # Request/response schemas
│   ├── db.py            # Database setup
│   └── utils.py         # Helper functions (Base62 encoder)
├── main.py              # App entry point
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlmodel
```

---

## ▶️ Running the App

```bash
uvicorn main:app --reload
```

App will be available at:

```
http://localhost:8000
```

Interactive docs:

```
http://localhost:8000/docs
```

---

## 📌 API Endpoints

### 🔹 Root

```
GET /
```

**Response:**

```json
{
  "message": "Welcome to the URL Shortener API!"
}
```

---

### 🔹 Shorten URL

```
POST /shorten
```

**Request Body:**

```json
{
  "original_url": "https://example.com",
  "custom_alias": "my-link"   // optional
}
```

**Response:**

```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

---

### 🔹 Redirect

```
GET /{short_code}
```

* Redirects to the original URL
* Increments click count
* Returns:

  * `404` if not found
  * `410` if expired

---

### 🔹 Analytics

```
GET /analytics/{short_code}
```

**Response:**

```json
{
  "original_url": "https://example.com",
  "click_count": 10,
  "created_at": "2026-01-01T12:00:00",
  "expiry_at": null
}
```

---

## 🔐 Custom Alias Rules

* Must be unique
* Returns `409 Conflict` if already taken

---

## 🧠 How It Works

1. URL is stored in the database
2. Unique ID is generated
3. ID is encoded using Base62
4. Encoded string becomes the short URL
5. Redirect endpoint maps short code → original URL

---

## 📈 Future Improvements

* User authentication
* Rate limiting
* QR code generation
* Dashboard UI
* Link expiration customization

---

## 🧪 Example cURL

```bash
curl -X POST "http://localhost:8000/shorten" \
-H "Content-Type: application/json" \
-d '{"original_url": "https://google.com"}'
```

 * -> You can use Postman too,i used Postman,this is my first time using curl.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Najad.
## Inspired from roadmap.sh
https://roadmap.sh/projects/url-shortening-service
---
