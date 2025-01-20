FROM python:3.10-slim

RUN apt update && apt install -y netcat-openbsd

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements/production.txt

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]