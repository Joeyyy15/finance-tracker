from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    category: str

class TransactionOut(TransactionCreate):
    id: int
    date: datetime

    class Config:
        orm_mode = True
        