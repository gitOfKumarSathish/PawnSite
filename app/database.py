from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLITE_DATABASE_URL = "sqlite:///./gold.db"

engine = create_engine(SQLITE_DATABASE_URL, echo=False,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
