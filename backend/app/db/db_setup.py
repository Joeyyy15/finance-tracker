from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#SQLite for now; might swap later with postgreSQL
SQLALCHEMY_DATABASE_URL = "sqlite:///./finance.db"

#SQLAlchemy egine connects python to the DB
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Session generator for DB access
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for all models
base = declarative_base()