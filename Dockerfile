FROM python:3.11-slim

WORKDIR /app

# Install necessary PostgreSQL libraries for building psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]
