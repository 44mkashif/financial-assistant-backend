#!/bin/bash

# Run database migrations
flask db upgrade

if [ "$FLASK_ENV" = "development" ]; then
  echo "Running Development Server"
  exec flask run --host=0.0.0.0 --port=8000 --reload
else
  echo "Running Production Server with Gunicorn"
  exec gunicorn --bind 0.0.0.0:8000 app:app
fi
