from pydantic import BaseModel
from typing import Optional, List
from datetime import date
import base64


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: Optional[str]  # Optional because it will be generated if not provided
    username: str
    password: str

    class Config:
        # This is important to convert SQLAlchemy objects to Pydantic models
        from_attributes = True


class CurrentAmountEntry(BaseModel):
    id: int
    payment_amount: int
    date: date


class CustomerCreate(BaseModel):
    app_no: int
    username: str
    address: str
    ph_no: str
    item_weight: int
    amount: int
    pending: int
    current_amount: int
    start_date: str
    end_date: str
    note: str


class PaymentEntry(BaseModel):
    payment: int
    date: str  # Date is a string in the payment history (ISO format)

    class Config:
        from_attributes = True  # This enables conversion from ORM models


class CustomerOut(BaseModel):
    id: Optional[str]
    app_no: int
    username: str
    address: str
    ph_no: int
    item_weight: int
    amount: int
    pending: int
    payment_history: str | List
    start_date: date
    end_date: date
    note: str
    image: str
    status: str

    class Config:
        from_attributes = True
