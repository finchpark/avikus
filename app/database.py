from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy로 사용할 DB URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@avikus-db-1:5432/postgres"

# Engine 생성
engine = create_engine(
	SQLALCHEMY_DATABASE_URL, echo=False
)

# DB 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class 생성
Base = declarative_base()