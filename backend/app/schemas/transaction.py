from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass 

class CategoryOut(CategoryBase):
    id:int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float

class TransactionCreate(BaseModel):
    amount: float
    category_id: int

class TransactionOut(TransactionBase):
    id: int
    date: datetime
    category: CategoryOut

    class Config:
        from_attributes = True
        
class TransactionUpdate(BaseModel):
    # made optional so you can update one or both
    amount: Optional[float] = None
    category_id: Optional[int] = None