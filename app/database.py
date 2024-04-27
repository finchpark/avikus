from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy로 사용할 DB URL
SQLALCHEMY_DATABASE_URL = "sqllite:///./avikus.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://user:passwrod@postgresserver/db"

# Engine 생성
engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# DB 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class 생성
Base = declarative_base()