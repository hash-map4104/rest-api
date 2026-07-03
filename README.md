# REST API using FastAPI

A backend REST API built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic**, following backend best practices for authentication, database migrations, and scalable API design.

## Features
- User authentication using OAuth2 with JWT tokens
- Secure password hashing with Argon2
- CRUD operations for posts
- Voting system for liking and unliking posts
- PostgreSQL database integration
- Database schema migrations with Alembic
- Environment-based configuration using `.env`
- Auto-generated API documentation with Swagger UI

## Tech Stack
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Authentication:** OAuth2 + JWT
- **Password Hashing:** Argon2
- **Server:** Uvicorn

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/hash-map4104/rest-api
cd rest-api
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate
```

For Windows:
```bash
env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file
```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run database migrations
```bash
alembic upgrade head
```

### 6. Start the server
```bash
uvicorn app.main:app --reload
```

## API Documentation
Once the server is running, interactive API docs are available at:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Future Improvements
- Add a frontend client
- Write unit and integration tests
- Dockerize the application
- Add CI/CD pipeline

### 🎥 Video Demonstration
[Click here to watch the Votely-API walkthrough]([https://your-google-drive-link-here](https://drive.google.com/drive/folders/1hehA0sAKQKY10NSSPh6q70-5xs6IH8ob))


The project was successfully deployed previously. The current live deployment is inactive because the hosting subscription has expired, but the codebase, database setup, and local run instructions remain fully functional.
