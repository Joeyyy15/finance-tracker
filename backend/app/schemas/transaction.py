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
        from_attributes = True

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

class CategoryTotal(BaseModel):
    category:str
    total: float

class GoalCreate(BaseModel):
    category_id: int
    weekly_budget: float

class GoalUpdate(BaseModel):
    weekly_budget: Optional[float] = None

# what the API returns after creating/listing/updating a goal
class GoalOut(BaseModel):
    id: int
    weekly_budget: float
    category:CategoryOut

    class Config:
        from_attributes = True
        