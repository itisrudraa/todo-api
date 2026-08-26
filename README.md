# Todo API

A RESTful Todo API built with **FastAPI** and **PostgreSQL**, using **SQLAlchemy** for database operations, **Pydantic** for validation, and **JWT-based authentication** for secure user access.

The API supports user registration, login, authentication, and user-specific Todo management with authorization to prevent users from accessing other users' Todos.

## 🛠️ Tech Stack

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![pwdlib](https://img.shields.io/badge/pwdlib-Password_Hashing-555555?style=for-the-badge)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


### Libraries & Tools

- **SQLAlchemy** - Database toolkit and ORM
- **Pydantic** - Request and response validation
- **PyJWT** - JWT creation and token validation
- **pwdlib** - Secure password hashing and verification
- **python-dotenv** - Environment variable management
- **PostgreSQL** - Relational database

## Features

- User registration
- Secure password hashing
- User login with JWT authentication
- Authentication using Bearer tokens
- User-specific Todo management
- Authorization to prevent access to other users' Todos
- Create Todos
- Get authenticated user's Todos
- Get a Todo by ID
- Update Todo title and completion status
- Delete Todos
- Request validation using Pydantic
- Response validation using Pydantic
- PostgreSQL database integration
- Database CRUD operations using SQLAlchemy ORM
- SQLAlchemy relationships between Users and Todos
- Environment variables for configuration
- Partial updates using `PATCH`
- HTTP error handling
- Organized routes using `APIRouter`

## Project Structure

```text
todo-api/
│
├── routes/
│   ├── todos.py
│   └── auth.py
│
├── utils/
│   ├── helper.py
│   └── password.py
│
├── database.py       # SQLAlchemy engine, sessions and database operations
├── models.py         # Pydantic models
├── db_models.py      # SQLAlchemy ORM models
├── main.py
├── .env
├── .gitignore
└── requirements.txt
```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/user/register` | Register a new user |
| `POST` | `/user/login` | Login and receive a JWT |
| `GET` | `/user/is_auth` | Verify authentication and return the current user |

### Todos

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/todos` | Get the authenticated user's Todos |
| `POST` | `/todos` | Create a Todo for the authenticated user |
| `GET` | `/todos/{todo_id}` | Get a Todo owned by the authenticated user |
| `PATCH` | `/todos/{todo_id}` | Update a user's Todo |
| `DELETE` | `/todos/{todo_id}` | Delete a user's Todo |

## Example Todo

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

## Database

The API uses **PostgreSQL** for persistent data storage and **SQLAlchemy ORM** for database operations.

The database layer is separated from the API routes:

```text
FastAPI Route
      ↓
SQLAlchemy ORM
      ↓
PostgreSQL
```

The database layer uses SQLAlchemy to interact with PostgreSQL. SQLAlchemy handles database sessions, queries, and CRUD operations, while psycopg provides the PostgreSQL database driver.

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

PostgreSQL is also responsible for generating Todo IDs.

## Environment Variables

Database credentials are stored in a `.env` file and are not committed to the repository.

Example .`env`:
```text
DB_URL = your_db_url

SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```
## Setup
### 1. Clone the repository
```bash
git clone https://github.com/itisrudraa/todo-api
cd todo-api
```
### 2. Create a virtual environment
```bash
python -m venv venv
```

### Activate it on Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure the database

Create a PostgreSQL database named:
```text
todo_db
```

Create a .env file in the project root:

```text
DB_URL = your_db_url

SECRET_KEY=your_secret_key
ALGORITHM=HS256
EXP_TIME=30
```

### 5. Start the server
```bash
fastapi dev main.py
```

The API will be available at:
```
http://127.0.0.1:8000
```
Interactive API documentation:
```
http://127.0.0.1:8000/docs
```

### Learning Progress

This project is being built incrementally to understand backend development fundamentals.

### Completed

- FastAPI application setup
- Routing
- Request parameters
- Request body handling
- Pydantic models
- Response models
- HTTP exceptions
- APIRouter and route organization
- Dependency injection
- PostgreSQL setup
- SQLAlchemy ORM
- SQLAlchemy CRUD operations
- Database session management
- Environment variable configuration
- Migration from in-memory storage to PostgreSQL
- SQLAlchemy relationships and foreign keys
- User model and user-specific Todos
- Password hashing
- User registration
- User login
- JWT authentication
- Authentication dependencies
- Authorization for user-owned Todos

### Next Steps

- Improve transaction and error handling
- Relationship loading strategies
- Testing with pytest
- Database migrations with Alembic
- Refresh tokens and improved authentication flow
- Production deployment