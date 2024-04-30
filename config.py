import os
from datetime import timedelta

class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@postgres:5432/postgres",
    )
    VERYFI_API_KEY = os.environ.get("VERYFI_API_KEY")
    VERYFI_CLIENT_ID = os.environ.get("VERYFI_CLIENT_ID")
    MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-3.5-turbo")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 4))
    )
    JWT_ERROR_MESSAGE_KEY = os.environ.get("JWT_ERROR_MESSAGE_KEY", "error")
