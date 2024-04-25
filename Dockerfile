
FROM python:3.11-slim

WORKDIR /app

# Install necessary PostgreSQL libraries for building psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

