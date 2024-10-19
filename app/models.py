from sqlalchemy import Column, String, Integer, Date, JSON, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
import uuid
from enum import Enum as PyEnum

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True, index=True)
    secret_key = Column(String, nullable=False)
    uri = Column(String, nullable=False)


class StatusEnum(PyEnum):
    pending: str = "pending"
    completed: str = "completed"

    class Config:
        from_attributes = True


class Customers(Base):
    __tablename__ = "customers"

    id = Column(String(36), primary_key=True, nullable=False,
                default=lambda: str(uuid.uuid4()))
    app_no = Column(Integer, nullable=False, unique=True)
    username = Column(String, nullable=False)
    address = Column(String, nullable=False)
    ph_no = Column(Integer, nullable=False)
    item_weight = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    pending = Column(Integer, nullable=False)
    payment_history = Column(JSON, nullable=False, default=[])
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    note = Column(String, nullable=False)
    image = Column(String, nullable=True)
    # SQLAlchemy Enum with default value
    status = Column(SQLEnum(StatusEnum), nullable=False,
                    default=StatusEnum.pending)

    class Config:
        from_attributes = True
