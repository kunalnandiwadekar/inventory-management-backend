# 🏭 Inventory Management System - Backend

A high-performance, scalable backend service for managing inventory operations, built with FastAPI and PostgreSQL. Features real-time stock tracking, comprehensive reporting, and robust authentication.

## ✨ Key Features

- **Product Management** - Full CRUD operations with categories and variants
- **Stock Control** - Real-time inventory tracking with stock in/out operations
- **Supplier Integration** - Manage suppliers and track purchase history
- **Automated Alerts** - Low stock notifications
- **Comprehensive Reporting** - Stock levels, sales, and inventory valuation
- **Secure Authentication** - JWT-based with role-based access control
- **RESTful API** - Clean, intuitive endpoints following best practices

## 🚀 Live API

- **Base URL**: `https://inventory-backend-16mw.onrender.com`
- **Interactive API Docs**: [Swagger UI](https://inventory-backend-16mw.onrender.com/docs)

## 🛠 Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL (Hosted on Render)
- **ORM**: SQLAlchemy 2.0
- **Data Validation**: Pydantic v2
- **ASGI Server**: Uvicorn
- **API Documentation**: OpenAPI (Swagger & ReDoc)

## 📦 API Endpoints

### Authentication
- `POST /auth/login` - User authentication

### Products
- `GET /products` - List all products
- `POST /products` - Create new product
- `GET /products/{id}` - Get product details
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product
- `POST /products/{id}/stock-in` - Add stock
- `POST /products/{id}/stock-out` - Remove stock

### Suppliers
- `GET /suppliers` - List all suppliers
- `POST /suppliers` - Add new supplier
- `GET /suppliers/{id}` - Get supplier details

### Reports
- `GET /reports/summary` - Inventory summary
- `GET /reports/low-stock` - Low stock alerts
- `GET /reports/valuation` - Inventory valuation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL 13+
- pip (Python package manager)

### Local Development

1. **Clone the repository**
   ```bash
   git clone [https://github.com/yourusername/inventory-management-backend.git](https://github.com/yourusername/inventory-management-backend.git)
   cd inventory-management-backend

2. **Set up virtual environment**
bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Unix/macOS
source venv/bin/activate
3. **Install dependencies**
bash
pip install -r requirements.txt
4. **Environment Setup**
bash
cp .env.example .env
# Edit .env with your database credentials
5. **Database Setup**
bash
# Create database
createdb inventory_db
# Run migrations
alembic upgrade head
6. **Start the server**
bash
uvicorn app.main:app --reload
# 🔧 Configuration
Create a .env file with:
```bash
env
```
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/inventory_db
# Authentication
SECRET_KEY=your-secure-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# 🌐 Deployment
The application is deployed on Render with the following configuration:

- Automatic deploys from main branch
- PostgreSQL database
- Automatic SSL certificates
- Health checks and auto-restart
# 🤝 Contributing
- Fork the repository
- Create feature branch (git checkout -b feature/AmazingFeature)
- Commit changes (git commit -m 'Add some AmazingFeature')
- Push to branch (git push origin feature/AmazingFeature)
- Open a Pull Request
# 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

# 👤 Author
Kunal Nandiwadekar
Full Stack Developer
GitHub | LinkedIn
