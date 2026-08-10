# 📝 Todo API

A simple **Todo REST API** built with **FastAPI**.

This project is being developed incrementally to learn API development, request validation, routing, and CRUD operations with FastAPI.

## 🚀 Features
* Create a todo
* Get all todos
* Get a todo by ID
* Update a todo
* Delete a todo

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=uvicorn&logoColor=white)

## 💾 Storage

Currently, the API uses **in-memory Python data structures** for storing todos.

> ⚠️ Data will be lost whenever the server restarts.

Database integration will be added in a later version.


## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/itisrudraa/todo-api
```

### 2. Navigate into the project

```bash
cd todo-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the server

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🎯 Project Status

🚧 **Work in Progress**

This is primarily a learning project. New features and improvements will be added as I learn more about FastAPI and REST API development.

## 📌 Future Improvements

* 🗄️ Add a database
* 🔐 Add authentication
* ✅ Complete CRUD operations
* 🧪 Add automated tests
* ⚠️ Improve validation and error handling
* 📊 Add proper response models
* 🐳 Dockerize the application

---

⭐ Built while learning **FastAPI and REST API development**.
