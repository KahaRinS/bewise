#!/bin/bash

function wait_for_db() {
  echo "Ожидание доступности базы данных..."
  until nc -z "$DB_HOST" "$DB_PORT"; do
    echo "База данных недоступна. Повторная проверка через 1 секунду..."
    sleep 1
  done
  echo "База данных доступна!"
}

DB_HOST=${POSTGRES_HOST:-localhost}
DB_PORT=${POSTGRES_PORT:-5432}

wait_for_db

echo "Applying database migrations..."
alembic upgrade head

echo "Starting FastAPI application..."
exec python3 main.py start