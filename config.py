import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    
    # 1. PostgreSQL Fix: SQLAlchemy 2.0 requires "postgresql://"
    database_url = os.environ.get("DATABASE_URL", "sqlite:///local.db")
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 2. Redis Configuration
    REDIS_URL = os.environ.get("REDIS_URL", "memory://")