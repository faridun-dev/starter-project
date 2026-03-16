# ⚡ FastAPI Starter Template

This template provides a **clean and scalable starting point** for building APIs with **FastAPI**.

It is designed to give developers a **production-ready structure** while staying simple enough for small projects. The architecture separates **routers, services, and configuration**, making the project easy to maintain and extend.

---

# ✨ Features

- ⚡ Built with **FastAPI**
- 🚀 Ready-to-run API server
- 🧱 Modular and scalable project structure
- ⚙️ Environment configuration using `.env`
- 📦 Dependency management with `uv`
- 🧩 Router-based API structure
- 📘 Automatic API documentation
- 🧼 Clean architecture principles

---

# 📦 Requirements

- Python **3.10+**
- `uv` package manager

Install `uv` if you don't have it:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

# 🚀 Getting Started

## 1. Install dependencies

```bash
uv sync
```

Or manually install:

```bash
uv add fastapi uvicorn pydantic-settings python-dotenv
```

---

## 2. Configure environment variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env`:

```env
APP_NAME=FastAPI Application
DEBUG=true
```

---

## 3. Run the server

```bash
uv run uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# 📘 API Documentation

FastAPI automatically generates API docs.

Open in browser:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📁 Project Structure

```
fastapi_project/
│
├── pyproject.toml
├── README.md
├── .env
├── .env.example
│
├── app/
│   ├── __init__.py
│   │
│   ├── main.py
│   ├── config.py
│
│   ├── routers/
│   │   ├── __init__.py
│   │   └── health.py
│
│   ├── services/
│   │   └── example_service.py
│
│   ├── models/
│   │   └── example_model.py
│
│   └── schemas/
│       └── example_schema.py
│
└── tests/
```

---

# 🧠 How It Works

### `main.py`

Application entry point.

Responsible for:

- Creating FastAPI app
- Registering routers
- Starting the server

Example:

```python
from fastapi import FastAPI
from app.routers import health

app = FastAPI()

app.include_router(health.router)
```

---

### `config.py`

Handles environment configuration.

Example:

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
```

---

### `routers/`

Contains API endpoints.

Example:

```
GET /health
GET /users
POST /users
```

Example router:

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}
```

---

### `services/`

Business logic layer.

Handlers should remain thin and delegate logic to services.

Example responsibilities:

- database operations
- external APIs
- background tasks

---

### `models/`

Database models or domain models.

Examples:

- SQLAlchemy models
- ORM classes
- internal data structures

---

### `schemas/`

Pydantic schemas for:

- request validation
- response models
- serialization

Example:

```python
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
```

---

# 🧪 Testing

Tests can be added inside:

```
tests/
```

Recommended tools:

```
pytest
pytest-asyncio
httpx
```

Example:

```bash
uv add pytest pytest-asyncio httpx --dev
```

Run tests:

```bash
pytest
```

---

# 🔧 Development Tips

Run development server:

```bash
uv run uvicorn main:app --reload
```

Add new dependency:

```bash
uv add package_name
```

Update lockfile:

```bash
uv lock
```

---

# 📈 Possible Extensions

This template can easily be extended with:

- PostgreSQL
- SQLAlchemy
- Alembic migrations
- Redis caching
- Authentication (JWT)
- Background workers
- Docker support
- Clean Architecture
- Microservices

---

# 📜 License

This template is provided as part of the **PyStart project**.

You are free to modify and use it in your own projects.

---

# 🚀 Happy Coding

Build fast and scalable APIs with **FastAPI** and **PyStart**.
