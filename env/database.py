#url
#engine
#session
#dababase object to interaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Defaults can be overridden via environment variables
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '5431'))  # user stated Postgres runs on 5431
DB_NAME = os.getenv('DB_NAME', 'TodoDatabase')

# Build a safe SQLAlchemy URL (handles encoding and optional password)
database_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD or None,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
)

# Backward-compatible string version if other modules expect this variable
SQLALCHEMY_DATABASE_URL = str(database_url)

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


