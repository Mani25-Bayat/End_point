# Clean Architecture API

A minimal, production-ready FastAPI project following **Clean Architecture** with strict layer separation.

## Architecture

```
HTTP Request
    │
    ▼
┌─────────────────────────────────────┐
│  Interface Adapters                 │
│  Schema → Router → Controller       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Application                        │
│  UseCase → Service → Pattern        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Infrastructure                     │
│  Config, HTTP, Exception handling   │
└─────────────────────────────────────┘
```

### Layers

| Layer | Responsibility |
|---|---|
| **Application** | Business logic (use cases, services, patterns, domain exceptions). Framework-agnostic. |
| **Interface Adapters** | Translates between HTTP and application (schemas, controllers, routers). |
| **Infrastructure** | Framework concerns (FastAPI setup, settings, global error handling). |

### Dependency Rule

Dependencies point **inward only**: Interface Adapters → Application ← Infrastructure.  
The Application layer never imports FastAPI or any framework code.

## Endpoint

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/v1/placeholder` | Returns a greeting message |

**Request:**
```json
{ "name": "Farnoosh" }
```

**Response:**
```json
{ "message": "Hello Farnoosh, this is a clean architecture placeholder." }
```

## Run Locally

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy environment file
cp .env.example .env

# 4. Start the server
uvicorn app.main:app --reload
```

## Run with Docker

```bash
# Build and start
docker-compose up --build

# Or run in detached mode
docker-compose up --build -d
```

## Swagger UI

Once running, open your browser:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure

```
app/
├── main.py                              # Composition root
├── core/
│   └── logger.py
├── application/                         # Business logic (no framework imports)
│   ├── usecases/
│   │   └── placeholder_usecase.py
│   ├── services/
│   │   └── greeting_service.py
│   ├── patterns/
│   │   └── message_pattern.py
│   └── exceptions/
│       └── domain_exception.py
├── interface_adapters/                  # HTTP ↔ Application translation
│   ├── controllers/
│   │   └── placeholder_controller.py
│   ├── routers/
│   │   └── placeholder_router.py
│   └── schemas/
│       └── placeholder_schema.py
└── infrastructure/                      # Framework & config
    ├── config/
    │   └── settings.py
    ├── http/
    │   └── exception_handler.py
    └── exceptions/
        └── app_exception.py
```

## Error Handling

All exceptions are handled globally in `infrastructure/http/exception_handler.py`:

| Exception | HTTP Status | When |
|---|---|---|
| `DomainException` | 422 | Business rule violation (e.g. empty name) |
| `AppException` | Custom | Infrastructure-level error |
| `ValidationError` | 422 | Pydantic validation failure |
| Any other `Exception` | 500 | Unexpected server error |
