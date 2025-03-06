# 🌱 EcoTrack - Sustainable E-Commerce Backend

## 🚀 Overview
EcoTrack is a sustainability-focused **e-commerce platform** that allows users to:
- ✅ **Browse & purchase eco-friendly products** 🛍️
- ✅ **Track their carbon footprint** 🌍
- ✅ **Earn rewards for sustainable shopping habits** 🎖️

The backend is built using **Django and Django REST Framework (DRF)**, with **JWT authentication**, and supports **Chapa, PayPal, and Stripe** for payments.

---

## 📌 Features

### 🛒 E-Commerce Core
- **Product Management**: Create, update, and delete eco-friendly products.
- **Category Management**: Organize products into categories.
- **Order Processing**: Track orders from **Pending → Paid → Shipped → Delivered**.
- **Payments**: Secure transactions with **Chapa, PayPal, and Stripe**.

### 🔒 User Authentication & Profiles
- **JWT-based authentication** (Login, Register, Logout).
- **Profile Management**: Users can update their profile info.
- **Sustainability Goals**: Users set goals for reducing their carbon footprint.

### 🌍 Sustainability & Rewards
- **Eco Actions**: Users earn points for **sustainable actions** (e.g., buying reusable items).
- **Carbon Footprint Tracking**: Monitor carbon savings from purchases.
- **Rewards System**: Users collect points for eco-friendly actions.

### 🔍 Filtering, Sorting & Pagination
- Filter products by **category**.
- Sort products by **price**.
- Paginated product listing for efficiency.

### 📑 API Documentation
- **Swagger/OpenAPI** for interactive API testing.
- **Postman Collection** included for easy testing.

---

## ⚙️ Tech Stack

| Component           | Technology |
|--------------------|------------|
| **Backend**       | Django, Django REST Framework (DRF) |
| **Database**      | PostgreSQL |
| **Authentication** | JWT (JSON Web Tokens) |
| **Payments**      | Chapa, PayPal, Stripe |
| **Task Queue**    | Celery + Redis (for async tasks) |
| **API Docs**      | Swagger / drf-yasg |

---

## 🏗 Database Schema (ERD)
👉 **View the full ERD on dbdiagram.io**: [Click Here](https://drive.google.com/file/d/1Wum2zSyAwAleKhMrJSqkirqHniSrEo1w/view?usp=sharing)

The **key database tables**:
- **Users & Profiles**: `User`, `Profile`, `SustainabilityGoal`
- **Products & Categories**: `Product`, `Category`, `CarbonData`
- **Orders & Payments**: `Order`, `OrderItem`, `Payment`
- **Eco Actions & Rewards**: `EcoAction`, `Reward`, `CarbonImpact`

---

## 🔌 API Endpoints

### 🔑 Authentication (JWT)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/users/register/` | Register a new user |
| POST   | `/api/users/login/` | Login & get JWT token |
| POST   | `/api/users/logout/` | Logout user |

### 🛍️ Products & Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/products/` | List all products (with filtering, sorting, pagination) |
| POST   | `/api/products/` | Add a new product (Admin only) |
| GET    | `/api/products/{id}/` | Retrieve a product |
| PUT    | `/api/products/{id}/` | Update a product (Admin only) |
| DELETE | `/api/products/{id}/` | Delete a product (Admin only) |
| GET    | `/api/products/categories/` | List all categories |

### 📦 Orders & Payments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/orders/` | List all orders for a user |
| POST   | `/api/orders/` | Create a new order |
| GET    | `/api/orders/{id}/` | Retrieve an order |
| POST   | `/api/orders/{id}/pay/` | Make a payment (Chapa, PayPal, Stripe) |

### 🎖️ Eco Actions & Rewards
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/actions/` | List all eco-friendly actions |
| POST   | `/api/actions/` | Log an eco action |
| GET    | `/api/rewards/` | View earned rewards |

---


### 7️⃣ Access API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 🚀 Deployment
### Deploy to PythonAnywhere 
- Use **Gunicorn & Nginx** for production
- Configure **PostgreSQL** for production database
- Set up **Celery & Redis** for background tasks
- Use **CORS Headers** for cross-origin API access

---

## 🎯 Evaluation Criteria
✅ **Functionality**: Complete CRUD APIs, filtering, sorting, pagination  
✅ **Code Quality**: Clean, modular, and well-structured codebase  
✅ **Security**: Proper authentication and secure transactions  
✅ **API Documentation**: Well-documented API for frontend integration  
✅ **Version Control**: Frequent commits with meaningful messages  

---

## 🎉 Contributors
👤 **Timothy Kipyego**  
📧 **timothykipyego@gmail.com**  
🔗 **https://www.linkedin.com/in/timothykipyego/**  

---

### 🌟 Built for a Greener Future! 🌍♻️
Let’s promote sustainability through smart shopping & responsible consumption! 🚀

