FROM python:3.14-slim AS builder

RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN ~/.local/bin/uv sync --frozen


FROM python:3.14-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

EXPOSE 8000
