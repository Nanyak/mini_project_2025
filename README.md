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

- Vue 3.5
- Vuetify 3.10
- VueUse 14.0
- TypeScript 5.9
- Vite 7.1

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
docker exec mini-project-api-1 /root/.local/bin/uv run alembic upgrade head
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
   - Host: `db`
   - Port: `5432`
   - Username: `postgres`
   - Password: `postgres`
   - Database: `mini_project`

## Local Development (không dùng Docker)

### Backend

```bash
cd api
uv sync
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Truy cập: http://localhost:8000/docs

### Frontend

```bash
cd web
npm install
npm run dev
```

Truy cập: http://localhost:5173

## Database & Migrations

### Tạo Migration Mới

Sau khi thêm/sửa models trong `api/models/`:

```bash
# Trong Docker (recommended)
docker exec mini-project-api-1 /root/.local/bin/uv run alembic revision --autogenerate -m "mô tả thay đổi"

# Local
cd api
uv run alembic revision --autogenerate -m "mô tả thay đổi"
```

### Apply Migrations

```bash
docker exec api /root/.local/bin/uv run alembic upgrade head
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

## Testing

```bash
# Chạy tất cả tests
docker exec mini-project-api-1 /root/.local/bin/uv run pytest

# Chạy test cụ thể
docker exec mini-project-api-1 /root/.local/bin/uv run pytest tests/test_users.py

# Chạy với coverage
docker exec mini-project-api-1 /root/.local/bin/uv run pytest --cov=.
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
│   ├── tests/                # Tests
│   │   └── test_users.py
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

## Workflow Thông Thường

1. **Checkout branch mới**

   ```bash
   git checkout -b feature/your-feature
   ```

2. **Sửa code**

   - Backend: `api/models/`, `api/routers/`, `api/services/`
   - Frontend: `web/src/`

3. **Nếu sửa models, tạo migration**

   ```bash
   docker exec mini-project-api-1 /root/.local/bin/uv run alembic revision --autogenerate -m "add new field"
   docker compose restart api
   ```

4. **Test**

   ```bash
   docker exec mini-project-api-1 /root/.local/bin/uv run pytest
   ```

5. **Commit** (pre-commit hooks sẽ tự chạy)

   ```bash
   git add .
   git commit -m "feat: your feature"
   ```

6. **Push và tạo PR**
   ```bash
   git push origin feature/your-feature
   ```

## Troubleshooting

### Container không start

```bash
docker compose down -v
docker compose up -d
```

### Database connection error

```bash
# Check db container
docker compose ps db

# Check logs
docker compose logs db
```

### Migration error

```bash
# Reset migrations
docker exec mini-project-api-1 /root/.local/bin/uv run alembic downgrade base
docker exec mini-project-api-1 /root/.local/bin/uv run alembic upgrade head
```

### Port already in use

```bash
# Thay đổi port trong docker-compose.yml
# Ví dụ: "8001:8000" thay vì "8000:8000"
```
### References:
https://dev.to/mohammad222pr/structuring-a-fastapi-project-best-practices-53l6
