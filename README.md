# Todo API

A RESTful Todo API built with **FastAPI** and **PostgreSQL**.

This project was built incrementally to understand backend development fundamentals. It started with in-memory storage using a Python dictionary and was later migrated to PostgreSQL using `psycopg`.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Psycopg](https://img.shields.io/badge/Psycopg-336791?style=for-the-badge&logo=python&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)


### Libraries & Tools

- **Pydantic** - Request and response validation
- **psycopg** - PostgreSQL database connectivity
- **python-dotenv** - Environment variable management

## Features

- Create Todos
- Get all Todos
- Get a Todo by ID
- Update Todo title and completion status
- Delete Todos
- Request validation using Pydantic
- Response validation using Pydantic
- PostgreSQL database integration
- SQL CRUD operations
- Environment variables for database credentials
- Automatic ID generation by PostgreSQL
- Partial updates using `PATCH`
- HTTP error handling for invalid Todo IDs
- Organized routes using `APIRouter`

## Project Structure

```text
todo-api/
│
├── routes/
│   └── todos.py          # Todo API routes
│
├── database.py           # PostgreSQL connection and SQL operations
├── models.py             # Pydantic request/response models
├── main.py               # FastAPI application entry point
├── .env                  # Local database credentials
├── .gitignore
└── requirements.txt
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/todos` | Get all Todos |
| `POST` | `/todos` | Create a Todo |
| `GET` | `/todos/{todo_id}` | Get a Todo by ID |
| `PATCH` | `/todos/{todo_id}` | Update a Todo |
| `DELETE` | `/todos/{todo_id}` | Delete a Todo |

## Example Todo

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

## Database

The API uses PostgreSQL for persistent data storage.
Database operations are separated from the API routes:
```text
FastAPI Route
      ↓
database.py
      ↓
psycopg
      ↓
PostgreSQL
```
The database layer handles SQL operations such as:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

PostgreSQL is also responsible for generating Todo IDs.

## Environment Variables

Database credentials are stored in a `.env` file and are not committed to the repository.

Example .`env`:
```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=your_password
```
## Setup
### 1. Clone the repository
```bash
git clone <your-repository-url>
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
DB_HOST=localhost
DB_PORT=5432
DB_NAME=todo_db
DB_USER=postgres
DB_PASSWORD=your_password
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

* Completed
* FastAPI application setup
* Routing
* Request parameters
* Request body handling
* Pydantic models
* Response models
* HTTP exceptions
* APIRouter and route organization
* Dependency injection basics
* PostgreSQL setup
* psycopg database connections
* SQL CRUD operations
* Environment variable configuration
* Migration from in-memory dictionary storage to PostgreSQL
### Next Steps
* Improve database connection management
* Better transaction and error handling
* Database-backed dependencies
* Testing with pytest
* Authentication and authorization
* User-specific Todos
* Database migrations
* Production deployment