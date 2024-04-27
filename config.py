import os

class Config:
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@postgres:5432/postgres",
    )
    VERYFI_API_KEY = os.environ.get("VERYFI_API_KEY")
    VERYFI_CLIENT_ID = os.environ.get("VERYFI_CLIENT_ID")