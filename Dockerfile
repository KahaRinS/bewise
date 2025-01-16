FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements/production.txt

EXPOSE 8000

CMD ["python3", "main.py", "start"]