# 💳 Transaction Monitoring System API

A robust backend API built with **Django Rest Framework (DRF)** to simulate a banking transaction management system.  
This system handles **user registration, customer data management, and transaction tracking** — including date filtering, customer-based queries, and pagination.

---

## 🚀 Features

### 👤 User Management
- Register and authenticate users using **JWT tokens**
- Secure login and logout endpoints
- Role-based access (admin, operator, analyst)

### 🧍 Customer Management
- Create and manage customer records
- Retrieve, update, and delete customer information
- Associate transactions with customers

### 💰 Transaction Management
- Create new transactions
- List all transactions (paginated)
- Retrieve single transactions by ID
- Filter transactions by date range
- View all transactions for a specific customer

---

## 🏗️ Project Structure

```
Transaction_Monitoring_System_API/
├── User/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── Customer/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── Transactions/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── TransactionMonitoringSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── requirements.txt
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|:------|:------------|
| **Backend Framework** | Django 5 / Django REST Framework |
| **Database** | PostgreSQL (recommended) / SQLite (for testing) |
| **Authentication** | JWT (JSON Web Token) |
| **API Docs** | Swagger / drf-yasg |
| **Testing** | Django TestCase / Postman |
| **Deployment** | Render, Railway, or AWS EC2 (optional) |

---

## 🧩 API Endpoints Overview

### 🔐 **User**
| Method | Endpoint | Description |
|:------:|:----------|:-------------|
| POST | `/api/users/register/` | Register a new user |
| POST | `/api/users/login/` | Login and get JWT tokens |
| GET | `/api/users/profile/` | Retrieve user profile |

---

### 👥 **Customer**
| Method | Endpoint | Description |
|:------:|:----------|:-------------|
| POST | `/api/customers/create/` | Create a new customer |
| GET | `/api/customers/list/` | List all customers |
| GET | `/api/customers/<uuid:pk>/` | Retrieve customer details |
| PUT/PATCH | `/api/customers/<uuid:pk>/` | Update customer info |
| POST/GET/PUT/PATCH/DELETE | `/api/customers/admin/<uuid:pk>/` | Admin |

---

### 💳 **Transaction**
| Method | Endpoint | Description |
|:------:|:----------|:-------------|
| POST | `/api/transactions/create/` | Create a new transaction |
| GET | `/api/transactions/list/` | List all transactions (paginated) |
| GET | `/api/transactions/<uuid:id>/` | Retrieve a transaction by ID |
| GET | `api/customers/<uuid:customer_id>/transactions/` | View all transactions for a customer |

---

## 🧠 Swagger API Documentation

After setup, visit:

```
http://127.0.0.1:8000/swagger/
```
or  
```
http://127.0.0.1:8000/api/docs/
```
to explore all endpoints interactively.

---

## 🧪 Running Tests

Run all automated tests:
```bash
python manage.py test
```

Alternatively, use **Postman** for manual endpoint testing.

---

## ⚡ Installation and Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Tech-it-with-Billy/Transaction_Monitoring_System_API.git
cd Transaction_Monitoring_System_API
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up the database
```bash
python manage.py migrate
```

### 5️⃣ Run the development server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧰 Example Transaction Creation (JSON)

```json
{
  "customer": 1,
  "amount": 2000.00,
  "transaction_type": "Deposit",
  "transaction_date": "2025-11-01"
}
```

---

## 🧑‍💻 Developer Notes

- Always create customers before transactions (due to FK relation).
- JWT Authentication required for protected endpoints.
- Pagination and filtering are implemented in the Transaction API.
- Swagger auto-generates API documentation.

---