FROM python:3.14-slim

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh
