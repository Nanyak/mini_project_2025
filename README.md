# Mini Project

Full-stack application với FastAPI backend, Vue 3 frontend, và PostgreSQL database.

## Tech Stack

### Backend (api/)

- Python 3.14
- FastAPI
- SQLAlchemy + Alembic
- Pydantic
- PostgreSQL (psycopg3)
- UV package manager

### Frontend (web/)

- Vue
- Vuetify
- VueUse
- TypeScript
- Vite

### Infrastructure

- Docker & Docker Compose
- Nginx (reverse proxy)
- PostgreSQL
- pgAdmin

## Setup Project

### 1. Clone và checkout branch

```bash
git checkout -b <your-branch-name>
```

### 2. Install dependencies

**API:**

```bash
docker compose run --rm api uv sync
```

**Web:**

```bash
docker compose run --rm web npm install
```

### 3. Chạy migrations (lần đầu)

```bash
docker compose up -d
docker compose run --rm api alembic upgrade head
```

### 4. Truy cập

- **Frontend:** http://localhost
- **Backend API:** http://localhost/api
- **API Docs:** http://localhost/api/docs
- **pgAdmin:** http://localhost:5000
  - Email: `admin@admin.com`
  - Password: `admin`

### 5. Setup Database Connection trong pgAdmin (Optional)

1. Login pgAdmin với thông tin trên
2. Click **Add New Server**
3. **General tab:**
   - Name: `mini_project`
4. **Connection tab:**
   - Host: `postgres`
   - Port: `5432`
   - Username: `postgres`
   - Password: `postgres`
   - Database: `mini_project`

Truy cập: http://localhost:5173

## Database & Migrations

### Tạo Migration Mới

Sau khi thêm/sửa models trong `api/models/`:

```bash
docker compose run --rm api alembic revision --autogenerate -m "mô tả thay đổi"


### Apply Migrations

```bash
docker compose run --rm api alembic upgrade head
```
## Code Quality

### Pre-commit Hooks

Cài đặt:

```bash
pip install pre-commit
pre-commit install
```

Hooks bao gồm:

- **Ruff** (Python linter + formatter)
- **Biome** (JS/TS/Vue linter + formatter)
- **Oxlint** (Fast JS/TS linter)
- **Pre-commit hooks** (trailing-whitespace, end-of-file-fixer, check-yaml, check-added-large-files, detect-aws-credentials)

Chạy thủ công:

```bash
pre-commit run --all-files
```

## Cấu trúc Project

```
.
├── api/                      # FastAPI backend
│   ├── alembic/              # Database migrations
│   │   ├── versions/         # Migration files
│   │   └── env.py
│   ├── db/                   # Database config
│   │   └── database.py
│   ├── models/               # SQLAlchemy models
│   │   └── user.py
│   ├── routers/              # API routes
│   │   └── users.py
│   ├── schemas/              # Pydantic schemas
│   │   └── user.py
│   ├── services/             # Business logic
│   │   └── users_service.py
│   ├── dependencies.py       # Dependency injection
│   ├── main.py               # FastAPI app
│   ├── alembic.ini           # Alembic config
│   ├── pyproject.toml        # Dependencies
│   └── Dockerfile
├── web/                      # Vue 3 frontend
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── router/
│   │   ├── views/
│   │   ├── App.vue
│   │   └── main.ts
│   ├── public/
│   ├── package.json
│   ├── vite.config.ts
│   └── Dockerfile
├── nginx/                    # Nginx reverse proxy
│   └── nginx.conf
├── .pre-commit-config.yaml   # Pre-commit hooks
├── biome.json                # Biome config
├── docker-compose.yml        # Docker compose
└── README.md
```
