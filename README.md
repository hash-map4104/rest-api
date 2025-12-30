# REST API using FastAPI 🚀

A backend REST API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, following best practices for authentication, database migrations, and API design.

This project is inspired by the **freeCodeCamp Python API Development course** and focuses purely on backend development.

---

## 📌 Features

- User authentication using **JWT (OAuth2)**
- Secure password hashing
- CRUD operations for posts
- Voting system (like / unlike posts)
- PostgreSQL database integration
- Database migrations using **Alembic**
- Environment-based configuration
- Auto-generated API documentation (Swagger UI)

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Migrations:** Alembic  
- **Authentication:** OAuth2 + JWT  
- **Password Hashing:** Passlib (bcrypt)  
- **Server:** Uvicorn  

---


---

####### SETUP INSTRUCTIONS->

###  CLONE THE REPOSITORY

### CREATE A VIRTUAL ENVIRONMENT
python -m venv env
source env/bin/activate   # macOS / Linux
env\Scripts\activate      # Windows


### INSTALL DEPENDENCIES
pip install -r requirements.txt


### CREATE A .env FILE
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30





