# Burger CI/CD Capstone (FastAPI + Docker + GitHub Actions)

Small FastAPI service that exposes a burger menu (Veg Grilled Paneer Burger + combo),
containerized with Docker and deployed on my local Windows laptop via Docker Compose
and a self-hosted GitHub Actions runner.

## Stack

- FastAPI + Uvicorn
- Docker & Docker Compose
- GitHub Actions (self-hosted runner on Windows)

## End-to-End Flow

1. Developer commits and pushes to GitHub.
2. CI workflow runs tests and builds Docker image.
3. On push to `main`, CD workflow runs on self-hosted runner and executes:
   `docker compose down` and `docker compose up --build -d`.
4. Updated app is available at `http://localhost:8000`.

## How to run locally

```bash
docker compose up --build -d
curl http://localhost:8000/health
curl http://localhost:8000/menu

Scripts
start_app.sh – start via Docker Compose.

stop_app.sh – stop stack.

backup_logs.sh – archive logs with timestamp.
