from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Local SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./facility.db"

# Create engine (check_same_thread is needed for SQLite in FastAPI)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session factory for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your SQLAlchemy models
Base = declarative_base()